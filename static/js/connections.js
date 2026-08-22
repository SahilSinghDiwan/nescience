// ==========================================================
// NESCIENCE — Connections corkboard (NESC-12)
// Hover / focus a pinned concept to light its threads and its
// neighbours, and dim the rest. Pure highlighting — no physics,
// no motion — so it degrades gracefully and respects
// prefers-reduced-motion by construction. Clicking a card is a
// normal link into that concept's case file.
// ==========================================================

(function () {
  var board = document.querySelector(".corkboard-svg");
  if (!board) return;

  var threads = Array.prototype.slice.call(board.querySelectorAll(".thread"));
  var nodes = Array.prototype.slice.call(board.querySelectorAll(".node"));

  function clear() {
    board.classList.remove("focused");
    threads.forEach(function (t) { t.classList.remove("lit", "dim"); });
    nodes.forEach(function (n) { n.classList.remove("neighbour", "dim"); });
  }

  function focus(name) {
    board.classList.add("focused");
    var linked = {};
    linked[name] = true;

    threads.forEach(function (t) {
      var a = t.getAttribute("data-a");
      var b = t.getAttribute("data-b");
      if (a === name || b === name) {
        t.classList.add("lit");
        t.classList.remove("dim");
        linked[a] = true;
        linked[b] = true;
      } else {
        t.classList.add("dim");
        t.classList.remove("lit");
      }
    });

    nodes.forEach(function (n) {
      var nm = n.getAttribute("data-name");
      if (nm === name) {
        n.classList.remove("dim");
        n.classList.add("neighbour");
      } else if (linked[nm]) {
        n.classList.remove("dim");
        n.classList.add("neighbour");
      } else {
        n.classList.add("dim");
        n.classList.remove("neighbour");
      }
    });
  }

  nodes.forEach(function (n) {
    var name = n.getAttribute("data-name");
    n.addEventListener("mouseenter", function () { focus(name); tension(); });
    n.addEventListener("focus", function () { focus(name); tension(); });
    n.addEventListener("mouseleave", function () { clear(); tension(); });
    n.addEventListener("blur", function () { clear(); tension(); });
  });

  // ----------------------------------------------------------
  // String physics (NESC-15): threads sag, lit threads pull taut
  // ----------------------------------------------------------
  var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
  var strings = [];

  function slackFor(x1, y1, x2, y2) {
    var len = Math.hypot(x2 - x1, y2 - y1);
    return Math.min(34, 6 + len * 0.055);   // longer string, deeper sag
  }

  function d(s, sag) {
    var mx = (s.x1 + s.x2) / 2;
    var my = (s.y1 + s.y2) / 2;
    return "M" + s.x1 + " " + s.y1 + " Q" + mx.toFixed(1) + " " + (my + sag).toFixed(1) +
           " " + s.x2 + " " + s.y2;
  }

  // Swap every <line class="thread"> for an equivalent sagging path.
  threads.forEach(function (line) {
    var x1 = parseFloat(line.getAttribute("x1"));
    var y1 = parseFloat(line.getAttribute("y1"));
    var x2 = parseFloat(line.getAttribute("x2"));
    var y2 = parseFloat(line.getAttribute("y2"));
    if (isNaN(x1) || isNaN(y1) || isNaN(x2) || isNaN(y2)) return;

    var path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("class", line.getAttribute("class") || "thread");
    path.setAttribute("data-a", line.getAttribute("data-a"));
    path.setAttribute("data-b", line.getAttribute("data-b"));

    var s = { el: path, x1: x1, y1: y1, x2: x2, y2: y2, sag: 0, target: 0 };
    s.slack = slackFor(x1, y1, x2, y2);
    s.sag = s.target = s.slack;
    path.setAttribute("d", d(s, s.sag));

    line.parentNode.replaceChild(path, line);
    strings.push(s);
  });

  // keep the highlight logic pointing at the new elements
  threads = strings.map(function (s) { return s.el; });

  var animating = false;

  function stepTension() {
    var moving = false;
    strings.forEach(function (s) {
      var diff = s.target - s.sag;
      if (Math.abs(diff) < 0.15) {
        if (s.sag !== s.target) { s.sag = s.target; s.el.setAttribute("d", d(s, s.sag)); }
        return;
      }
      s.sag += diff * 0.18;
      s.el.setAttribute("d", d(s, s.sag));
      moving = true;
    });
    if (moving) { requestAnimationFrame(stepTension); } else { animating = false; }
  }

  function tension() {
    strings.forEach(function (s) {
      // a thread the investigation is following is pulled tight
      s.target = s.el.classList.contains("lit") ? s.slack * 0.22 : s.slack;
    });
    if (mq && mq.matches) {
      strings.forEach(function (s) { s.sag = s.target; s.el.setAttribute("d", d(s, s.sag)); });
      return;
    }
    if (!animating) { animating = true; requestAnimationFrame(stepTension); }
  }
})();
