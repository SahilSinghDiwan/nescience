# Nescience — Build Brief → Tickets

Source: [`docs/nescience-brief.md`](../docs/nescience-brief.md). Each ticket is a folder under `.scratch/` with a `spec.md`. Tickets follow the existing Flask app's patterns — extend, don't restart.

**Canonical triage labels:** `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`.

## Guiding constraints (apply to every ticket)
- Reuse existing files/patterns (`app.py`, `atlas.py`, `matcher.py`, `database.py`, templates, one stylesheet). No feature sprawl.
- **Self-contained assets only** — textures, fonts, audio bundled in `static/`, committed. No CDNs / network calls.
- Honor `prefers-reduced-motion`; keep parchment/serif contrast readable; never let physics/audio block content or autoplay loudly.
- Public routes must **never** leak private fields (real names, unpublished responses, code mapping). See NESC-01.
- The human owns research direction, questions, interpretation, and design intent — surface decisions, don't invent facts.

## Phases & dependency order

**Phase 0 — Foundations (data, privacy, schema)**
| ID | Ticket | Labels | Depends on |
|----|--------|--------|-----------|
| NESC-01 | [Privacy, identity & consent model](nesc-01-privacy-identity-consent/spec.md) | ready-for-agent | — |
| NESC-02 | [Investigator surface (password-gated)](nesc-02-investigator-surface/spec.md) | ready-for-agent | 01 |
| NESC-03 | [Concept data-model expansion + author Memory](nesc-03-concept-data-model/spec.md) | ready-for-agent | — |
| NESC-04 | [Citations & bibliography system](nesc-04-citations-bibliography/spec.md) | ready-for-agent | 03 |

**Phase 1 — Interview**
| ID | Ticket | Labels | Depends on |
|----|--------|--------|-----------|
| NESC-05 | [Interview: name field + publication consent](nesc-05-interview-consent-flow/spec.md) | ready-for-agent | 01 |

**Phase 2 — Site architecture & content surfaces**
| ID | Ticket | Labels | Depends on |
|----|--------|--------|-----------|
| NESC-06 | [Landing as an "active file"](nesc-06-landing-active-file/spec.md) | ready-for-agent | — |
| NESC-07 | [Archive hub — six ways in](nesc-07-archive-hub/spec.md) | ready-for-agent | — |
| NESC-08 | [Case File view (deep concept)](nesc-08-case-file-view/spec.md) | ready-for-agent | 03 |
| NESC-09 | [Evidence Room — four epistemic tiers](nesc-09-evidence-room/spec.md) | ready-for-agent | 03, 04 |
| NESC-10 | [Open Questions surface](nesc-10-open-questions/spec.md) | ready-for-agent | 03 |
| NESC-11 | [Witness Accounts (public, code-only)](nesc-11-witness-accounts/spec.md) | ready-for-agent | 01, 05 |
| NESC-12 | [Connections — corkboard graph](nesc-12-connections-corkboard/spec.md) | ready-for-agent | 03 |
| NESC-13 | [Investigation Notes](nesc-13-investigation-notes/spec.md) | needs-info | — |

**Phase 3 — Aesthetic & tactile experience**
| ID | Ticket | Labels | Depends on |
|----|--------|--------|-----------|
| NESC-14 | [Aesthetic overhaul → vault/casebook system](nesc-14-aesthetic-vault-casebook/spec.md) | ready-for-agent | — |
| NESC-15 | [Tactile interactions + ambient audio](nesc-15-tactile-interactions/spec.md) | ready-for-agent | 14 |
| NESC-16 | [Accessibility & performance pass](nesc-16-accessibility-performance/spec.md) | ready-for-agent | 14, 15 |

## Suggested sequencing
1. NESC-01, NESC-03 first (unblock the most). NESC-14 can start in parallel (design system).
2. Then NESC-02, NESC-04, NESC-05.
3. Content surfaces (06–12) once schema + consent land.
4. NESC-15/16 layer polish onto working structure — never before it.
