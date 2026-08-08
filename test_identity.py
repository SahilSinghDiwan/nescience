# ==========================================================
# NESCIENCE — tests for the privacy / identity / consent model
#
# Code generation is the core logic, so it is driven test-first:
# the collision-numbering rules and the public projection's privacy
# guarantees are pinned down here before anything renders publicly.
# ==========================================================

import identity


# ----------------------------------------------------------
# Small helpers so the tests read like the interview records
# app.py actually produces (modules of answers + a Case File).
# ----------------------------------------------------------

def make_record(name, published, responses=None):
    """Build an interview record and stamp its private identity onto it,
    assigning a code from the records that already exist."""
    record = {
        "Participant Information": {"Age": "30"},
        "Module I — Experience": responses or {"Question 1": "a memory"},
        "Case File": {"Recorded": "2026-08-08 12:00"},
    }
    identity.apply_identity(record, name, published, _RECORDS)
    _RECORDS.append(record)
    return record


# Each test that uses make_record resets this shared list first.
_RECORDS = []


def reset():
    _RECORDS.clear()


# ----------------------------------------------------------
# code_from_name — the two-letter base code + fallbacks
# ----------------------------------------------------------

def test_code_from_name_basic():
    assert identity.code_from_name("Alex") == "AL"
    assert identity.code_from_name("Alan") == "AL"
    assert identity.code_from_name("bo") == "BO"


def test_code_from_name_short_is_padded():
    assert identity.code_from_name("A") == "AX"


def test_code_from_name_empty_or_missing_falls_back():
    assert identity.code_from_name("") == "XX"
    assert identity.code_from_name("   ") == "XX"
    assert identity.code_from_name(None) == "XX"


def test_code_from_name_skips_non_letters():
    assert identity.code_from_name("7-eleven") == "EL"
    assert identity.code_from_name("_bob") == "BO"
    assert identity.code_from_name("123") == "XX"


# ----------------------------------------------------------
# assign_code — collision numbering (the spec's worked example)
# ----------------------------------------------------------

def test_collision_numbering_alex_alan_al():
    reset()
    alex = make_record("Alex", True)
    alan = make_record("Alan", True)
    al = make_record("Al", True)

    assert identity.get_code(alex) == "AL"
    assert identity.get_code(alan) == "AL1"
    assert identity.get_code(al) == "AL2"


def test_distinct_names_do_not_collide():
    reset()
    bob = make_record("Bob", True)
    cat = make_record("Cat", True)
    assert identity.get_code(bob) == "BO"
    assert identity.get_code(cat) == "CA"


def test_assign_code_fills_smallest_unused_gap():
    reset()
    # Pre-seed with AL and AL2 already taken; AL1 is the smallest gap.
    records = [
        {"Case File": {"Name": "Alex", "Code": "AL", "Published": True}},
        {"Case File": {"Name": "Alan", "Code": "AL2", "Published": True}},
    ]
    assert identity.assign_code("Alfred", records) == "AL1"


# ----------------------------------------------------------
# public_projection — the privacy guarantee
# ----------------------------------------------------------

def test_public_projection_only_published():
    reset()
    make_record("Alex", True)
    make_record("Blair", False)
    make_record("Cara", True)

    public = identity.public_projection(_RECORDS)
    assert len(public) == 2
    assert {entry["code"] for entry in public} == {"AL", "CA"}


def test_public_projection_strips_names_and_private_fields():
    reset()
    make_record("Alex", True, responses={"Question 1": "the sea"})

    public = identity.public_projection(_RECORDS)
    entry = public[0]

    # code + responses only
    assert entry["code"] == "AL"
    assert entry["responses"]["Module I — Experience"]["Question 1"] == "the sea"

    # the real name / mapping / private block must be gone entirely
    blob = repr(entry)
    assert "Alex" not in blob
    assert "Case File" not in entry
    assert "Case File" not in entry.get("responses", {})
    assert "Name" not in blob


def test_public_projection_ignores_records_without_publication_flag():
    reset()
    # A legacy record with no Published field at all.
    legacy = {"Module I — Experience": {"Question 1": "old"}}
    _RECORDS.append(legacy)
    make_record("Alex", True)

    public = identity.public_projection(_RECORDS)
    assert len(public) == 1
    assert public[0]["code"] == "AL"


# ----------------------------------------------------------
# name_code_mapping — private accessor only
# ----------------------------------------------------------

def test_name_code_mapping_is_private_and_complete():
    reset()
    make_record("Alex", True)
    make_record("Alan", False)  # unpublished still has a name->code mapping

    mapping = identity.name_code_mapping(_RECORDS)
    assert mapping == {"Alex": "AL", "Alan": "AL1"}


# ----------------------------------------------------------
# Backward compatibility with pre-identity participants.json
# ----------------------------------------------------------

def test_legacy_record_is_unpublished_and_codeless():
    legacy = {"Module I — Experience": {"Question 1": "old"}}
    assert identity.is_published(legacy) is False
    assert identity.get_code(legacy) is None
    assert identity.get_name(legacy) is None


def test_ensure_code_backfills_lazily_for_display():
    legacy = {
        "Case File": {"Name": "Mira"},
        "Module I — Experience": {"Question 1": "old"},
    }
    code = identity.ensure_code(legacy, [])
    assert code == "MI"
    assert identity.get_code(legacy) == "MI"
