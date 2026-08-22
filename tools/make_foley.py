"""Render the exhibit's ambient foley to WAV files (NESC-15).

The four cues are generated rather than recorded, so there is nothing to
licence, fetch, or attribute — the same reason every other asset in this
project is committed rather than pulled from a CDN. This script is committed
alongside the files it produces so the assets are reproducible and tunable
instead of being mystery binaries in static/.

    python3 tools/make_foley.py

Rendering offline (rather than in the browser, as static/js/foley.js also can)
buys layering that would be wasteful in realtime: a rustle is many overlapping
grains, a clip has metal ringing over its click. Pure standard library — no
numpy, no ffmpeg — to match a project that ships one dependency.
"""

import math
import os
import random
import struct
import wave

RATE = 22050          # plenty for foley; keeps the files small
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "static", "audio")


# ----------------------------------------------------------
# Building blocks
# ----------------------------------------------------------

def frames(seconds):
    return int(RATE * seconds)


def noise(n, rng):
    return [rng.uniform(-1.0, 1.0) for _ in range(n)]


def svf(signal, cutoff, q=1.0, mode="band"):
    """Chamberlin state-variable filter. `cutoff` may be a constant or a
    per-sample list, which is how the sweeps below are done."""
    low = band = 0.0
    out = []
    damp = 1.0 / q
    for i, x in enumerate(signal):
        fc = cutoff[i] if isinstance(cutoff, list) else cutoff
        f = 2.0 * math.sin(math.pi * min(fc, RATE / 3.0) / RATE)
        high = x - low - damp * band
        band += f * high
        low += f * band
        out.append({"low": low, "band": band, "high": high}[mode])
    return out


def sweep(n, start, end):
    """Exponential glide, which is how physical resonances actually fall."""
    if start <= 0 or end <= 0:
        return [start] * n
    return [start * (end / start) ** (i / max(1, n - 1)) for i in range(n)]


def envelope(n, attack, decay, curve=2.5):
    """Attack/decay in seconds, with a convex tail."""
    a, d = max(1, frames(attack)), max(1, frames(decay))
    env = []
    for i in range(n):
        if i < a:
            env.append(i / a)
        else:
            t = min(1.0, (i - a) / d)
            env.append((1.0 - t) ** curve)
    return env


def sine(n, freq_start, freq_end=None):
    freq_end = freq_start if freq_end is None else freq_end
    fs = sweep(n, freq_start, freq_end)
    out, phase = [], 0.0
    for f in fs:
        phase += 2 * math.pi * f / RATE
        out.append(math.sin(phase))
    return out


def mix(*layers):
    n = max(len(l) for l in layers)
    out = [0.0] * n
    for layer in layers:
        for i, v in enumerate(layer):
            out[i] += v
    return out


def apply_env(signal, env):
    return [s * e for s, e in zip(signal, env)]


def normalise(signal, peak=0.72):
    hi = max(abs(s) for s in signal) or 1.0
    return [s * peak / hi for s in signal]


def declick(signal, ms=4.0):
    """Fade the tail only.

    A hard edge at the end is an audible tick. The *start* needs no fade —
    every envelope here already begins at zero — and fading it would blunt
    the attack transient, which for a snap is the entire sound."""
    n = max(1, frames(ms / 1000.0))
    out = list(signal)
    for i in range(min(n, len(out))):
        out[-(i + 1)] *= i / n
    return out


def write(name, signal):
    signal = normalise(signal, PEAKS.get(name, 0.72))
    if name not in NO_DECLICK:
        signal = declick(signal)
    path = os.path.join(OUT, name)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(b"".join(
            struct.pack("<h", int(max(-1.0, min(1.0, s)) * 32767)) for s in signal
        ))
    return path, os.path.getsize(path)


# ----------------------------------------------------------
# The four cues
# ----------------------------------------------------------

def sheet_slide(rng):
    """A parchment sheet dragged across a desk: fibrous, breathy, uneven."""
    n = frames(0.34)
    body = svf(noise(n, rng), sweep(n, 2100, 620), q=0.8, mode="band")

    # Paper is not smooth — it is a crowd of tiny catches. A slow random
    # walk over the amplitude gives the drag its grain.
    grain, g = [], 0.0
    for _ in range(n):
        g += rng.uniform(-0.06, 0.06)
        g = max(-0.5, min(0.5, g))
        grain.append(1.0 + g)

    shaped = [b * g for b, g in zip(body, grain)]
    return apply_env(shaped, envelope(n, 0.045, 0.30, curve=1.8))


def clip_snap(rng):
    """A card seating under a brass clip: a click, a small body, some metal."""
    n = frames(0.14)

    click = apply_env(
        svf(noise(n, rng), sweep(n, 4200, 2400), q=1.2, mode="band"),
        envelope(n, 0.0006, 0.045, curve=3.5),
    )
    body = apply_env(sine(n, 240, 96), envelope(n, 0.001, 0.06, curve=3.0))
    # Two partials, deliberately not harmonic — brass, not a bell.
    ring = apply_env(
        mix([0.5 * s for s in sine(n, 2640)], [0.32 * s for s in sine(n, 3910)]),
        envelope(n, 0.0008, 0.10, curve=4.0),
    )
    return mix([c * 1.0 for c in click], [b * 0.55 for b in body],
               [r * 0.22 for r in ring])


