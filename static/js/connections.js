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
    n.addEventListener("mouseenter", function () { focus(name); });
    n.addEventListener("focus", function () { focus(name); });
    n.addEventListener("mouseleave", clear);
    n.addEventListener("blur", clear);
  });
})();
