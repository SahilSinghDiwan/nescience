# ==========================================================
# NESCIENCE — Case File view tests (NESC-08 + 09/10 rendering)
# ==========================================================

import app as flaskapp


def _html(path):
    return flaskapp.app.test_client().get(path).get_data(as_text=True)


def test_memory_case_file_renders_full_anatomy():
    html = _html("/atlas/Memory")
    for marker in [
        "Case File No. 001",
        "EXHIBIT 001/A",
        "Primary question",
        "Why it matters",
        "Neural systems",
        "Evidence Room",
        "What we know",
        "Open Questions",
        "What remains unknown",
        "Connected files",
        "Next case",
    ]:
        assert marker in html, f"missing case-file section: {marker}"


def test_evidence_room_shows_real_reference_cards():
    html = _html("/atlas/Memory")
    assert "Scoville" in html          # a real citation surfaced as a card
    assert "Reference missing" not in html  # no dangling citation keys


def test_stub_concept_reads_unknown():
    html = _html("/atlas/Habit")
    assert "UNKNOWN" in html
    assert "Evidence Room" not in html  # stubs present no finished evidence


def test_next_case_points_forward():
    html = _html("/atlas/Memory")
    assert "IDENTITY" in html  # Memory.next_case -> Identity
