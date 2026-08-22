# NESC-03 — Concept data-model expansion + author Memory fully

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P0 (blocks NESC-04, 08, 09, 10, 12)
- **Brief refs:** §7, §9, §11
- **Depends on:** —

## Summary
Expand each concept's schema in `knowledge.graph.py` to support the deep **Case File** and **Evidence Room** structures, and fully author the first case (**001 MEMORY**) as the reference implementation.

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
