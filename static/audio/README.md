# static/audio — the ambient analog layer (currently empty on purpose)

No audio ships with this build; the assets have not been sourced yet.
`static/js/foley.js` already wires the toggle, the persistence and every
call site, so installing sound is a copy-and-paste:

| drop this file in | plays when |
| --- | --- |
| `sheet-slide.mp3` | a parchment sheet is dragged across the desk |
| `clip-snap.mp3`   | a card seats into place under its clip |
| `pen-scratch.mp3` | a redaction dissolves |
| `drawer.mp3`      | reserved for a folder/drawer opening |

Rules baked into `foley.js` — keep them true of whatever is added:

- muted by default; sound only ever follows a deliberate click on the
  visible toggle in the masthead, and that choice is remembered,
- never autoplay, never loud: a hard `0.22` volume ceiling,
- a missing file is silence, not an error, so the exhibit is always
  shippable with this directory empty.

Use only assets you can licence (CC0 / CC-BY with attribution recorded here).
