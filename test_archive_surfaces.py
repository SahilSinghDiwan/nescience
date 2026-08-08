# ==========================================================
# NESCIENCE — Evidence Room & Open Questions surfaces (NESC-09 / 10)
# ==========================================================

import app as flaskapp


def _html(path):
    r = flaskapp.app.test_client().get(path)
    assert r.status_code == 200, f"{path} -> {r.status_code}"
    return r.get_data(as_text=True)


def test_evidence_room_shows_four_tiers_with_real_citations():
    html = _html("/archive/evidence-room")
    for tier in ["What we know", "What the evidence suggests",
                 "What researchers disagree about"]:
        assert tier in html
    assert "What we don&#39;t know" in html or "What we don't know" in html
    assert "Scoville" in html and "Nader" in html   # real reference cards
    assert "Reference missing" not in html          # every citation resolves


def test_open_questions_use_the_five_part_structure():
    html = _html("/archive/open-questions")
    for part in ["What science knows", "What the evidence suggests",
                 "Where the evidence disagrees", "What remains unknown"]:
        assert part in html
    assert "Case 001" in html  # linked to the Memory case file


def test_hub_wires_the_two_surfaces_live():
    hub = _html("/archive")
    assert "/archive/evidence-room" in hub
    assert "/archive/open-questions" in hub


def test_retired_placeholder_slugs_are_gone():
    c = flaskapp.app.test_client()
    # these two moved from placeholder to real routes
    assert c.get("/archive/pending/evidence-room").status_code == 404
    assert c.get("/archive/pending/open-questions").status_code == 404
    # connections / notes are still honest placeholders
    assert c.get("/archive/pending/connections").status_code == 200
    assert c.get("/archive/pending/notes").status_code == 200
