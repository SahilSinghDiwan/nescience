# ==========================================================
# NESCIENCE — minimal in-process rate limiter
#
# A sliding window per key (the client address). State lives in this
# process only: with N gunicorn workers the effective limit is up to N
# times the configured one, and it resets on restart. That is a deliberate
# trade for having no extra dependency or service; it blunts password
# guessing and bulk submission, it is not a substitute for a proxy limit.
# ==========================================================

import threading
import time
from collections import deque

_lock = threading.Lock()
_limiters = []


class RateLimiter:
    def __init__(self, limit, window_seconds):
        self.limit = limit
        self.window = window_seconds
        self._hits = {}
        with _lock:
            _limiters.append(self)

    def allow(self, key, now=None):
        """Record an attempt for `key`; False when it exceeds the limit."""
        now = time.monotonic() if now is None else now
        with _lock:
            hits = self._hits.setdefault(key, deque())
            while hits and hits[0] <= now - self.window:
                hits.popleft()
            if len(hits) >= self.limit:
                return False
            hits.append(now)
            # Keep memory bounded: drop idle keys when the table grows.
            if len(self._hits) > 10000:
                for k in [k for k, h in self._hits.items()
                          if not h or h[-1] <= now - self.window]:
                    del self._hits[k]
            return True

    def reset(self):
        with _lock:
            self._hits.clear()


def reset_all():
    for limiter in list(_limiters):
        limiter.reset()
