# NESC-16 — Accessibility & performance pass

- **Status:** done
- **Labels:** ready-for-agent
- **Priority:** P2 (cross-cutting)
- **Brief refs:** §12
- **Depends on:** NESC-14, NESC-15

## Summary
A cross-cutting pass to keep the atmospheric design accessible and performant.

## Scope / acceptance criteria
- [x] `prefers-reduced-motion` respected everywhere motion/physics exists.
      Three CSS blocks including a catch-all `*` neutraliser (so a new
      transition is covered the day it lands), plus explicit checks in
      `tactile.js` and `connections.js`.
- [x] Text contrast meets WCAG AA. Audited every colour token against the
      ground it is actually painted on. Four real failures found and fixed
      (below); a fifth candidate, `--line` at 1.49:1, is a decorative hairline
      rule and carries no text, so it is left alone deliberately.
- [x] Keyboard navigability + focus states. Global `:focus-visible` rings for
      links, buttons, inputs, textareas and `[tabindex]`; corkboard nodes are
      real SVG `<a href>` elements, so threads light on keyboard focus as well
      as hover. Added the missing **skip link** to `base.html`.
- [x] Audio never autoplays; toggle reachable and labelled (`aria-pressed`
      button with an `aria-label`, starts muted, 0.22 volume ceiling).
- [x] No network calls / CDNs — verified against what the app actually serves,
      not just the source.
- [x] Page weight: full case-file page including fonts, CSS, all JS and
      textures is **134 KB**. No work needed.

## Contrast fixes
| Pair | Was | Now |
| --- | --- | --- |
| `--ink-faint` labels on the sheet | 4.41 | 5.45 (token darkened to `#5c574c`) |
| stub node label on its corkboard tag | 3.68 | 4.55 (same token) |
| brass text on the sheet | 2.96 | 4.51 (new `--brass-ink` `#796034`) |
| drawer index numeral on its panel | 2.76 | 3.75 (takes `--brass-ink`) |

`--brass` keeps its job on charcoal, borders and focus rings, where it already
clears the bar. The split is enforced by a test, since the whole failure mode
here is a colour being nudged for the look of it without recomputing contrast.

## Delivered
`test_accessibility.py` — 9 tests that parse the real tokens out of the
stylesheet and recompute WCAG ratios for the 17 pairs that actually render,
plus guards for reduced motion, focus rings, the skip link, audio defaults and
the no-network rule. 74 tests pass overall.

## Notes
- Re-check whenever a new tactile surface lands; the palette test will catch
  colour drift on its own.
