# NESC-03 — Concept data-model expansion + author Memory fully

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P0 (blocks NESC-04, 08, 09, 10, 12)
- **Brief refs:** §7, §9, §11
- **Depends on:** —

## Summary
Expand each concept's schema in `knowledge_graph.py` to support the deep **Case File** and **Evidence Room** structures, and fully author the first case (**001 MEMORY**) as the reference implementation.

## Why
The current concept dict has definition/regions/researchers/questions/unresolved. The brief needs richer, epistemically-structured content per concept (§7 Case File anatomy; §11 four tiers; §7/§9 connections). Memory is the first complete case; others follow the same shape.

## Scope / acceptance criteria
- [ ] Extend the concept schema (additive; keep existing keys) with fields to support:
  - `investigators_note`, `primary_question`, `why_it_matters`
  - `neural_systems` (can reuse/rename `brain_regions`)
  - `evidence_room` — entries grouped into the **four tiers**: `what_we_know`, `evidence_suggests`, `disagreement`, `unknown` (see NESC-09). Each entry references a citation key (see NESC-04).
  - `open_questions` in the structured Open-Questions format (see NESC-10)
  - `connected_files` (reuse `connects_to`) and a `next_case` pointer
  - `citations` list (keys into `docs/bibliography.md`, see NESC-04)
- [ ] `atlas.py` continues to work; `is_defined()` still keys off a non-empty definition; stubs remain "mapped-but-UNKNOWN".
- [ ] **001 MEMORY** fully authored against the new schema, with real cited evidence (H.M., Loftus, reconsolidation — verify per NESC-04).
- [ ] Document the schema (a short comment block or `docs/concept-schema.md`) so future concepts follow it.

## Out of scope
- Rendering the Case File / Evidence Room / Open Questions (NESC-08/09/10).
- Authoring all remaining concepts — seed structure + Memory only; others are follow-up content tickets.

## Notes
- Keep `matcher.py` working: `interview_themes` must remain on every concept.

## Status note (2026-08-22)
Schema and the reference case (001 Memory) are done, and the content tail is
mostly authored: 11 of 15 concepts are complete, with 53 verified citations.

Still stubs, rendering honestly as mapped-but-UNKNOWN: **Habit, Motivation,
Social Cognition, Narrative.** Two of those are pinned as stubs by existing
tests (`test_is_defined_contract` names Narrative, `test_stub_concept_reads_unknown`
fetches /atlas/Habit), so authoring either means repointing those tests at a
concept that is still unwritten.

## Status note (2026-09-17)
Content tail closed out: **Habit** (009), **Motivation** (013) and **Social
Cognition** (012) are now fully authored against the schema — 14 of 15
concepts, 75 verified citations (22 new, each confirmed against Crossref or
the publisher before it was written in). Each was drafted by a separate agent
and spliced in as its own commit.

`test_stub_concept_reads_unknown` moved from /atlas/Habit to /atlas/Narrative.
The case sequence now closes a full loop: Language -> Habit -> Motivation ->
Social Cognition -> Memory.

**Narrative is deliberately left a stub.** Two tests pin the
"mapped-but-UNKNOWN" contract to a real unauthored concept, so at least one
must stay unwritten, and §3 of the brief calls narrative a *mechanism, not the
whole subject* — leaving the exhibit's own central mechanism marked UNKNOWN is
consistent with what it argues. Authoring it is a content decision for the
human: it needs either a new deliberate stub concept to carry the test
contract, or that contract dropped.
