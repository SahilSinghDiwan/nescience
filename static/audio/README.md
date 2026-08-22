# static/audio — the ambient analog layer

Four clips, **generated rather than recorded**:

| file | plays when |
| --- | --- |
| `sheet-slide.wav` | a parchment sheet is dragged across the desk |
| `clip-snap.wav`   | a card seats into place under its clip |
| `pen-scratch.wav` | a redaction dissolves |
| `drawer.wav`      | the audio toggle is switched on; reserved for drawers |

They are rendered by [`tools/make_foley.py`](../../tools/make_foley.py) — pure
standard library, no numpy, no ffmpeg — and committed alongside it, so the
assets are reproducible and tunable instead of being mystery binaries. Nothing
here needs licensing or attribution, which is why generating beat sourcing: the
exhibit makes no network requests and vendors every asset it uses.

Regenerate after editing the script:

```bash
python3 tools/make_foley.py
```

The random seed is fixed, so regenerating cannot silently change what ships.
Total weight is about 53 KB for all four.

## Replacing one with a real recording

Drop a file in here under the same name. If you change the extension, update
`MANIFEST` in `static/js/foley.js` to match.

`foley.js` also carries a **synthesised fallback** for every cue, so a missing
or undecodable clip degrades to a generated one rather than to silence.

Rules baked into `foley.js` — keep them true of whatever is added:

- muted by default; sound only ever follows a deliberate click on the visible
  toggle in the masthead, and that choice is remembered,
- never autoplay: nothing is fetched or constructed until that click,
- never loud: a hard `0.22` volume ceiling on top of each clip's own level,
- a missing or broken file is never an error.
