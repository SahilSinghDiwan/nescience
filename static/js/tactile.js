// ==========================================================
// NESCIENCE — the tactile layer (NESC-15)
//
// Five behaviours, each modelling a real material:
//   1. the vault lamp — a pool of light that lags the pointer
//      (weight, drag, easing; never an instant snap),
//   2. evidence cards that land askew and lock square,
//   3. parchment sheets you can pick up by the brass clip and
//      let go of — they spring back and seat with a soft lock,
//   4. redacted ink that dissolves under the cursor,
//   5. marginalia that warms as the nib passes over it.
//
// Non-negotiables, enforced below rather than documented:
//   * prefers-reduced-motion turns every one of them into a
//     static state — nothing animates, nothing follows,
//   * nothing here gates content: every affordance is an
//     enhancement over markup that already reads without it,
//   * everything interactive is a real button, keyboard
//     operable, with a visible focus ring,
//   * no library, no network, no CDN.
// ==========================================================

(function () {
  "use strict";

  var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
  var fine = window.matchMedia ? window.matchMedia("(pointer: fine)") : null;
  function reduced() { return !!(mq && mq.matches); }
  function finePointer() { return !fine || fine.matches; }

  var foley = (window.Nescience && window.Nescience.foley) || { play: function () {}, onChange: function () {}, toggle: function () { return false; }, isEnabled: function () { return false; } };

  function each(sel, fn, root) {
    var list = (root || document).querySelectorAll(sel);
    Array.prototype.forEach.call(list, fn);
  }

  // --------------------------------------------------------
  // 1. The vault lamp — cursor physics
  // --------------------------------------------------------
  function mountLamp() {
    if (reduced() || !finePointer()) return;

    var lamp = document.createElement("div");
    lamp.className = "vault-lamp";
    lamp.setAttribute("aria-hidden", "true");
    document.body.appendChild(lamp);

    var tx = window.innerWidth / 2, ty = window.innerHeight / 2;
    var x = tx, y = ty, running = false;

    // Heavier than the cursor: the light is dragged, not carried.
    var EASE = 0.085;

    function frame() {
      var dx = tx - x, dy = ty - y;
      x += dx * EASE;
      y += dy * EASE;
      lamp.style.transform = "translate3d(" + x.toFixed(2) + "px," + y.toFixed(2) + "px,0)";
      if (Math.abs(dx) < 0.35 && Math.abs(dy) < 0.35) { running = false; return; }
      requestAnimationFrame(frame);
    }
    function kick() { if (!running) { running = true; requestAnimationFrame(frame); } }

    document.addEventListener("pointermove", function (e) {
      if (e.pointerType !== "mouse") return;
      tx = e.clientX; ty = e.clientY;
      lamp.classList.add("lit");
      kick();
    }, { passive: true });

    document.addEventListener("pointerdown", function () { lamp.classList.add("pressed"); }, { passive: true });
    document.addEventListener("pointerup", function () { lamp.classList.remove("pressed"); }, { passive: true });
    document.addEventListener("pointerleave", function () { lamp.classList.remove("lit"); }, { passive: true });
  }

  // --------------------------------------------------------
  // 2. Evidence cards snapping into place
  // --------------------------------------------------------
  var CARD_SELECTOR = ".lead, .atlas-card, .entrance, .drawer, .tier, .refcard, .openq";

  function mountSnap() {
    var cards = Array.prototype.slice.call(document.querySelectorAll(CARD_SELECTOR));
    if (!cards.length) return;

    if (reduced() || !("IntersectionObserver" in window)) return; // markup is already square

    cards.forEach(function (el, i) {
      // alternate the angle so a stack looks hand-filed, not machined
      el.style.setProperty("--snap-rot", (i % 2 ? 1 : -1) * (0.7 + (i % 3) * 0.35) + "deg");
      el.classList.add("snap");
    });

    var seated = 0;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        io.unobserve(el);
        var delay = Math.min(entry.boundingClientRect.top > 0 ? seated++ % 6 : 0, 6) * 55;
        setTimeout(function () {
          seat(el);
        }, delay);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.01 });

    cards.forEach(function (el) { io.observe(el); });

    // Safety net: whatever has not been seen in two seconds is
    // seated anyway. A card must never be left invisible.
    setTimeout(function () {
      cards.forEach(function (el) {
        if (el.classList.contains("snap")) { io.unobserve(el); seat(el); }
      });
    }, 2000);
  }

  // Seat a card square and hand its transform back to the
  // stylesheet, so hover states are not held hostage by the
  // snap-in transform.
  function seat(el) {
    if (!el.classList.contains("snap")) return;
    var done = false;
    function finish() {
      if (done) return;
      done = true;
      el.removeEventListener("transitionend", onEnd);
      el.classList.remove("snap", "snapped");
      el.style.removeProperty("--snap-rot");
      lock(el);
    }
    function onEnd(ev) { if (ev.propertyName === "transform") finish(); }
    el.addEventListener("transitionend", onEnd);
    el.classList.add("snapped");
    setTimeout(finish, 900);
  }

  function lock(el, withSound) {
    el.classList.remove("locked");
    // reflow so the animation can restart on a repeat seat
    void el.offsetWidth;
    el.classList.add("locked");
    setTimeout(function () { el.classList.remove("locked"); }, 340);
    if (withSound) foley.play("snap");
  }

  // --------------------------------------------------------
  // 3. Parchment sheets: pick up by the clip, let go, it seats
  // --------------------------------------------------------
  function mountSheets() {
    each("[data-sheet]", function (sheet) {
      var grip = sheet.querySelector("[data-grip]");
      if (!grip) return;

      var state = {
        // where the sheet is, where the hand wants it
        x: 0, y: 0, tx: 0, ty: 0,
        vx: 0, vy: 0, rot: 0,
        dragging: false, running: false, id: null
      };

      function paint() {
        if (state.x === 0 && state.y === 0 && state.rot === 0) {
          sheet.style.transform = "";
          return;
        }
        sheet.style.transform =
          "translate3d(" + state.x.toFixed(2) + "px," + state.y.toFixed(2) + "px,0) rotate(" + state.rot.toFixed(2) + "deg)";
      }

      function run() {
        if (state.running) return;
        state.running = true;
        requestAnimationFrame(step);
      }

      function step() {
        if (state.dragging) {
          // the sheet trails the hand — paper has mass and friction
          var dx = state.tx - state.x, dy = state.ty - state.y;
          state.x += dx * 0.17;
          state.y += dy * 0.17;
          state.rot += ((dx * 0.035) - state.rot) * 0.12;   // leans into the pull
          paint();
          requestAnimationFrame(step);
          return;
        }
        // released: a damped spring back into the file
        var K = 0.16, D = 0.74;
        state.vx = (state.vx - state.x * K) * D;
        state.vy = (state.vy - state.y * K) * D;
        state.x += state.vx;
        state.y += state.vy;
        state.rot += (0 - state.rot) * 0.22;
        paint();

        var still = Math.abs(state.x) < 0.4 && Math.abs(state.y) < 0.4 &&
                    Math.abs(state.vx) < 0.4 && Math.abs(state.vy) < 0.4 &&
                    Math.abs(state.rot) < 0.05;
        if (still) {
          state.x = state.y = state.vx = state.vy = state.rot = 0;
          paint();
          state.running = false;
          sheet.classList.remove("returning");
          lock(sheet, true);                 // the soft mechanical lock
          return;
        }
        requestAnimationFrame(step);
      }

      function release() {
        if (!state.dragging) return;
        state.dragging = false;
        sheet.classList.remove("dragging");
        sheet.classList.add("returning");
        grip.setAttribute("aria-pressed", "false");
        if (reduced()) {
          state.x = state.y = state.rot = 0;
          paint();
          sheet.classList.remove("returning");
          foley.play("snap");
          return;
        }
        run();
      }

      grip.addEventListener("pointerdown", function (e) {
        if (reduced()) return;
        e.preventDefault();
        state.dragging = true;
        state.id = e.pointerId;
        state.ox = e.clientX - state.x;
        state.oy = e.clientY - state.y;
        sheet.classList.add("dragging");
        sheet.classList.remove("returning");
        grip.setAttribute("aria-pressed", "true");
        try { grip.setPointerCapture(e.pointerId); } catch (err) {}
        foley.play("sheet-slide");
        run();
      });

      grip.addEventListener("pointermove", function (e) {
        if (!state.dragging || e.pointerId !== state.id) return;
        state.tx = e.clientX - state.ox;
        state.ty = e.clientY - state.oy;
      });

      ["pointerup", "pointercancel", "lostpointercapture"].forEach(function (ev) {
        grip.addEventListener(ev, release);
      });

      // Keyboard: the same handling, without a pointer.
      grip.addEventListener("keydown", function (e) {
        var STEP = 14, moved = true;
        switch (e.key) {
          case "ArrowLeft":  state.x -= STEP; break;
          case "ArrowRight": state.x += STEP; break;
          case "ArrowUp":    state.y -= STEP; break;
          case "ArrowDown":  state.y += STEP; break;
          case "Escape":
          case "Enter":
          case " ":
            state.dragging = false;
            if (reduced()) { state.x = state.y = state.rot = 0; paint(); foley.play("snap"); }
            else { sheet.classList.add("returning"); run(); }
            break;
          default: moved = false;
        }
        if (!moved) return;
        e.preventDefault();
        if (e.key.indexOf("Arrow") === 0) {
          state.rot = Math.max(-3, Math.min(3, state.x * 0.02));
          paint();
        }
      });

      grip.addEventListener("blur", function () {
        if (state.x || state.y) {
          if (reduced()) { state.x = state.y = state.rot = 0; paint(); }
          else { sheet.classList.add("returning"); run(); }
        }
      });
    });
  }

  // --------------------------------------------------------
  // 4. Redactions that dissolve
  // --------------------------------------------------------
  function mountRedactions() {
    each(".redacted", function (el) {
      // hover + focus are handled in CSS; this is the touch/click path
      var fired = false;
      el.addEventListener("click", function () {
        el.classList.toggle("dissolved");
        el.setAttribute("aria-expanded", el.classList.contains("dissolved") ? "true" : "false");
        foley.play("ink");
      });
      el.addEventListener("pointerenter", function () {
        if (fired) return;
        fired = true;
        foley.play("ink");
        setTimeout(function () { fired = false; }, 1200);
      });
    });
  }

  // --------------------------------------------------------
  // 5. Marginalia warming under the nib
  // --------------------------------------------------------
  function mountMarginalia() {
    if (reduced() || !finePointer()) return;
    var notes = Array.prototype.slice.call(document.querySelectorAll(".marginalia"));
    if (!notes.length) return;

    var RADIUS = 260;
    var px = -9999, py = -9999, queued = false;

    function measure() {
      queued = false;
      notes.forEach(function (n) {
        var r = n.getBoundingClientRect();
        if (r.bottom < -200 || r.top > window.innerHeight + 200) {
          n.style.setProperty("--glow", "0");
          return;
        }
        var cx = Math.max(r.left, Math.min(px, r.right));
        var cy = Math.max(r.top, Math.min(py, r.bottom));
        var d = Math.hypot(px - cx, py - cy);
        var g = d >= RADIUS ? 0 : Math.pow(1 - d / RADIUS, 1.7);
        n.style.setProperty("--glow", g.toFixed(3));
      });
    }

    document.addEventListener("pointermove", function (e) {
      if (e.pointerType !== "mouse") return;
      px = e.clientX; py = e.clientY;
      if (!queued) { queued = true; requestAnimationFrame(measure); }
    }, { passive: true });
  }

  // --------------------------------------------------------
  // 6. Ambient audio toggle — visible, labelled, OFF by default
  //    Cues are synthesised at runtime; see static/audio/README.md
  // --------------------------------------------------------
  function mountAudioToggle() {
    var slot = document.querySelector("[data-audio-slot]");
    if (!slot) return;

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "audio-toggle";
    btn.setAttribute("aria-pressed", "false");
    btn.innerHTML = '<span class="lamp" aria-hidden="true"></span><span class="audio-label"></span>';
    var label = btn.querySelector(".audio-label");

    function render(on) {
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      label.textContent = on ? "Ambient audio · on" : "Ambient audio · off";
      btn.title = on
        ? "Ambient analog audio is on (quiet) — paper, ink and the clip."
        : "Ambient analog audio is off. Turn on for quiet paper and pen sounds.";
      btn.setAttribute("aria-label", label.textContent);
    }

    foley.onChange(render);
    btn.addEventListener("click", function () {
      // Turning it on plays one cue immediately. Without it the control
      // gives no evidence it did anything — the next sound waits on a card
      // being dragged, which reads as a broken toggle.
      if (foley.toggle()) foley.play("drawer");
    });
    slot.appendChild(btn);
  }

  function boot() {
    mountAudioToggle();
    mountRedactions();
    mountSheets();
    mountSnap();
    mountMarginalia();
    mountLamp();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
