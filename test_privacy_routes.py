# ==========================================================
# NESCIENCE — route-level privacy & consent tests
#
# The identity model is unit-tested in test_identity.py; this file
# guards the *routes* that must honour it (NESC-05 consent capture,
# NESC-11 public code-only surface, NESC-02 gated investigator view).
# Every test drives the real Flask app through its test client against
# a throwaway data file, so no test ever touches participants.json.
# ==========================================================

import json

import pytest

import app as flaskapp
import database
import identity


@pytest.fixture
def client(tmp_path, monkeypatch):
    """A test client whose archive is an empty temp file."""
    data = tmp_path / "participants.json"
    data.write_text("[]")
    monkeypatch.setattr(database, "FILE_NAME", str(data))
    return flaskapp.app.test_client()


def _file(client, name, published, answer="A childhood memory of family and loss."):
    return client.post("/api/interview", json={
        "name": name,
        "published": published,
        "Participant Information": {"Age": "31", "Country": "India"},
        "Module I — Experience": {"Question 1": answer},
    })


# ---- NESC-05: consent capture --------------------------------------------

def test_interview_page_has_name_field_and_publication_choice(client):
    html = client.get("/interview").get_data(as_text=True)
    assert "data-name" in html
    assert 'id="submit-publish"' in html
    assert 'id="submit-private"' in html


def test_name_is_private_and_code_is_returned(client):
    data = _file(client, "Alex", published=True).get_json()
    assert data["code"] == "AL"
    assert data["published"] is True
    # the real name must not travel back to the browser
    assert "Alex" not in json.dumps(data)

    record = database.load_interviews()[0]
    assert identity.get_name(record) == "Alex"          # stored privately
    assert identity.get_code(record) == "AL"
    assert identity.is_published(record) is True
    # never in the public Participant Information block
    assert "Alex" not in json.dumps(record["Participant Information"])


def test_publication_choice_is_recorded(client):
    _file(client, "Sam", published=False)
    record = database.load_interviews()[0]
    assert identity.is_published(record) is False


def test_codes_get_collision_numbers_through_the_route(client):
    assert _file(client, "Alex", True).get_json()["code"] == "AL"
    assert _file(client, "Alan", False).get_json()["code"] == "AL1"
    assert _file(client, "Al", True).get_json()["code"] == "AL2"


def test_private_name_never_reaches_the_matcher(client):
    # The name "Memory" is stored privately in the Case File; the answer text
    # never contains the word "memory" (only "remember"). So if "memory" shows
    # up as matcher evidence, the private name leaked in — it must not.
    _file(client, "Memory", published=True, answer="I remember my family.")
    record = database.load_interviews()[0]
    from matcher import match_interview
    evidence = [e.lower() for lead in match_interview(record) for e in lead["evidence"]]
    assert "family" in evidence          # legitimate hit from the answer
    assert "memory" not in evidence      # would appear only if the name were scanned


# ---- NESC-11: public witness accounts (code-only, published-only) --------

def test_unpublished_testimony_absent_from_public_list(client):
    _file(client, "Bea", published=False, answer="childhood memory of family")
    html = client.get("/archive/witnesses").get_data(as_text=True)
    assert "None published" in html or "No testimony has been published" in html
    assert "Memory" not in html  # its lead would show only if it were published


def test_published_testimony_shows_by_code_only(client):
    code = _file(client, "Bea", published=True).get_json()["code"]
    html = client.get("/archive/witnesses").get_data(as_text=True)
    assert code in html            # identified by code
    assert "Bea" not in html       # never by name
    assert "Memory" in html        # its lead appears


def test_witness_detail_is_code_only_and_nameless(client):
    code = _file(client, "Bea", published=True).get_json()["code"]
    r = client.get(f"/archive/witnesses/{code}")
    assert r.status_code == 200
    body = r.get_data(as_text=True)
    assert code in body
    assert "Bea" not in body
    # an unknown / unpublished code is not found
    assert client.get("/archive/witnesses/ZZ").status_code == 404


def test_index_case_route_no_longer_leaks_full_records(client):
    # unpublished record: bare index must 404 (no public full transcript)
    _file(client, "Cid", published=False)
    assert client.get("/archive/0").status_code == 404
    # published record: index redirects to the code-based witness view
    code = _file(client, "Dot", published=True).get_json()["code"]
    r = client.get("/archive/1", follow_redirects=False)
    assert r.status_code in (301, 302)
    assert f"/archive/witnesses/{code}" in r.headers["Location"]


def test_name_appears_on_no_public_route(client):
    _file(client, "Zelda", published=True)
    for path in ["/archive", "/archive/witnesses", "/archive/witnesses/ZE"]:
        assert "Zelda" not in client.get(path).get_data(as_text=True)


# ---- NESC-02: gated investigator surface ---------------------------------

@pytest.fixture
def gated_client(tmp_path, monkeypatch):
    data = tmp_path / "participants.json"
    data.write_text("[]")
    monkeypatch.setattr(database, "FILE_NAME", str(data))
    monkeypatch.setenv("NESCIENCE_INVESTIGATOR_PASSWORD", "letmein")
    return flaskapp.app.test_client()


def test_investigator_disabled_when_no_password(client, monkeypatch):
    monkeypatch.delenv("NESCIENCE_INVESTIGATOR_PASSWORD", raising=False)
    assert client.get("/investigator").status_code == 404
    assert client.get("/investigator/case/0").status_code == 404
    assert client.post("/investigator/login", data={"password": "x"}).status_code == 404


def test_investigator_requires_password(gated_client):
    r = gated_client.get("/investigator")
    assert r.status_code == 401
    assert "INVESTIGATOR" in r.get_data(as_text=True)
    assert gated_client.post("/investigator/login", data={"password": "wrong"}).status_code == 401


def test_investigator_login_grants_full_access(gated_client):
    gated_client.post("/api/interview", json={
        "name": "Alex", "published": False,
        "Module I — Experience": {"Question 1": "secret private testimony"},
    })
    # gated before login
    assert gated_client.get("/investigator/case/0").status_code == 401
    # log in
    r = gated_client.post("/investigator/login", data={"password": "letmein"})
    assert r.status_code in (301, 302)
    ledger = gated_client.get("/investigator").get_data(as_text=True)
    assert "Alex" in ledger  # real name visible only to the investigator
    # full case detail incl unpublished testimony + name
    detail = gated_client.get("/investigator/case/0").get_data(as_text=True)
    assert "Alex" in detail and "secret private testimony" in detail
