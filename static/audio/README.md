# static/audio — empty, and that is the working state

No recordings ship with this build and none are required. The ambient cues are
**synthesised at runtime** by `static/js/foley.js` using the Web Audio API:
shaped noise through a filter envelope, with a short pitched body where a
physical event would have one. Paper is broad and breathy; the clip is a tight
transient over a small thud.

That suits an exhibit that makes no network requests and vendors every asset —
there is no file to licence, fetch, or forget to commit. It is foley, not a
field recording, and it does not pretend otherwise.

## Replacing a cue with a real recording

Drop a file in here under the matching name and it takes over that cue
automatically; the synth stays as the fallback if the file fails to load.

| drop this file in | plays when |
| --- | --- |
| `sheet-slide.mp3` | a parchment sheet is dragged across the desk |
| `clip-snap.mp3`   | a card seats into place under its clip |
| `pen-scratch.mp3` | a redaction dissolves |
| `drawer.mp3`      | the audio toggle is switched on; reserved for drawers |

Rules baked into `foley.js` — keep them true of whatever is added:

- muted by default; sound only ever follows a deliberate click on the visible
  toggle in the masthead, and that choice is remembered,
- never autoplay: the audio context is not created until that click,
- never loud: a hard `0.22` volume ceiling,
- a missing or broken file is silence, not an error.

Use only assets you can licence (CC0 / CC-BY with attribution recorded here).
