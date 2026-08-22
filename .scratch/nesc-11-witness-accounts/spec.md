# NESC-11 — Witness Accounts (public, code-only)

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P1
- **Brief refs:** §7, §8, §11a
- **Depends on:** NESC-01, NESC-05

## Summary
Public surface showing interview responses of **consenting** participants, **under their code only**, never real names — and only entries the participant chose to publish.

## Why
§7/§11a: public surfaces render published entries only, codes only; unpublished responses are investigator-only.

## Scope / acceptance criteria
- [ ] Witness Accounts route (hub entry [002]) lists **published** entries only, each identified by code (e.g. `AL`), never name.
- [ ] Uses the NESC-01 public projection helper — template has **no access** to private fields (name, mapping, unpublished records).
- [ ] Individual witness view shows the participant's responses (transcript) under the code; may surface the concept **leads** (matcher) as investigative connective tissue.
- [ ] Unpublished and legacy/no-consent records are excluded from all public rendering.
- [ ] Guard test: a record with `published = false` never appears on any public route; no route exposes `name`.

## Out of scope
- Investigator (full) view (NESC-02).

## Notes
- Participants are **participants**, not suspects/patients — copy must reflect §8's ethical framing.
