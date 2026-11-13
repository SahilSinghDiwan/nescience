# ==========================================================
# NESCIENCE — startup configuration
#
# With two gunicorn workers, a per-process random secret key makes
# investigator logins fail at random. The app must refuse to start in
# that configuration rather than run it.
# ==========================================================

import pytest

import app as flaskapp


def test_refuses_to_start_with_password_but_no_secret_key():
    with pytest.raises(RuntimeError, match="NESCIENCE_SECRET_KEY"):
        flaskapp.resolve_secret_key({"NESCIENCE_INVESTIGATOR_PASSWORD": "x"})


def test_dev_mode_allows_a_random_key_with_a_password():
    key = flaskapp.resolve_secret_key(
        {"NESCIENCE_INVESTIGATOR_PASSWORD": "x", "NESCIENCE_DEV": "1"}
    )
    assert key and len(key) >= 32


def test_configured_key_is_used_as_is():
    env = {"NESCIENCE_INVESTIGATOR_PASSWORD": "x", "NESCIENCE_SECRET_KEY": "k" * 40}
    assert flaskapp.resolve_secret_key(env) == "k" * 40


def test_public_only_deployment_needs_no_key():
    assert flaskapp.resolve_secret_key({})
