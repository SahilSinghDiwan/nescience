# NESC-13 — Investigation Notes

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P2
- **Brief refs:** §7 (hub entry [006])
- **Depends on:** —

## Summary
Hub entry **[006] INVESTIGATION NOTES** — the archive's public methodology
drawer: how the investigation works, what it accepts as evidence, and where it
agrees to stop.

## Decisions (2026-08-22, from the owner)
The brief lists [006] but never specifies it. Resolved as:

- **Audience: public.** How the archive reaches its conclusions is part of its
  argument, not backstage material. A private [006] would also leave a visible
  dead drawer on a hub of five public surfaces.
- **Content: methodology notes.** Not a dated log and not marginalia —
  standing notes on method.
- **Authoring: markdown committed in the repo**, under `docs/notes/`, mirroring
  how `docs/bibliography.md` already works. No storage layer, no write path,
  no auth, version-controlled.
- **Distinct from NESC-10** because Open Questions are unresolved questions
  *about the mind*; these are notes about *the investigation itself*.

## Delivered
- [x] `notes.py` — reads `docs/notes/*.md`, parses a `key: value` header block,
      renders a narrow markdown subset (h2/h3, paragraphs, wrapped lists,
      blockquotes, rules, bold/italic/code, internal links). Hand-rolled so the
      app keeps its single dependency (Flask); source is HTML-escaped before
      any tags are reintroduced, and links to external hosts are stripped to
      plain text so the no-network promise holds.
- [x] Five authored notes: what counts as evidence · why four tiers · how the
      concepts were chosen · on writing UNKNOWN · how testimony is handled.
- [x] Routes `/archive/notes` (index) and `/archive/notes/<slug>` (404 on miss);
      templates `notes.html` + `note.html` reusing existing case-file styling.
- [x] Hub entry [006] wired to the real route.
- [x] `test_investigation_notes.py` — 14 tests (markdown subset, escaping,
      link policy, loader, routes, hub wiring).

## Follow-on
Retired the "in progress" placeholder: [006] was the last unbuilt drawer, so
`/archive/pending/<section>` and `templates/placeholder.html` were dead code
and have been removed. `test_archive_surfaces.py` updated to assert the
placeholder is fully gone.
