# NESC-01 — Privacy, identity & consent model

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P0 (foundation — blocks NESC-05, NESC-11)
- **Brief refs:** §11a, §8
- **Depends on:** —

## Summary
Introduce the participant identity + consent data model so public surfaces show **published entries under an anonymized code only**, while real names and unpublished responses stay private. This is the foundation every public/participant surface depends on.

## Why
The brief is firm (§11a): real names are private and never rendered publicly; publication is opt-in; public code = first two letters of the name, uppercased, with collision numbering. Getting this wrong leaks personal testimony.

## Scope / acceptance criteria
- [ ] Interview records gain private + public fields:
  - private: `name` (real, owner-side only), `code`, `published` (bool), recorded timestamp.
  - The real-name → code mapping is stored **privately** (not on any public record projection).
- [ ] **Code generation:** `code = first two letters of name, uppercased`. On collision with an existing code, append the smallest unused integer per-code: `AL`, `AL1`, `AL2`, … Assigned **at save time** from existing records. Non-letter/short names handled gracefully (define fallback, e.g. pad/`XX`).
- [ ] `database.py` (or a new `identity.py`) exposes: assign a code for a new record; a **public projection** helper that returns only published entries with codes and responses, stripping `name` and any private fields.
- [ ] `matcher` / concept matches may be computed for all records, but public projections never expose private fields.
- [ ] Unit-style check: two participants named "Alex" and "Alan" → `AL`, `AL1`. A third "Al" → `AL2`.

## Out of scope
- The interview UI publication choice (NESC-05) and the public Witness Accounts view (NESC-11) — this ticket is the model + helpers only.
- Password-gated investigator route (NESC-02).

## Notes
- Keep backward-compatible with existing `participants.json` records (older records have no `name`/`code`/`published`; treat missing `published` as unpublished; backfill a code lazily if needed for display).
