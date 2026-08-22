# NESC-14 — Aesthetic overhaul → vault/casebook design system

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P1 (can start in parallel with Phase 0)
- **Brief refs:** §5, §7, §12
- **Depends on:** —

## Summary
Evolve the single stylesheet from the current minimal monochrome into the **ancient leather-bound casebook in a dimly lit university vault** direction — digitized history treated as a physical artifact.

## Why
§5 is a firm art-direction spec (palette, surfaces, typography, props) anchored to the reference flat-lay `docs/refs/evidence-flatlay.jpg`. The current CSS is explicitly a starting point to evolve.

## Scope / acceptance criteria
- [ ] **Palette:** near-black ground; manila/kraft folder tones; aged off-white forms; ink blue-black handwriting; **one faded evidence-red** reserved for stamps and the word **UNKNOWN**. High contrast, dim ambient lighting.
- [ ] **Surfaces:** textured charcoals + aged-parchment backdrops; subtle paper grain, faint ink bleeds, weathered/coffee-stained edges — every layout has physical weight. Textures bundled in `static/` (committed, no CDNs).
- [ ] **Typography:** editorial **serif** (rare-manuscript feel) paired with raw **typewriter** for case tags / form labels (e.g. `EXHIBIT 001/A`). Printed field labels filled "by hand." Fonts self-hosted in `static/`.
- [ ] **Props & marks:** stamped seals, red rubber stamps, brass paperclips, handwritten marginal notes, case/exhibit numbers, evidence cards, sample wells, thin rules — as reusable components.
- [ ] Applied consistently across existing templates (landing, interview, archive, case, atlas, concept, 404) without breaking them.
- [ ] **Guardrails honored (§4):** investigation *language/props* only — never horror, serial-killer wall, cyberpunk, futuristic-AI-dashboard, or actual-crime framing. Restraint over theme-park.
- [ ] Readable contrast; the design must not depend on motion (that's NESC-15).

## Out of scope
- Interaction/physics/audio (NESC-15).

## Notes
- Reproduce the flat-lay's material realism (overlapping, slightly-rotated, photographed-desk feel) as a design language, not a literal copy.
- Benchmark for polish: Morgan Library & Museum digital archives (§6).
