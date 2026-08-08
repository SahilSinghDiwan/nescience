# Concept schema (`knowledge.graph.py`)

This document defines the shape of every entry in the `concepts` dict in
`knowledge.graph.py`. It was expanded in **NESC-03** to support the deep
**Case File** and **Evidence Room** surfaces. The expansion is *additive*:
the original v1.0 keys are unchanged, and `atlas.py` / `matcher.py` still read
them exactly as before. Author future concepts against this contract, using
**001 MEMORY** as the reference implementation.

## Golden rules

- **Never remove or rename an existing key.** `atlas.is_defined()` keys off a
  non-empty `definition`; `matcher.py` reads `interview_themes`,
  `real_world_examples`, `connects_to`, and `brain_regions`.
- **Stubs stay stubs.** A concept with an empty `definition` is
  "mapped-but-UNKNOWN" and must not be presented as finished evidence. Leave
  the new fields empty (`""` / `[]` / `{}`) on stubs.
- **Citations must be real.** Every entry in `citations` must be a genuine,
  verifiable reference. Do not invent studies. `evidence_room` and
  `open_questions` claims should trace back to a real citation key.

## Core keys (v1.0 — unchanged, required on every concept)

| Key | Type | Notes |
|-----|------|-------|
| `definition` | `str` | Non-empty marks the concept as "defined" (`is_defined`). |
| `narrative_role` | `str` | How the concept functions in the exhibit's story. |
| `paradox` | `str` | The one-line tension at the heart of the concept. |
| `brain_regions` | `list[str]` | Plain region names. Read by `matcher.py`. **Keep this** even when `neural_systems` is authored. |
| `key_experiments` | `list[str]` | Short experiment labels. Read by `show_concept`. |
| `landmark_researchers` | `list[str]` | Names. |
| `connects_to` | `list[str]` | Other concept keys. Read by `matcher.py` and `get_connections`. |
| `real_world_examples` | `list[str]` | Read by `matcher.py`. |
| `questions` | `list[str]` | Surfaced by `matcher.py` on a match. |
| `unresolved` | `str` | The concept's headline open question. |
| `interview_themes` | `list[str]` | **Required on every concept** — the bridge `matcher.py` uses to link testimony to concepts. |
| `evidence` | `list[dict]` | Legacy evidence list (`type`, `title`, optional `year`). Kept for existing templates; the richer structure is `evidence_room`. |

> Historical note: some early concepts carry `evidence` and others carry
> `key_experiments`. Author **both** on new concepts so every template renders.

## Expanded keys (NESC-03 — additive)

### Case File narrative

| Key | Type | Notes |
|-----|------|-------|
| `investigators_note` | `str` | First-person framing an investigator would clip to the file. |
| `primary_question` | `str` | The single driving question of the case. |
| `why_it_matters` | `str` | Why this concept matters beyond the lab. |

### Neural systems

`neural_systems` — `list[dict]`, a richer companion to `brain_regions` (keep
both). Each entry:

```python
{"system": "Hippocampus & medial temporal lobe", "role": "…what it does…"}
```

### Evidence Room — four epistemic tiers

`evidence_room` — `dict` with exactly these four keys, each a `list[dict]`:

| Tier | Meaning |
|------|---------|
| `what_we_know` | Robust, well-replicated findings. |
| `evidence_suggests` | Supported but interpretive / not yet settled. |
| `disagreement` | Where credible researchers actively disagree. |
| `unknown` | Honest gaps — open even to current science. |

Each entry:

```python
{"claim": "One-paragraph summary of the finding or gap.",
 "citation": "scoville_milner_1957"}   # a key in this concept's `citations`
```

### Structured open questions

`open_questions` — `list[dict]`, each question examined through the same four
lenses used by the Evidence Room (NESC-10):

```python
{
  "question": "Is forgetting a failure of storage or of retrieval?",
  "what_science_knows": "…",
  "what_evidence_suggests": "…",
  "where_evidence_disagrees": "…",
  "what_remains_unknown": "…",
}
```

### Connections & sequencing

| Key | Type | Notes |
|-----|------|-------|
| `connected_files` | `list[str]` | Concept keys for the corkboard graph (NESC-12). May mirror `connects_to`; kept separate so they can diverge. |
| `next_case` | `str` | Concept key of the next case in the numbered sequence. |

### Citations

`citations` — `list[dict]` of **real** references. Keys are referenced by
`evidence_room` and `open_questions`, and mirror `docs/bibliography.md`
(NESC-04):

```python
{
  "key": "scoville_milner_1957",
  "author": "Scoville, W. B., & Milner, B.",
  "year": 1957,
  "title": "Loss of recent memory after bilateral hippocampal lesions",
  "source": "Journal of Neurology, Neurosurgery & Psychiatry, 20(1), 11–21",
}
```

## Reference implementation

**001 MEMORY** in `knowledge.graph.py` is fully authored against this schema.
Its Evidence Room draws on four verified sources:

- Scoville & Milner (1957) — patient H.M. → `what_we_know`
- Loftus & Palmer (1974) — misinformation effect → `evidence_suggests`
- Loftus & Pickrell (1995) — implanted false memories → `disagreement`
- Nader, Schafe & LeDoux (2000) — reconsolidation → `disagreement` / `unknown`
