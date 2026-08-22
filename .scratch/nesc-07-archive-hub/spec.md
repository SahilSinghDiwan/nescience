# NESC-07 — Archive hub: six ways in

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P1
- **Brief refs:** §7
- **Depends on:** —

## Summary
Build the archive hub — the investigator's index offering **six ways of investigating the question**.

## Why
§7 defines the hub:
```
[001] CASE FILES · [002] WITNESS ACCOUNTS · [003] CONNECTIONS ·
[004] OPEN QUESTIONS · [005] EVIDENCE ROOM · [006] INVESTIGATION NOTES
```

## Scope / acceptance criteria
- [ ] A hub route (e.g. `/archive`) presenting the six labelled entries as case-file drawers/tabs, each numbered `[001]…[006]`.
- [ ] Each links to its surface:
  - [001] Case Files → concept case files (NESC-08)
  - [002] Witness Accounts → public interviews (NESC-11)
  - [003] Connections → corkboard graph (NESC-12)
  - [004] Open Questions → (NESC-10)
  - [005] Evidence Room → (NESC-09)
  - [006] Investigation Notes → (NESC-13)
- [ ] Surfaces not yet built show an honest "in progress / evidence being collected" placeholder rather than a dead link.
- [ ] Aesthetic aligns with NESC-14; navigation should already hint at the "physical dossier" feel (full tactile behavior is NESC-15).

## Out of scope
- The six destination surfaces themselves (their own tickets).

## Notes
- Current `/archive` (flat case list) becomes the [002]/[001] destinations; the hub is the new top level.
