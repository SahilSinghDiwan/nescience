# ==========================================================
# NESCIENCE — adversarial privacy tests (§11a)
#
# test_identity.py unit-tests the model and test_privacy_routes.py
# covers the happy-path contracts. This file is the attack suite: it
# actively tries to make a private field surface on a public route —
# by sweeping *every* public route for a sentinel real name, by asking
# for an unpublished participant's code directly, by trying case /
# encoding / traversal tricks on the code lookup, by feeding the app
# hand-edited legacy records, and by trying to walk past the
# investigator gate without the password.
#
# Every test drives the real Flask app through its test client against
# a throwaway data file, so no test ever touches participants.json.
# ==========================================================

import hashlib
import json

import pytest
import testutil

import app as flaskapp
import database
import identity

# A name no template, concept, or fixture could produce by accident, so a
# substring hit anywhere in a response body is unambiguously a leak.
SENTINEL = "Zebulon Quarry"

# Every route a visitor can reach without a password.
PUBLIC_PATHS = [
    "/",
    "/interview",
    "/archive",
    "/archive/witnesses",
    "/archive/connections",
    "/archive/open-questions",
    "/archive/evidence-room",
    "/archive/notes",
    "/atlas",
    "/atlas/Memory",
    "/no-such-page-at-all",  # the 404 page
]


@pytest.fixture
def client(tmp_path, monkeypatch):
    """A test client whose archive is an empty temp file, with the
    investigator surface unconfigured (i.e. disabled)."""
    data = tmp_path / "participants.json"
    data.write_text("[]")
    monkeypatch.setattr(database, "FILE_NAME", str(data))
    monkeypatch.delenv("NESCIENCE_INVESTIGATOR_PASSWORD", raising=False)
    return flaskapp.app.test_client()


@pytest.fixture
def seeded(tmp_path, monkeypatch):
    """A client plus a writer that installs arbitrary *raw* records —
    used to forge legacy / hand-edited participants.json shapes that the
    API route itself would never produce."""
    data = tmp_path / "participants.json"
    data.write_text("[]")
    monkeypatch.setattr(database, "FILE_NAME", str(data))
    monkeypatch.delenv("NESCIENCE_INVESTIGATOR_PASSWORD", raising=False)

    def write(records):
        data.write_text(json.dumps(records))

    return flaskapp.app.test_client(), write


@pytest.fixture
def gated(tmp_path, monkeypatch):
    """A client with the investigator surface configured and locked."""
    data = tmp_path / "participants.json"
    data.write_text("[]")
    monkeypatch.setattr(database, "FILE_NAME", str(data))
    monkeypatch.setenv("NESCIENCE_INVESTIGATOR_PASSWORD", "letmein")
    return flaskapp.app.test_client()


def _file(client, name, published, answer="A childhood memory of family and loss."):
    return client.post("/api/interview", json={
        "name": name,
        "published": published,
        "Participant Information": {"Age": "31", "Country": "India"},
        "Module I — Experience": {"Question 1": answer},
    })


# ----------------------------------------------------------
# The sentinel sweep — the real name must not appear in the bytes of
# any public response, by any channel (markup, comment, attribute,
# embedded JSON, header, redirect target).
# ----------------------------------------------------------

def test_sentinel_name_appears_in_no_public_response_body(client):
    _file(client, SENTINEL, published=True)
    _file(client, "Private Person", published=False)
    for path in PUBLIC_PATHS + ["/archive/witnesses/ZE", "/archive/0"]:
        body = client.get(path, follow_redirects=True).get_data(as_text=True)
        assert "Zebulon" not in body, path      # given name
        assert "Quarry" not in body, path       # family name
        assert "Private Person" not in body, path


def test_sentinel_name_appears_in_no_public_response_header(client):
    _file(client, SENTINEL, published=True)
    for path in PUBLIC_PATHS + ["/archive/witnesses/ZE", "/archive/0"]:
        r = client.get(path)
        assert "Zebulon" not in repr(dict(r.headers)), path


