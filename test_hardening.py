# ==========================================================
# NESCIENCE — request hardening: CSRF, rate limits, size cap,
# logout method, cookie flags, non-ASCII passwords.
# ==========================================================

import pytest

import app as flaskapp
import database
import ratelimit
import testutil


@pytest.fixture
def gated(tmp_path, monkeypatch):
    data = tmp_path / "participants.json"
    data.write_text("[]")
    monkeypatch.setattr(database, "FILE_NAME", str(data))
    monkeypatch.setenv("NESCIENCE_INVESTIGATOR_PASSWORD", "letmein")
    return flaskapp.app.test_client()


def _submit(client):
    return client.post("/api/interview", json={
        "name": "A", "published": False,
        "Module I — Experience": {"Question 1": "x"},
    })


# ---- CSRF ----------------------------------------------------------------

def test_login_form_carries_a_csrf_token(gated):
    assert testutil.csrf_token(gated)


def test_login_without_token_is_rejected_even_with_right_password(gated):
    r = gated.post("/investigator/login", data={"password": "letmein"})
    assert r.status_code == 400
    assert gated.get("/investigator").status_code == 401


def test_login_with_wrong_token_is_rejected(gated):
    testutil.csrf_token(gated)
    r = gated.post("/investigator/login",
                   data={"password": "letmein", "csrf_token": "forged"})
    assert r.status_code == 400


def test_logout_is_post_only_and_needs_a_token(gated):
    testutil.login(gated, "letmein")
    assert gated.get("/investigator/logout").status_code == 405
    assert gated.get("/investigator").status_code == 200  # still signed in
    assert gated.post("/investigator/logout").status_code == 400
    assert gated.get("/investigator").status_code == 200
    assert testutil.logout(gated).status_code in (301, 302)
    assert gated.get("/investigator").status_code == 401


def test_ledger_uses_a_logout_form_not_a_link(gated):
    testutil.login(gated, "letmein")
    page = gated.get("/investigator").get_data(as_text=True)
    assert 'action="/investigator/logout"' in page
    assert 'href="/investigator/logout"' not in page


# ---- non-ASCII password ---------------------------------------------------

def test_non_ascii_password_is_a_401_not_a_500(gated):
    assert testutil.login(gated, "pässwörd–日本").status_code == 401


def test_non_ascii_configured_password_works(gated, monkeypatch):
    monkeypatch.setenv("NESCIENCE_INVESTIGATOR_PASSWORD", "pässwörd–日本")
    assert testutil.login(gated, "pässwörd–日本").status_code in (301, 302)


# ---- rate limits ----------------------------------------------------------

def test_login_is_rate_limited(gated):
    codes = [testutil.login(gated, "wrong").status_code for _ in range(12)]
    assert codes[0] == 401
    assert 429 in codes
    # once limited, even the right password is refused
    assert testutil.login(gated, "letmein").status_code == 429


def test_interview_submission_is_rate_limited(gated, monkeypatch):
    monkeypatch.setattr(flaskapp, "interview_limiter", ratelimit.RateLimiter(3, 60))
    codes = [_submit(gated).status_code for _ in range(5)]
    assert codes[:3] == [200, 200, 200]
    assert codes[3:] == [429, 429]


def test_limiter_window_expires():
    lim = ratelimit.RateLimiter(2, 10)
    assert lim.allow("k", now=0) and lim.allow("k", now=1)
    assert not lim.allow("k", now=2)
    assert lim.allow("k", now=11)
    assert lim.allow("other", now=2)


# ---- size cap -------------------------------------------------------------

def test_oversized_submission_is_refused_with_json(gated):
    assert flaskapp.app.config["MAX_CONTENT_LENGTH"]
    big = "x" * (flaskapp.app.config["MAX_CONTENT_LENGTH"] + 1)
    r = gated.post("/api/interview", json={"name": big})
    assert r.status_code == 413
    assert r.get_json()["error"]
    assert database.load_interviews() == []


# ---- cookie flags ---------------------------------------------------------

def test_cookie_flags_are_secure_outside_dev():
    cfg = flaskapp.session_cookie_config({})
    assert cfg["SESSION_COOKIE_HTTPONLY"] is True
    assert cfg["SESSION_COOKIE_SAMESITE"] == "Lax"
    assert cfg["SESSION_COOKIE_SECURE"] is True


def test_cookie_secure_flag_dropped_only_in_dev():
    assert flaskapp.session_cookie_config({"NESCIENCE_DEV": "1"})["SESSION_COOKIE_SECURE"] is False


def test_session_cookie_is_httponly_samesite(gated):
    r = gated.get("/investigator")
    cookie = r.headers.get("Set-Cookie", "")
    assert "HttpOnly" in cookie and "SameSite=Lax" in cookie
