# ==========================================================
# NESCIENCE — Evidence matcher
#
# Bridges a participant's interview (raw human testimony) to the
# concept atlas (knowledge.graph.py). It reads the free-text answers,
# looks for the signals each concept declares in `interview_themes`
# (plus supporting vocabulary), and returns the concepts the testimony
# appears to touch — the "leads" an investigator would follow next.
#
# This is deliberately transparent, not a black box: every match comes
# back with the exact words in the testimony that triggered it.
# ==========================================================

import re

from atlas import concepts, is_defined


def _normalise(text):
    """Lowercase and collapse hyphens/underscores to spaces so that
    'Self-image' in the graph can match 'self image' in an answer."""
    text = text.lower()
    text = re.sub(r"[-_/]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def _signals_for(concept_name):
    """Weighted signal words for a concept.

    interview_themes are the intended bridge, so they score highest;
    the concept's name and its neighbouring vocabulary are softer hints.
    Returns a list of (phrase, weight) with normalised phrases."""
    concept = concepts[concept_name]
    signals = {}

    def add(phrase, weight):
        phrase = _normalise(str(phrase)).strip()
        if len(phrase) < 3:
            return
        # keep the strongest weight if a phrase appears in several fields
        signals[phrase] = max(signals.get(phrase, 0), weight)

    add(concept_name, 3)
    for theme in concept.get("interview_themes", []):
        add(theme, 3)
    for example in concept.get("real_world_examples", []):
        add(example, 2)
    for other in concept.get("connects_to", []):
        add(other, 1)
    for region in concept.get("brain_regions", []):
        add(region, 1)

    return list(signals.items())


# Blocks that are not testimony and must never enter matching: demographics
# (so a country named 'Turkey' can't be mistaken for content) and the private
# Case File block (real name, code, timestamp — never scan or surface these).
_NON_TESTIMONY = ("Participant Information", "Case File")


def _collect_answers(interview):
    """Flatten every free-text answer in an interview into one blob,
    skipping the non-testimony blocks in `_NON_TESTIMONY`."""
    parts = []
    for module, responses in interview.items():
        if module in _NON_TESTIMONY:
            continue
        if isinstance(responses, dict):
            parts.extend(str(v) for v in responses.values())
        else:
            parts.append(str(responses))
    return _normalise(" \n ".join(parts))


def match_interview(interview, limit=4):
    """Return the concepts a given interview most plausibly touches.

    Each result:
        {
          "concept": <name>,
          "score": <float>,
          "evidence": [<matched phrase>, ...],   # what triggered it
          "unresolved": <the concept's open question>,
          "questions": [<open questions>, ...],
          "defined": <bool>,                     # researched vs. stub
        }
    Sorted strongest-first. Only concepts with at least one hit appear."""
    blob = _collect_answers(interview)
    if not blob.strip():
        return []

    results = []
    for name in concepts:
        score = 0.0
        evidence = []
        for phrase, weight in _signals_for(name):
            # whole-word / whole-phrase match against the normalised blob
            pattern = r"\b" + re.escape(phrase) + r"\b"
            if re.search(pattern, blob):
                score += weight
                evidence.append(phrase)

        if score <= 0:
            continue

        concept = concepts[name]
        results.append(
            {
                "concept": name,
                "score": score,
                "evidence": sorted(set(evidence)),
                "unresolved": concept.get("unresolved", ""),
                "questions": concept.get("questions", []),
                "defined": is_defined(name),
            }
        )

    # Prefer higher score, then researched concepts over bare stubs.
    results.sort(key=lambda r: (r["score"], r["defined"]), reverse=True)
    return results[:limit]