def test_redirect_location_carries_the_code_not_the_name(client):
    _file(client, SENTINEL, published=True)
    r = client.get("/archive/0")
    assert r.status_code in (301, 302)
    assert "Zebulon" not in r.headers["Location"]
    assert "/archive/witnesses/ZE" in r.headers["Location"]


def test_api_reply_never_echoes_the_name_and_hides_url_when_private(client):
    data = _file(client, SENTINEL, published=False).get_json()
    assert data["published"] is False
    assert data["public_url"] is None       # no public handle for a private record
    assert "Zebulon" not in json.dumps(data)


def test_witness_page_exposes_no_private_field_labels(client):
    _file(client, SENTINEL, published=True)
    body = client.get("/archive/witnesses/ZE").get_data(as_text=True)
    # The private Case File block — name, mapping, recorded timestamp — is
    # dropped at the source, so none of its keys can reach the page.
    assert "Case File" not in body
    assert "Recorded" not in body
    assert "Zebulon" not in body


def test_public_projection_carries_only_code_and_responses(client):
    _file(client, SENTINEL, published=True)
    entry = identity.public_projection(database.load_interviews())[0]
    assert set(entry) == {"code", "responses"}
    assert "Case File" not in entry["responses"]
    assert "Zebulon" not in repr(entry)


# ----------------------------------------------------------
# Opt-in publication — an unpublished record must be unreachable, even
# by someone who knows its code.
# ----------------------------------------------------------

def test_unpublished_code_is_404_when_requested_directly(client):
    code = _file(client, "Hidden Hank", published=False).get_json()["code"]
    assert code == "HI"
    r = client.get(f"/archive/witnesses/{code}")
    assert r.status_code == 404
    assert "Hidden Hank" not in r.get_data(as_text=True)


def test_unpublished_answers_reach_no_public_route(client):
    _file(client, "Hidden Hank", published=False,
          answer="the unpublishable sentence about my mother")
    for path in PUBLIC_PATHS + ["/archive/witnesses/HI", "/archive/0"]:
        body = client.get(path, follow_redirects=True).get_data(as_text=True)
        assert "unpublishable sentence" not in body, path


def test_unpublished_record_404s_between_published_neighbours(client):
    _file(client, "Pub One", published=True)
    _file(client, "Hidden Hank", published=False)
    _file(client, "Pub Two", published=True)
    assert client.get("/archive/1").status_code == 404
    assert client.get("/archive/0").status_code in (301, 302)
    assert client.get("/archive/2").status_code in (301, 302)


def test_witness_list_links_only_published_codes(client):
    _file(client, "Pub One", published=True)
    _file(client, "Hidden Hank", published=False)
    body = client.get("/archive/witnesses").get_data(as_text=True)
    assert "witnesses/PU" in body
    assert "witnesses/HI" not in body


def test_public_witness_list_exposes_no_recorded_timestamps(client):
    # Timestamps alongside codes would let an observer reconstruct the
    # order codes were issued in; the Case File block keeps them private.
    _file(client, "Ann Early", published=True)
    _file(client, "Bob Later", published=True)
    body = client.get("/archive/witnesses").get_data(as_text=True)
    assert "Recorded" not in body


# ----------------------------------------------------------
# Code-lookup tricks — case, encoding, traversal, out-of-range indices.
# ----------------------------------------------------------

def test_code_lookup_is_exact_and_case_sensitive(client):
    _file(client, "Zoe", published=True)
    assert client.get("/archive/witnesses/ZO").status_code == 200
    for variant in ["zo", "Zo", "zO", "ZO1", "Z", "ZZ"]:
        assert client.get(f"/archive/witnesses/{variant}").status_code == 404, variant


def test_code_lookup_rejects_traversal_and_junk(client):
    _file(client, "Zoe", published=True)
    for junk in ["%2e%2e%2f%2e%2e%2fetc%2fpasswd", "..", "*", "__init__",
                 "None", "ZO%20"]:
        r = client.get(f"/archive/witnesses/{junk}")
        assert r.status_code in (404, 308), (junk, r.status_code)


