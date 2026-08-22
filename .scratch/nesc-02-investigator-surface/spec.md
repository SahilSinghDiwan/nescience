# NESC-02 — Investigator surface (password-gated)

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P0
- **Brief refs:** §2, §11a
- **Depends on:** NESC-01

## Summary
Add a private, password-gated `/investigator` surface that shows **everything** — real names, unpublished responses, the code mapping, and interview→concept matches. Public templates must never render these fields.

## Why
§11a requires a clear split between public (codes only, published only) and an owner-only view of the full record for actually doing the investigation.

## Scope / acceptance criteria
- [ ] Password comes from an **environment variable** (e.g. `NESCIENCE_INVESTIGATOR_PASSWORD`), never committed. If unset, the route is disabled (returns 404 or a clear "not configured" state) rather than open.
- [ ] Simple auth gate (session cookie after correct password; a plain login form is fine). No user accounts.
- [ ] `/investigator` lists all cases with real name, code, published state, timestamp; links to a full case view showing complete transcript + matches + the code mapping.
- [ ] Reuse existing archive/case templates where possible, but this is a **separate** template set/flag so private fields can't leak into public templates.
- [ ] Add `.env`/config guidance to README; ensure no secret is committed.

## Out of scope
- Public archive/Witness Accounts (NESC-11).

## Notes
- Keep it minimal and honest — this is an internal tool, not a product login. Rate-limiting/lockout is nice-to-have, not required.
