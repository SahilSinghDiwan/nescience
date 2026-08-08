# ==========================================================
# NESCIENCE — bibliography / citation tests (NESC-04)
#
# Guards the promise that every displayed claim traces to a real,
# resolvable reference — no invented or dangling citations.
# ==========================================================

import bibliography


def test_seed_references_are_on_file():
    reg = bibliography.registry()
    for key in (
        "scoville_milner_1957",
        "loftus_palmer_1974",
        "loftus_pickrell_1995",
        "nader_2000",
    ):
        assert key in reg, f"missing seed citation {key}"
        cit = reg[key]
        assert cit["author"] and cit["year"] and cit["title"] and cit["source"]


def test_every_referenced_citation_resolves():
    # The core NESC-04 guarantee: no Evidence Room / Open Question may point at
    # a citation key that has no real reference behind it.
    assert bibliography.unresolved_citation_keys() == set()


def test_index_for_memory_has_its_citations():
    idx = bibliography.index_for("Memory")
    assert "scoville_milner_1957" in idx
    assert idx["scoville_milner_1957"]["year"] == 1957


def test_format_reference_reads_like_a_citation():
    ref = bibliography.format_reference(bibliography.get("scoville_milner_1957"))
    assert ref.startswith("Scoville")
    assert "(1957)" in ref
    assert ref.endswith(".")


def test_unknown_key_returns_none():
    assert bibliography.get("does_not_exist") is None