def test_urlencoded_code_resolves_only_to_a_published_record(client):
    _file(client, "Zoe", published=True)          # ZO
    _file(client, "Hidden Hank", published=False)  # HI
    assert client.get("/archive/witnesses/%5A%4F").status_code == 200   # ZO
    assert client.get("/archive/witnesses/%48%49").status_code == 404   # HI


def test_out_of_range_indices_404(client):
    _file(client, "Zoe", published=True)
    assert client.get("/archive/-1").status_code == 404
    assert client.get("/archive/999999").status_code == 404


# ----------------------------------------------------------
# Legacy / hand-edited records — a record that predates the consent
# model must never become publicly visible by default.
# ----------------------------------------------------------

def test_legacy_record_without_a_published_key_is_invisible(seeded):
    client, write = seeded
    write([{"Participant Information": {"Age": "44"},
            "Module I — Experience": {"Question 1": "a legacy memory of family"}}])
    body = client.get("/archive/witnesses").get_data(as_text=True)
    assert "legacy memory" not in body
    assert "No testimony has been published" in body
    assert client.get("/archive/0").status_code == 404


def test_legacy_record_with_a_name_but_no_consent_leaks_nothing(seeded):
    client, write = seeded
    write([{"Case File": {"Name": SENTINEL, "Recorded": "2020-01-01 00:00"},
            "Module I — Experience": {"Question 1": "a legacy memory"}}])
    for path in PUBLIC_PATHS + ["/archive/0", "/archive/witnesses/ZE"]:
        body = client.get(path, follow_redirects=True).get_data(as_text=True)
        assert "Zebulon" not in body, path
        assert "legacy memory" not in body, path


def test_malformed_case_file_block_is_treated_as_unpublished(seeded):
    client, write = seeded
    write([{"Case File": "not-a-dict",
            "Module I — Experience": {"Question 1": "a legacy memory"}}])
    r = client.get("/archive/witnesses")
    assert r.status_code == 200
    assert "legacy memory" not in r.get_data(as_text=True)


def test_published_record_missing_its_code_is_not_addressable(seeded):
    # A hand-edited record marked published but never assigned a code has
    # no public handle: there is no code URL that can reach it.
    # (NOTE: rendering the *list* with such a record raises BuildError in
    # archive.html — reported to the orchestrator, not asserted here.)
    client, write = seeded
    write([{"Case File": {"Name": SENTINEL, "Published": True},
            "Module I — Experience": {"Question 1": "a memory of family"}}])
    for path in ["/archive/witnesses/ZE", "/archive/witnesses/None", "/archive/0"]:
        r = client.get(path)
        assert r.status_code == 404, path
        assert "Zebulon" not in r.get_data(as_text=True), path


# ----------------------------------------------------------
# The investigator gate.
# ----------------------------------------------------------

def test_investigator_surface_is_disabled_not_open_when_unconfigured(client):
    _file(client, SENTINEL, published=False, answer="my private confession")
    for path in ["/investigator", "/investigator/case/0"]:
        r = client.get(path)
        assert r.status_code == 404, path
        body = r.get_data(as_text=True)
        assert "Zebulon" not in body, path
        assert "private confession" not in body, path


def test_investigator_surface_is_disabled_when_password_is_blank(client, monkeypatch):
    monkeypatch.setenv("NESCIENCE_INVESTIGATOR_PASSWORD", "")
    assert client.get("/investigator").status_code == 404
    # An empty submitted password must not satisfy an empty configured one.
    assert testutil.login(client, "").status_code == 404


def test_locked_investigator_pages_leak_no_record_data(gated):
    _file(gated, SENTINEL, published=False, answer="my private confession")
    for path in ["/investigator", "/investigator/case/0"]:
        r = gated.get(path)
        assert r.status_code == 401, path
        body = r.get_data(as_text=True)
        assert "Zebulon" not in body, path
        assert "private confession" not in body, path
        assert "ZE" not in body, path


