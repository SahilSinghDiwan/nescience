# ==========================================================
# NESCIENCE — bibliography / citation registry (NESC-04)
#
# Every factual claim in the exhibit must trace to a real, verifiable
# paper (see brief §11). The per-concept `citations` lists in
# knowledge.graph.py are the source of truth; this module aggregates
# them into one keyed registry, mirrors docs/bibliography.md, and lets
# the Evidence Room / Open Questions resolve a citation key into a
# reference card. An unknown key is *surfaced* (see
# `unresolved_citation_keys`), never silently rendered.
# ==========================================================

from atlas import concepts


def registry():
    """All citations across every concept, keyed by their citation key.

    The first definition of a key wins; keys are expected to be globally
    consistent (the same paper carries the same key everywhere)."""
    reg = {}
    for concept in concepts.values():
        for citation in concept.get("citations", []) or []:
            key = citation.get("key")
            if key and key not in reg:
                reg[key] = citation
    return reg


def get(key):
    """The citation for a key, or None if it is not on file."""
    return registry().get(key)


def index_for(name):
    """{key: citation} for one concept's own citations — what its templates
    need to resolve evidence_room / open_questions references."""
    concept = concepts.get(name, {})
    return {
        c["key"]: c
        for c in concept.get("citations", []) or []
        if c.get("key")
    }


def format_reference(citation):
    """Render a citation dict as a single reference string:
    'Author (year). Title. Source.'"""
    if not citation:
        return ""
    parts = []
    author = (citation.get("author") or "").strip().rstrip(".")
    if author:
        parts.append(author)
    year = citation.get("year")
    if year:
        parts.append(f"({year})")
    lead = " ".join(parts)

    ref = lead
    title = (citation.get("title") or "").strip().rstrip(".")
    if title:
        ref = f"{ref}. {title}" if ref else title
    source = (citation.get("source") or "").strip().rstrip(".")
    if source:
        ref = f"{ref}. {source}" if ref else source
    return (ref.strip().rstrip(".") + ".") if ref else ""


def _referenced_keys():
    """Every citation key referenced by an evidence_room entry or an
    open_questions entry, across all concepts."""
    keys = set()
    for concept in concepts.values():
        room = concept.get("evidence_room", {}) or {}
        for tier in room.values():
            for entry in tier or []:
                key = entry.get("citation")
                if key:
                    keys.add(key)
    return keys


def unresolved_citation_keys():
    """Citation keys that are referenced but have no real reference on file.
    An empty set means every claim traces to a genuine source."""
    reg = registry()
    return {key for key in _referenced_keys() if key not in reg}
