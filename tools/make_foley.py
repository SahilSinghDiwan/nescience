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
    signal = declick(normalise(signal))
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


CUES = {
    "sheet-slide.wav": sheet_slide,
    "clip-snap.wav": clip_snap,
    "pen-scratch.wav": pen_scratch,
    "drawer.wav": drawer,
}


def main():
    os.makedirs(OUT, exist_ok=True)
    # Fixed seed: regenerating must not silently change what ships.
    rng = random.Random(20260822)
    for name, render in CUES.items():
        path, size = write(name, render(rng))
        print(f"{os.path.basename(path):18} {size:>7,} bytes")


if __name__ == "__main__":
    main()
