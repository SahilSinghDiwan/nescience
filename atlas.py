# ==========================================================
# NESCIENCE — Atlas loader
#
# Re-exposes the concept dictionary from knowledge_graph.py and adds
# the "defined vs. stub" helpers, so the rest of the project can
# write `from atlas import concepts`.
# ==========================================================

from knowledge_graph import concepts, show_concept, get_connections, explore  # noqa: F401


def is_defined(name):
    """A concept is 'defined' once it has an actual definition written.

    The knowledge graph ships with many template stubs (empty strings /
    empty lists). Those are part of the investigation's map but should not
    be presented as finished evidence."""
    concept = concepts.get(name)
    if not concept:
        return False
    return bool(concept.get("definition", "").strip())


def defined_concepts():
    """Names of concepts that have been researched so far."""
    return [name for name in concepts if is_defined(name)]


def stub_concepts():
    """Names of concepts that are mapped but not yet investigated."""
    return [name for name in concepts if not is_defined(name)]
