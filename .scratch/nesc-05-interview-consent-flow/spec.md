# NESC-05 — Interview: name field + publication consent

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P0
- **Brief refs:** §8, §11a
- **Depends on:** NESC-01

## Summary
Add a name field up front and a **publication choice** at the end of the interview, wiring both into the privacy/consent model. Keep Nescience as the questioner (no investigator/witness role-play).

## Why
§8: the interview collects a name up front and ends with "Would you like your responses displayed in the public archive?" — Yes publishes under an anonymized code; No keeps it investigation-only (§11a).

## Scope / acceptance criteria
- [ ] Name field collected up front (in the interview intake). Stored privately (NESC-01); **never** rendered on public routes.
- [ ] Confirm the five modules match the brief: **I Experience · II The Story · III Decisions · IV The Unknown · V Reflection.** Module IV turns the participant toward what they don't know about themselves; Module V acknowledges the questions may have shifted their thinking. Adjust `protocol.py` wording only if needed — the system records exactly what the participant enters (nothing pre-filled).
- [ ] Opening tone preserved: *"There's no right answer here…"* (already in the Introduction).
- [ ] **End step:** an explicit publication choice — Yes → `published = true` and a code is assigned (NESC-01); No → stored, `published = false`, investigation-only.
- [ ] `POST /api/interview` persists name + publication decision + assigned code via the NESC-01 helpers.
- [ ] Confirmation screen shows the participant their **code** (not name) and whether they published.

## Out of scope
- Public Witness Accounts rendering (NESC-11).
- Aesthetic overhaul of the interview (NESC-14/15).

## Notes
- Keep the stepper (`static/js/interview.js`) approach; extend it, don't rewrite.
