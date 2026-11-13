# The concept graph is an ordinary importable module (it used to be
# knowledge.graph.py, which needed an importlib workaround), and the
# pre-web CLI prototype is gone.
import importlib
import os

import pytest

import atlas

HERE = os.path.dirname(os.path.abspath(__file__))


def test_knowledge_graph_is_a_normal_module_shared_with_atlas():
    kg = importlib.import_module("knowledge_graph")
    assert atlas.concepts is kg.concepts
    assert "Memory" in atlas.concepts


def test_atlas_no_longer_uses_importlib():
    assert "importlib" not in open(os.path.join(HERE, "atlas.py")).read()


@pytest.mark.parametrize("name", ["main.py", "interview.py", "knowledge.graph.py"])
def test_retired_files_are_gone(name):
    assert not os.path.exists(os.path.join(HERE, name))