def test_wrong_password_leaks_neither_records_nor_the_password(gated):
    _file(gated, SENTINEL, published=False, answer="my private confession")
    r = testutil.login(gated, "wrong")
    body = r.get_data(as_text=True)
    assert r.status_code == 401
    assert "Zebulon" not in body
    assert "private confession" not in body
    assert "letmein" not in body


def test_forged_session_cookie_does_not_authenticate(gated):
    _file(gated, SENTINEL, published=False)
    for forged in ["investigator=1",
                   "eyJpbnZlc3RpZ2F0b3IiOnRydWV9.fake.signature"]:
        gated.set_cookie("session", forged)
        assert gated.get("/investigator").status_code == 401


def test_session_signed_with_another_key_is_rejected(gated):
    from flask.sessions import TaggedJSONSerializer
    from itsdangerous import URLSafeTimedSerializer

    forger = URLSafeTimedSerializer(
        "not-the-real-secret-key",
        salt="cookie-session",
        serializer=TaggedJSONSerializer(),
        signer_kwargs={"key_derivation": "hmac", "digest_method": hashlib.sha1},
    )
    gated.set_cookie("session", forger.dumps({"investigator": True}))
    assert gated.get("/investigator").status_code == 401


def test_a_live_session_does_not_survive_disabling_the_surface(gated, monkeypatch):
    testutil.login(gated, "letmein")
    assert gated.get("/investigator").status_code == 200
    monkeypatch.delenv("NESCIENCE_INVESTIGATOR_PASSWORD", raising=False)
    assert gated.get("/investigator").status_code == 404


def test_logout_revokes_access(gated):
    _file(gated, SENTINEL, published=False)
    testutil.login(gated, "letmein")
    assert gated.get("/investigator").status_code == 200
    testutil.logout(gated)
    r = gated.get("/investigator")
    assert r.status_code == 401
    assert "Zebulon" not in r.get_data(as_text=True)


# ----------------------------------------------------------
# Code assignment — two participants must never share a code, whatever
# they type into the name field.
# ----------------------------------------------------------

def test_no_two_records_ever_share_a_code(client):
    hostile_names = [
        "Alex", "Alan", "Al", "A", "", "   ", "123", "_bob", "Bo",
        "ßeta", "Ünal", "Ulf", "élan", "Elan", "Zoe", "Zoë",
        "7-eleven", "Elena", "  alex  ", "ALEX", "<script>x</script>",
    ]
    codes = [
        _file(client, name, published=bool(i % 2)).get_json()["code"]
        for i, name in enumerate(hostile_names)
    ]
    assert len(codes) == len(set(codes)), codes


def test_collision_numbering_counts_unpublished_records_too(client):
    # An unpublished record still consumes a code, so numbering cannot be
    # used to detect how many records are hidden vs. published.
    assert _file(client, "Alex", True).get_json()["code"] == "AL"
    assert _file(client, "Alan", False).get_json()["code"] == "AL1"
    assert _file(client, "Al", True).get_json()["code"] == "AL2"


def test_unicode_names_yield_short_uppercase_codes(client):
    for name in ["Ünal", "élan", "Zoë", "Ωmega", "日本語"]:
        code = _file(client, name, published=True).get_json()["code"]
        assert code == code.upper()
        assert 2 <= len(code) <= 3   # two letters, plus a collision digit


def test_blank_name_falls_back_to_a_code_and_renders_as_a_code(client):
    assert _file(client, "", published=True).get_json()["code"] == "XX"
    assert client.get("/archive/witnesses/XX").status_code == 200
    assert _file(client, "   ", published=True).get_json()["code"] == "XX1"


def test_name_never_reaches_the_public_participant_information_block(client):
    _file(client, SENTINEL, published=True)
    record = database.load_interviews()[0]
    assert identity.get_name(record) == SENTINEL            # private
    assert "Zebulon" not in json.dumps(record["Participant Information"])
    assert "Zebulon" not in json.dumps(record["Module I — Experience"])
