# Shared test setup. Runs before any test module imports `app`.
import os

# Tests run over plain http with the Flask test client; the Secure cookie
# flag (on outside dev mode) would stop the client sending the session back.
os.environ.setdefault("NESCIENCE_DEV", "1")

import pytest  # noqa: E402

import ratelimit  # noqa: E402


@pytest.fixture(autouse=True)
def _fresh_rate_limits():
    """Rate-limit counters are process-wide; keep tests independent."""
    ratelimit.reset_all()
    yield
    ratelimit.reset_all()


@pytest.fixture(autouse=True)
def _roomy_interview_limit(monkeypatch):
    """Tests file many interviews from one 'address'; the production limit
    is exercised explicitly in test_hardening.py."""
    import app as flaskapp
    monkeypatch.setattr(flaskapp, "interview_limiter",
                        ratelimit.RateLimiter(10_000, 60))
