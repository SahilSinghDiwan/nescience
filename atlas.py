# ==========================================================
# NESCIENCE — Atlas loader
#
# knowledge.graph.py has a dot in its filename, so it cannot
# be imported with a normal `import` statement. This module
# loads it by file path and re-exposes the `concepts` dict so
# the rest of the project can treat the knowledge graph as an
# ordinary importable module: `from atlas import concepts`.
# ==========================================================

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_GRAPH_PATH = os.path.join(_HERE, "knowledge.graph.py")

_spec = importlib.util.spec_from_file_location("knowledge_graph", _GRAPH_PATH)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

# The full concept dictionary, exactly as authored in knowledge.graph.py
concepts = _module.concepts

# Re-export the browsing helpers too, in case they are useful elsewhere.
show_concept = _module.show_concept
get_connections = _module.get_connections
explore = _module.explore


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