def pen_scratch(rng):
    """A nib crossing paper: narrow, dry, and audibly rough."""
    n = frames(0.20)
    raw = svf(noise(n, rng), sweep(n, 3000, 1700), q=4.0, mode="band")

    # The scratch is amplitude-modulated by the nib catching the fibres;
    # a fast irregular flutter reads as friction rather than as hiss.
    flutter = []
    phase = 0.0
    for _ in range(n):
        phase += 2 * math.pi * rng.uniform(70, 190) / RATE
        flutter.append(0.55 + 0.45 * abs(math.sin(phase)))

    shaped = [r * f for r, f in zip(raw, flutter)]
    return apply_env(shaped, envelope(n, 0.006, 0.17, curve=2.0))


def drawer(rng):
    """A wooden drawer pulled open, ending against its stop."""
    n = frames(0.52)
    roll = apply_env(
        svf(noise(n, rng), sweep(n, 950, 260), q=0.7, mode="low"),
        envelope(n, 0.07, 0.42, curve=1.5),
    )

    # The stop: a knock late in the sound, not at the very end, so the tail
    # rings past it the way a real drawer does.
    knock_at = frames(0.36)
    kn = n - knock_at
    knock = apply_env(
        mix(sine(kn, 190, 78),
            [0.4 * s for s in svf(noise(kn, rng), 1400, q=1.0, mode="band")]),
        envelope(kn, 0.0008, 0.12, curve=3.2),
    )
    padded = [0.0] * knock_at + [k * 0.5 for k in knock]
    return mix(roll, padded)


def nav_click(rng):
    """Navigating to a new section: a dry switch, closer to a typewriter key
    than to a UI beep. Very short — it must not sit under the next page."""
    n = frames(0.055)
    tick = apply_env(
        svf(noise(n, rng), sweep(n, 5200, 2800), q=1.6, mode="band"),
        envelope(n, 0.0005, 0.018, curve=4.0),
    )
    body = apply_env(sine(n, 1250, 620), envelope(n, 0.0008, 0.03, curve=3.5))
    return mix(tick, [b * 0.42 for b in body])


def page_flip(rng):
    """Opening a file: a sheet turning over — air first, then the settle as
    it lands. Two gestures, not one, or it reads as a swipe."""
    n = frames(0.46)

    # The turn: broadband air that rises as the page lifts and falls as it
    # comes over. A single downward sweep sounds like a drag instead.
    half = n // 2
    rise = svf(noise(half, rng), sweep(half, 700, 2600), q=0.8, mode="band")
    fall = svf(noise(n - half, rng), sweep(n - half, 2600, 900), q=0.8, mode="band")
    turn = apply_env(rise + fall, envelope(n, 0.06, 0.34, curve=1.6))

    # The landing: a soft slap late in the sound.
    at = frames(0.33)
    ln = n - at
    land = apply_env(
        svf(noise(ln, rng), sweep(ln, 1600, 500), q=1.0, mode="band"),
        envelope(ln, 0.002, 0.10, curve=3.0),
    )
    return mix(turn, [0.0] * at + [x * 0.7 for x in land])


def ambient_bed(rng):
    """A room tone for the vault: a low drone that drifts, under a breath of
    air. Written to loop seamlessly — the tail is crossfaded into the head,
    so it can run indefinitely without a seam."""
    seconds = 12.0
    n = frames(seconds)

    # A minor-flavoured stack, detuned slightly so it beats slowly rather
    # than sitting still. Low enough to sit under reading without competing.
    layers = []
    for freq, level, drift in ((55.0, 0.55, 0.06), (82.41, 0.34, 0.09),
                               (110.0, 0.22, 0.05), (130.81, 0.13, 0.11)):
        tone = sine(n, freq, freq * (1.0 + drift / 100.0))
        # Each partial breathes on its own slow cycle, so the stack never
        # repeats audibly inside the loop.
        rate = rng.uniform(0.03, 0.07)
        phase = rng.uniform(0, math.pi * 2)
        swell = [0.6 + 0.4 * math.sin(2 * math.pi * rate * (i / RATE) + phase)
                 for i in range(n)]
        layers.append([t * s * level for t, s in zip(tone, swell)])

    # Air: heavily filtered noise, barely there, to stop the drone sounding
    # synthetic. A room is never silent.
    air = svf(noise(n, rng), 420, q=0.5, mode="low")
    layers.append([a * 0.16 for a in air])

    bed = mix(*layers)

    # Seamless loop: crossfade the last `x` seconds over the first `x`.
    x = frames(1.5)
    for i in range(x):
        t = i / x
        bed[i] = bed[i] * t + bed[n - x + i] * (1 - t)
    return bed[: n - x]


CUES = {
    "sheet-slide.wav": sheet_slide,
    "clip-snap.wav": clip_snap,
    "pen-scratch.wav": pen_scratch,
    "drawer.wav": drawer,
    "nav-click.wav": nav_click,
    "page-flip.wav": page_flip,
    "ambient-bed.wav": ambient_bed,
}

# The bed loops under everything else, so it must not be tail-faded (that
# would punch a hole in the loop) and it sits much lower in level.
NO_DECLICK = {"ambient-bed.wav"}
PEAKS = {"ambient-bed.wav": 0.55}


def main():
    os.makedirs(OUT, exist_ok=True)
    # Fixed seed: regenerating must not silently change what ships.
    rng = random.Random(20260822)
    for name, render in CUES.items():
        path, size = write(name, render(rng))
        print(f"{os.path.basename(path):18} {size:>9,} bytes")


if __name__ == "__main__":
    main()
