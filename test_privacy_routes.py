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
