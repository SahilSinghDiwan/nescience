"""NESC-16 — accessibility & performance guards.

The atmospheric palette is the thing most likely to drift back below a
readable bar: a colour gets nudged for the look of it and nobody recomputes
the contrast. These tests read the real tokens out of the stylesheet and
recompute WCAG 2.1 ratios for the pairs that actually render, so a nudge that
costs legibility fails the suite instead of shipping.

The no-network rule (brief §12) is guarded the same way — by reading what the
app actually serves, not by trusting that nobody pasted a CDN link."""

import re

import pytest

from app import app

CSS_PATH = "static/css/nescience.css"


# ----------------------------------------------------------
# WCAG 2.1 relative luminance / contrast
# ----------------------------------------------------------

def _luminance(hex_colour):
    h = hex_colour.lstrip("#")
    channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    channels = [
        c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
        for c in channels
    ]
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(fg, bg):
    lighter, darker = sorted((_luminance(fg), _luminance(bg)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def over(fg, alpha, bg):
    """Composite a translucent layer onto a ground — some panels are painted
    as a wash over the folder beneath them, and the wash is what text sits on."""
    f = [int(fg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    b = [int(bg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#%02x%02x%02x" % tuple(
        round(alpha * f[i] + (1 - alpha) * b[i]) for i in range(3)
    )


@pytest.fixture(scope="module")
def tokens():
    """The palette, read from the stylesheet so the test cannot drift from it."""
    css = open(CSS_PATH, encoding="utf-8").read()
    found = dict(re.findall(r"(--[a-z0-9-]+):\s*(#[0-9a-fA-F]{6})\s*;", css))
    assert found, "no colour tokens parsed out of the stylesheet"
    return found


def test_expected_tokens_exist(tokens):
    for name in (
        "--paper", "--paper-3", "--vault", "--charcoal", "--ink", "--ink-soft",
        "--ink-faint", "--hand", "--stamp", "--brass", "--brass-ink", "--manila",
    ):
        assert name in tokens, f"{name} vanished from the palette"


# label -> (foreground, background, minimum ratio)
#
# Backgrounds are the ground each colour is actually painted on: .wrap lays a
# parchment sheet over the vault, so page text sits on --paper, while the
# masthead and footer sit on the dark ground.
def _pairs(t):
    drawer_panel = over("#fffaee", 0.35, "#cdb375")   # .drawer .idx wash
    return {
        # body text on the parchment sheet — AA 4.5
        "body prose on the sheet": (t["--ink-soft"], t["--paper"], 4.5),
        "headings on the sheet": (t["--ink"], t["--paper"], 4.5),
        "handwriting on the sheet": (t["--hand"], t["--paper"], 4.5),
        "faint labels on the sheet": (t["--ink-faint"], t["--paper"], 4.5),
        "faint labels on a raised card": (t["--ink-faint"], t["--paper-3"], 4.5),
        "brass text on the sheet": (t["--brass-ink"], t["--paper"], 4.5),
        # UNKNOWN is emphasis, but it still carries words — hold it to AA too
        "UNKNOWN red on the sheet": (t["--stamp"], t["--paper"], 4.5),
        "UNKNOWN red on a raised card": (t["--stamp"], t["--paper-3"], 4.5),
        # the dark grounds
        "wordmark on charcoal": (t["--paper"], t["--charcoal"], 4.5),
        "department line on charcoal": (t["--brass-soft"], t["--charcoal"], 4.5),
        "nav links on charcoal": ("#b9b0a0", t["--charcoal"], 4.5),
        "page footer on the vault": ("#8a8172", t["--vault"], 4.5),
        "audio toggle on charcoal": ("#8d8474", t["--charcoal"], 4.5),
        # manila folder drawers
        "drawer description on manila": ("#4a3f27", "#cdb375", 4.5),
        "drawer numeral on its panel": (t["--brass-ink"], drawer_panel, 3.0),
        # corkboard tags
        "node label on its tag": (t["--ink"], t["--paper-3"], 4.5),
        "stub node label on its tag": (t["--ink-faint"], "#d8cdb2", 4.5),
    }


def test_every_rendered_text_pair_meets_its_bar(tokens):
    failures = []
    for label, (fg, bg, need) in _pairs(tokens).items():
        ratio = contrast(fg, bg)
        if ratio < need:
            failures.append(f"{label}: {ratio:.2f} < {need} ({fg} on {bg})")
    assert not failures, "contrast regressions:\n  " + "\n  ".join(failures)


def test_brass_is_not_used_as_text_on_parchment():
    """--brass reads as metal on charcoal but only reaches 2.96:1 on the
    sheet; --brass-ink is the variant for text. Guard the split."""
    css = open(CSS_PATH, encoding="utf-8").read()
    # Match the `color` property only — not border-color, outline-color or
    # any other hyphenated property that happens to end in "color".
    offenders = [
        line.strip()
        for line in css.splitlines()
        if re.search(r"(?<![-\w])color:\s*var\(--brass\)", line)
    ]
    assert not offenders, (
        "--brass used as a text colour; use --brass-ink on parchment:\n  "
        + "\n  ".join(offenders)
    )


# ----------------------------------------------------------
# Motion, keyboard, audio, network
# ----------------------------------------------------------

def test_reduced_motion_is_honoured_wherever_motion_exists():
    css = open(CSS_PATH, encoding="utf-8").read()
    assert "@media (prefers-reduced-motion: reduce)" in css
    # A blanket neutraliser, so a new transition is covered the day it lands.
    blanket = re.search(
        r"@media \(prefers-reduced-motion: reduce\) \{\s*\*\s*\{([^}]*)\}", css
    )
    assert blanket, "no catch-all reduced-motion rule"
    assert "transition-duration" in blanket.group(1)
    assert "animation-duration" in blanket.group(1)

    for path in ("static/js/tactile.js", "static/js/connections.js"):
        js = open(path, encoding="utf-8").read()
        assert "prefers-reduced-motion" in js, f"{path} never checks the setting"


def test_focus_states_exist_for_every_interactive_kind():
    css = open(CSS_PATH, encoding="utf-8").read()
    for selector in (
        "a:focus-visible", "button:focus-visible", "input:focus-visible",
        "textarea:focus-visible", "[tabindex]:focus-visible",
    ):
        assert selector in css, f"no focus ring for {selector}"


def test_every_page_offers_a_skip_link():
    css = open(CSS_PATH, encoding="utf-8").read()
    assert ".skip-link:focus" in css, "skip link never becomes visible"
    client = app.test_client()
    for url in ("/", "/archive", "/archive/notes", "/atlas/Memory", "/interview"):
        body = client.get(url).get_data(as_text=True)
        assert 'class="skip-link"' in body, f"{url} has no skip link"
        assert 'id="file"' in body, f"{url} has no skip target"


def test_audio_never_autoplays_and_starts_muted():
    js = open("static/js/foley.js", encoding="utf-8").read()
    # The toggle is the only thing that can enable sound, and it starts off.
    assert re.search(r"var enabled\s*=\s*false", js)
    ceiling = re.search(r"var CEILING\s*=\s*([0-9.]+)", js)
    assert ceiling and float(ceiling.group(1)) <= 0.3, "audio ceiling too loud"


def test_audio_context_is_not_created_until_a_gesture():
    """An exhibit that opened an AudioContext on load would be doing the very
    thing the no-autoplay rule exists to prevent."""
    js = open("static/js/foley.js", encoding="utf-8").read()
    assert re.search(r"var ctx\s*=\s*null", js), "context should start unbuilt"
    # The only construction site sits inside the lazy accessor.
    assert js.count("new Ctx()") == 1
    accessor = js[js.index("function audio()"):js.index("function noise(")]
    assert "new Ctx()" in accessor, "context built outside the lazy accessor"


def test_every_manifest_cue_has_a_synthesised_voice():
    """No recordings ship, so a cue without a voice is a silent call site."""
    js = open("static/js/foley.js", encoding="utf-8").read()
    manifest = set(re.findall(r'"([a-z-]+)":\s*\{\s*file:', js))
    if not manifest:
        manifest = set(re.findall(r'"([a-z-]+)":\s*\{ file:', js))
    voices_block = js[js.index("var VOICES = {"):js.index("function synth(")]
    voices = set(re.findall(r'"([a-z-]+)":\s*function', voices_block))
    assert manifest, "no manifest entries parsed"
    assert manifest <= voices, f"cues with no voice: {sorted(manifest - voices)}"


def test_call_sites_only_use_cues_that_exist():
    foley_js = open("static/js/foley.js", encoding="utf-8").read()
    tactile_js = open("static/js/tactile.js", encoding="utf-8").read()
    voices_block = foley_js[foley_js.index("var VOICES = {"):foley_js.index("function synth(")]
    voices = set(re.findall(r'"([a-z-]+)":\s*function', voices_block))
    used = set(re.findall(r'foley\.play\("([a-z-]+)"\)', tactile_js))
    assert used, "no play call sites found"
    assert used <= voices, f"call sites fire unknown cues: {sorted(used - voices)}"


def test_audio_toggle_is_a_labelled_button():
    js = open("static/js/tactile.js", encoding="utf-8").read()
    assert 'aria-pressed' in js
    assert 'aria-label' in js


def test_nothing_reaches_the_network():
    """Brief §12: no CDNs, no external assets, anywhere the app serves."""
    client = app.test_client()
    served = []
    for url in (
        "/", "/archive", "/archive/notes", "/archive/witnesses",
        "/archive/connections", "/archive/evidence-room",
        "/archive/open-questions", "/atlas", "/atlas/Memory", "/interview",
        "/static/css/nescience.css", "/static/js/tactile.js",
        "/static/js/foley.js", "/static/js/connections.js",
        "/static/js/interview.js",
    ):
        served.append(client.get(url).get_data(as_text=True))

    external = re.findall(
        r"""(?:src|href)\s*=\s*["']https?://[^"']+|url\(\s*["']?https?://[^)]+""",
        "\n".join(served),
    )
    assert not external, "external asset references found:\n  " + "\n  ".join(external)
