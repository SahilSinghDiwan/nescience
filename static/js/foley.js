// ==========================================================
// NESCIENCE — foley hook (NESC-15)
//
// The ambient analog layer: paper slides, pen scratches, the
// soft snap of a clip. NO AUDIO SHIPS WITH THIS BUILD — the
// assets have not been sourced yet. This module is the empty
// socket they plug into:
//
//   1. drop files into /static/audio using the names in
//      MANIFEST below (any of .mp3/.ogg/.wav — set the name),
//   2. nothing else changes; the toggle already exists and the
//      call sites already fire Foley.play("snap") etc.
//
// Rules kept here so they cannot be forgotten later:
//   * muted by default, always — the toggle starts OFF and only
//     a deliberate click (persisted in localStorage) turns it on,
//   * never autoplay: the first sound can only follow a user
//     gesture, because nothing plays while disabled,
//   * quiet: a hard volume ceiling, well under conversational,
//   * a missing asset is silence, never an error.
// ==========================================================

(function (global) {
  "use strict";

  var STORAGE_KEY = "nescience.foley";
  var CEILING = 0.22;              // hard quiet ceiling
  var BASE = "/static/audio/";

  // name -> { file, volume }. Files are intentionally absent.
  var MANIFEST = {
    "sheet-slide": { file: "sheet-slide.mp3", volume: 0.7 },  // paper dragged across the desk
    "snap":        { file: "clip-snap.mp3",   volume: 1.0 },  // a card seating under the clip
    "ink":         { file: "pen-scratch.mp3", volume: 0.6 },  // redaction dissolving
    "drawer":      { file: "drawer.mp3",      volume: 0.8 }   // a folder pulled open
  };

  var cache = {};
  var enabled = false;
  var listeners = [];

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
    // A 404 (the current state of every asset) resolves to silence.
    el.addEventListener("error", function () { cache[name] = null; });
    cache[name] = el;
    return el;
  }

  var Foley = {
    manifest: MANIFEST,

    isEnabled: function () { return enabled; },

    /** Any asset actually on disk? Today: no. */
    hasAssets: function () {
      var name;
      for (name in cache) { if (cache[name]) return true; }
      return false;
    },

    set: function (on) {
      enabled = !!on;
      persist();
      listeners.forEach(function (fn) { fn(enabled); });
      return enabled;
    },

    toggle: function () { return Foley.set(!enabled); },

    onChange: function (fn) { listeners.push(fn); fn(enabled); },

    /** Fire a cue. Silent (and harmless) while off or unsourced. */
    play: function (name) {
      if (!enabled) return;
      var el = load(name);
      if (!el) return;
      try {
        el.currentTime = 0;
        var p = el.play();
        if (p && typeof p.catch === "function") { p.catch(function () {}); }
      } catch (e) { /* silence beats a console full of noise */ }
    }
  };

  global.Nescience = global.Nescience || {};
  global.Nescience.foley = Foley;
})(window);
