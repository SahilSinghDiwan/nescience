// ==========================================================
// NESCIENCE — foley hook (NESC-15)
//
// The ambient analog layer: paper slides, pen scratches, the
// soft snap of a clip.
//
// The four clips in /static/audio are GENERATED, not recorded —
// rendered by tools/make_foley.py and committed, so there is
// nothing to licence, fetch, or forget. That keeps the exhibit's
// promise that it makes no network requests and vendors every
// asset. It is foley, not a field recording, and it is honest
// about being made rather than captured.
//
// If a clip is missing or fails to decode, the same cue is
// SYNTHESISED here at runtime through the Web Audio API, so the
// exhibit is never silent for want of a file. Replacing a clip is
// just dropping a new file under its MANIFEST name.
//
// Rules kept here so they cannot be forgotten later:
//   * muted by default, always — the toggle starts OFF and only
//     a deliberate click (persisted in localStorage) turns it on,
//   * never autoplay: the audio context is not even created until
//     a deliberate gesture, and nothing plays while disabled,
//   * quiet: a hard volume ceiling, well under conversational,
//   * a missing asset is silence, never an error.
// ==========================================================

(function (global) {
  "use strict";

  var STORAGE_KEY = "nescience.foley";
  var CEILING = 0.22;              // hard quiet ceiling
  var BASE = "/static/audio/";

  // name -> { file, volume }. The files are generated, not recorded —
  // see tools/make_foley.py, which renders exactly these four.
  var MANIFEST = {
    "sheet-slide": { file: "sheet-slide.wav", volume: 0.7 },  // paper dragged across the desk
    "snap":        { file: "clip-snap.wav",   volume: 1.0 },  // a card seating under the clip
    "ink":         { file: "pen-scratch.wav", volume: 0.6 },  // redaction dissolving
    "drawer":      { file: "drawer.wav",      volume: 0.8 }   // a folder pulled open
  };

  var cache = {};
  var enabled = false;
  var listeners = [];

  // --------------------------------------------------------
  // Synthesised foley
  //
  // One AudioContext, created on the first deliberate gesture and
  // never before — an exhibit that opened an audio context on load
  // would be doing the thing the no-autoplay rule exists to prevent.
  // --------------------------------------------------------

  var ctx = null;
  var noiseBuffer = null;

  function audio() {
    if (ctx) return ctx;
    var Ctx = global.AudioContext || global.webkitAudioContext;
    if (!Ctx) return null;
    try { ctx = new Ctx(); } catch (e) { ctx = null; }
    return ctx;
  }

  /** Two seconds of white noise, made once and reused by every cue. */
  function noise(ac) {
    if (noiseBuffer) return noiseBuffer;
    var frames = Math.floor(ac.sampleRate * 2);
    noiseBuffer = ac.createBuffer(1, frames, ac.sampleRate);
    var data = noiseBuffer.getChannelData(0);
    for (var i = 0; i < frames; i++) data[i] = Math.random() * 2 - 1;
    return noiseBuffer;
  }

  /** A burst of filtered noise with an attack/decay envelope. */
  function burst(ac, out, opts) {
    var src = ac.createBufferSource();
    src.buffer = noise(ac);
    src.loop = true;
    src.playbackRate.value = opts.rate || 1;

    var filter = ac.createBiquadFilter();
    filter.type = opts.type || "bandpass";
    filter.frequency.value = opts.from;
    filter.Q.value = opts.q || 1;

    var gain = ac.createGain();
    var t = ac.currentTime;
    var attack = opts.attack || 0.005;
    var dur = opts.duration;

    gain.gain.setValueAtTime(0.0001, t);
    gain.gain.linearRampToValueAtTime(opts.peak, t + attack);
    // Exponential tails read as physical; linear ones read as electronic.
    gain.gain.exponentialRampToValueAtTime(0.0001, t + dur);

    if (opts.to && opts.to !== opts.from) {
      filter.frequency.exponentialRampToValueAtTime(opts.to, t + dur);
    }

    src.connect(filter); filter.connect(gain); gain.connect(out);
    src.start(t);
    src.stop(t + dur + 0.02);
  }

  /** A short pitched body — the wooden part of a knock or a snap. */
  function thud(ac, out, opts) {
    var osc = ac.createOscillator();
    osc.type = "sine";
    var gain = ac.createGain();
    var t = ac.currentTime;

    osc.frequency.setValueAtTime(opts.from, t);
    osc.frequency.exponentialRampToValueAtTime(opts.to, t + opts.duration);
    gain.gain.setValueAtTime(opts.peak, t);
    gain.gain.exponentialRampToValueAtTime(0.0001, t + opts.duration);

    osc.connect(gain); gain.connect(out);
    osc.start(t);
    osc.stop(t + opts.duration + 0.02);
  }

  // Each voice is a small recipe for a physical event. Levels are
  // relative; the master gain applies the ceiling.
  var VOICES = {
    // A parchment sheet dragged across a desk: broad, breathy, brief.
    "sheet-slide": function (ac, out) {
      burst(ac, out, { from: 1800, to: 700, q: 0.7, peak: 0.5,
                       attack: 0.03, duration: 0.26 });
    },
    // A card seating under a brass clip: a tight tick over a small body.
    "snap": function (ac, out) {
      burst(ac, out, { from: 3200, to: 2000, q: 1.4, peak: 0.85,
                       attack: 0.001, duration: 0.055 });
      thud(ac, out, { from: 220, to: 90, peak: 0.28, duration: 0.07 });
    },
    // A nib crossing paper: narrower, grainier, slightly longer.
    "ink": function (ac, out) {
      burst(ac, out, { from: 2600, to: 1500, q: 3.5, peak: 0.42,
                       attack: 0.004, duration: 0.14, rate: 1.4 });
    },
    // A drawer pulled open: low, rolling, with a soft stop at the end.
    "drawer": function (ac, out) {
      burst(ac, out, { type: "lowpass", from: 900, to: 300, q: 0.6,
                       peak: 0.55, attack: 0.05, duration: 0.42 });
      thud(ac, out, { from: 150, to: 70, peak: 0.2, duration: 0.16 });
    }
  };

  function synth(name, volume) {
    var ac = audio();
    if (!ac || !VOICES[name]) return false;
    // A context can start suspended until the page has been interacted
    // with; resuming here is safe because we only get called from a click.
    if (ac.state === "suspended" && ac.resume) { ac.resume(); }

    var master = ac.createGain();
    master.gain.value = CEILING * (volume || 1);
    master.connect(ac.destination);
    try { VOICES[name](ac, master); } catch (e) { return false; }
    return true;
  }

  try {
    enabled = global.localStorage &&
              global.localStorage.getItem(STORAGE_KEY) === "on";
  } catch (e) { enabled = false; }

  function persist() {
    try { global.localStorage.setItem(STORAGE_KEY, enabled ? "on" : "off"); }
    catch (e) { /* private mode: session-only preference, still fine */ }
  }

  function load(name) {
    if (cache[name] !== undefined) return cache[name];
    var entry = MANIFEST[name];
    if (!entry || typeof global.Audio !== "function") {
      cache[name] = null;
      return null;
    }
    var el = new global.Audio();
    el.preload = "none";
    el.src = BASE + entry.file;
    el.volume = CEILING * (entry.volume || 1);
    // If the clip is missing or undecodable, drop it and let the
    // synthesised voice cover the cue from here on.
    el.addEventListener("error", function () { cache[name] = null; });
    cache[name] = el;
    return el;
  }

  var Foley = {
    manifest: MANIFEST,

    isEnabled: function () { return enabled; },

    /** Whether any clip has actually loaded (vs. falling back to the synth). */
    hasAssets: function () {
      var name;
      for (name in cache) { if (cache[name]) return true; }
      return false;
    },

    /** Whether this browser can synthesise at all (Web Audio present). */
    canSynthesise: function () {
      return !!(global.AudioContext || global.webkitAudioContext);
    },

    set: function (on) {
      enabled = !!on;
      persist();
      // Fetch the clips on enable rather than on first cue, so the first
      // sound is not a beat late. This follows a click, never page load.
      if (enabled) {
        var name;
        for (name in MANIFEST) {
          var el = load(name);
          if (el) { el.preload = "auto"; try { el.load(); } catch (e) {} }
        }
      }
      listeners.forEach(function (fn) { fn(enabled); });
      return enabled;
    },

    toggle: function () { return Foley.set(!enabled); },

    onChange: function (fn) { listeners.push(fn); fn(enabled); },

    /** Fire a cue. Silent (and harmless) while off.
     *
     *  A committed recording takes the cue if one exists; otherwise the
     *  synthesised voice plays. Either way a failure is silence. */
    play: function (name) {
      if (!enabled) return;

      var el = load(name);
      if (el) {
        try {
          el.currentTime = 0;
          var p = el.play();
          if (p && typeof p.catch === "function") {
            // A 404'd or undecodable file falls through to the synth.
            p.catch(function () { synth(name, (MANIFEST[name] || {}).volume); });
          }
          return;
        } catch (e) { /* fall through to the synth */ }
      }

      synth(name, (MANIFEST[name] || {}).volume);
    }
  };

  global.Nescience = global.Nescience || {};
  global.Nescience.foley = Foley;
})(window);
