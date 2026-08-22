# NESC-04 — Citations & bibliography system

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P1 (blocks NESC-09 display)
- **Brief refs:** §11
- **Depends on:** NESC-03

## Summary
Every factual claim / Evidence Room exhibit must trace to a **real, verifiable paper** surfaced in the UI as a reference card / footnote. Build the canonical bibliography and the citation-rendering path.

## Why
§11: "No invented or unattributed studies." Concept entries carry a `citations` list; the canonical list lives in `docs/bibliography.md`.

## Scope / acceptance criteria
- [ ] Create `docs/bibliography.md` as the canonical, keyed reference list (author, year, title, journal/source; optional DOI/URL). Seed with verified starter refs from §11:
  - Scoville & Milner 1957 (H.M.)
  - Loftus & Palmer 1974; Loftus & Pickrell 1995 (false memory)
  - Nader, Schafe & LeDoux 2000 (reconsolidation)
- [ ] A small loader (e.g. `bibliography.py` or a parsed data file) maps citation keys → reference metadata for templates.
- [ ] A reusable **reference card / footnote** template partial renders a citation as an artifact in the UI.
- [ ] Concept `citations` keys (NESC-03) resolve to real entries; a missing/unknown key is caught (build-time check or visible warning), never silently rendered.
- [ ] **Verification gate:** each seeded reference is confirmed to be a real paper before display; unverifiable claims are not shown.

## Out of scope
- Full Evidence Room layout (NESC-09) — this provides the citation primitive it uses.

## Notes
- Keep it a plain committed markdown + light loader; no external citation API.
