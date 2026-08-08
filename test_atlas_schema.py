# ==========================================================
# NESCIENCE — Atlas schema tests (NESC-03)
#
# Guards the concept data-model expansion: the atlas must still
# load, the matcher's contract (interview_themes on every concept)
# must hold, and 001 MEMORY must be fully authored against the new
# Case File / Evidence Room schema.
# ==========================================================

import atlas
from matcher import match_interview


TIERS = ("what_we_know", "evidence_suggests", "disagreement", "unknown")

OPEN_Q_LENSES = (
    "question",
    "what_science_knows",
    "what_evidence_suggests",
    "where_evidence_disagrees",
    "what_remains_unknown",
)


def test_atlas_loads():
    assert atlas.concepts
    assert "Memory" in atlas.concepts


def test_matcher_still_imports_and_runs():
    # A tiny interview touching Memory's themes should return results.
    interview = {
        "Life": {"q1": "My childhood and family shaped my sense of loss."}
    }
    results = match_interview(interview)
    assert isinstance(results, list)
    assert any(r["concept"] == "Memory" for r in results)


def test_every_concept_has_interview_themes():
    for name, concept in atlas.concepts.items():
        assert "interview_themes" in concept, f"{name} missing interview_themes"
        assert isinstance(concept["interview_themes"], list)


def test_is_defined_contract():
    assert atlas.is_defined("Memory") is True
    # A known template stub remains "mapped-but-UNKNOWN".
    assert atlas.is_defined("Narrative") is False


def test_existing_keys_preserved_on_memory():
    memory = atlas.concepts["Memory"]
    for key in (
        "definition",
        "narrative_role",
        "paradox",
        "brain_regions",
        "landmark_researchers",
        "connects_to",
        "real_world_examples",
        "questions",
        "unresolved",
        "interview_themes",
        "evidence",
    ):
        assert key in memory, f"Memory lost existing key {key}"


def test_memory_new_narrative_fields():
    memory = atlas.concepts["Memory"]
    for key in ("investigators_note", "primary_question", "why_it_matters"):
        assert memory.get(key, "").strip(), f"Memory.{key} is empty"


def test_memory_neural_systems():
    systems = atlas.concepts["Memory"]["neural_systems"]
    assert systems
    for entry in systems:
        assert entry["system"].strip()
        assert entry["role"].strip()


def test_memory_evidence_room_four_tiers_populated():
    room = atlas.concepts["Memory"]["evidence_room"]
    assert set(room.keys()) == set(TIERS)
    for tier in TIERS:
        assert room[tier], f"evidence_room.{tier} is empty"
        for entry in room[tier]:
            assert entry["claim"].strip()
            assert entry["citation"].strip()


def test_memory_open_questions_structured():
    questions = atlas.concepts["Memory"]["open_questions"]
    assert questions
    for q in questions:
        for lens in OPEN_Q_LENSES:
            assert q.get(lens, "").strip(), f"open question missing {lens}"


def test_memory_connections_and_next_case():
    memory = atlas.concepts["Memory"]
    assert memory["connected_files"]
    assert memory["next_case"] in atlas.concepts


def test_memory_citations_are_real_and_referenced():
    memory = atlas.concepts["Memory"]
    citations = memory["citations"]
    assert citations
    keys = {c["key"] for c in citations}
    # The four verified references the brief requires.
    for required in (
        "scoville_milner_1957",
        "loftus_palmer_1974",
        "loftus_pickrell_1995",
        "nader_2000",
    ):
        assert required in keys, f"missing required citation {required}"
    for c in citations:
        for field in ("key", "author", "year", "title", "source"):
            assert str(c.get(field, "")).strip(), f"citation missing {field}"
    # Every citation referenced in the evidence room must resolve.
    room = memory["evidence_room"]
    for tier in TIERS:
        for entry in room[tier]:
            assert entry["citation"] in keys
