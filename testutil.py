"""Helpers shared by the route tests."""
import re

_TOKEN = re.compile(r'name="csrf_token"\s+value="([^"]+)"')


def csrf_token(client, path="/investigator"):
    """Fetch a page that carries a CSRF token and return it ('' if none)."""
    m = _TOKEN.search(client.get(path).get_data(as_text=True))
    return m.group(1) if m else ""


def login(client, password):
    """POST the investigator login form the way a browser would."""
    return client.post("/investigator/login", data={
        "password": password, "csrf_token": csrf_token(client),
    })


def logout(client):
    return client.post("/investigator/logout", data={
        "csrf_token": csrf_token(client),
    })
