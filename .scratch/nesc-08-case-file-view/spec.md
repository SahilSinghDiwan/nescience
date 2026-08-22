# NESC-08 — Case File view (deep concept)

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P1
- **Brief refs:** §7
- **Depends on:** NESC-03

## Summary
Turn a concept page into a **deep Case File** — a full investigation into one concept, starting with 001 MEMORY.

## Why
§7: "A Case File = a deep investigation into one concept." Defines the anatomy each file contains.

## Scope / acceptance criteria
- [ ] Case File route renders, in order: **investigator's note · primary question · why it matters · collected evidence · neural systems · evidence room · open questions · connected files · next case.**
- [ ] Content is driven by the expanded schema (NESC-03); 001 MEMORY is the reference.
- [ ] Case/exhibit numbering shown (e.g. `CASE 001 — MEMORY`, `EXHIBIT 001/A`).
- [ ] Stub/undefined concepts render honestly as **mapped-but-UNKNOWN** (not an empty template).
- [ ] `connected_files` link to other case files; `next_case` provides a forward path.
- [ ] Evidence Room section may embed/deep-link to NESC-09; Open Questions to NESC-10.

## Out of scope
- Full Evidence Room and Open Questions internals (NESC-09/10) — this view composes them.
- Authoring concepts beyond Memory.

## Notes
- Evolves the existing `concept.html`; keep the atlas/concept routing intact.
