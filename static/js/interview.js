// ==========================================================
// NESCIENCE — interview stepper
// One question at a time. Collects answers, posts them, then
// renders the leads returned by the evidence matcher.
// ==========================================================

(function () {
  var stage = document.getElementById("stage");
  var steps = Array.prototype.slice.call(stage.querySelectorAll(".step"));
  var postUrl = JSON.parse(document.getElementById("post-url").textContent);

  // Steps that count toward the visible progress bar: the questions + seal.
  var counted = steps.filter(function (s) {
    var name = s.getAttribute("data-step");
    return name !== "intro" && name !== "done";
  });

  var current = 0;

  function show(index) {
    if (index < 0 || index >= steps.length) return;
    steps[current].classList.remove("active");
    current = index;
    steps[current].classList.add("active");
    window.scrollTo({ top: 0, behavior: "smooth" });

    var focusable = steps[current].querySelector("textarea, input[type=text]");
    if (focusable) setTimeout(function () { focusable.focus(); }, 60);

    updateProgress();
  }

  function updateProgress() {
    var step = steps[current];
    var name = step.getAttribute("data-step");
    var label = document.getElementById("progress-label");
    var count = document.getElementById("progress-count");
    var fill = document.getElementById("progress-fill");

    if (name === "done") {
      label.textContent = "Filed";
      count.textContent = "";
      fill.style.width = "100%";
      return;
    }

    var pos = counted.indexOf(step); // -1 for intro
    var total = counted.length;
    if (pos < 0) {
      label.textContent = "Intake";
      count.textContent = "";
      fill.style.width = "2%";
    } else {
      var module = step.getAttribute("data-module");
      label.textContent = module || "Intake";
      count.textContent = String(pos + 1).padStart(2, "0") + " / " + String(total).padStart(2, "0");
      fill.style.width = ((pos + 1) / total) * 100 + "%";
    }
  }

  function collect() {
    var payload = { "Participant Information": {} };

    stage.querySelectorAll("[data-field]").forEach(function (input) {
      payload["Participant Information"][input.getAttribute("data-field")] = input.value.trim();
    });

    stage.querySelectorAll("textarea[data-module]").forEach(function (ta) {
      var module = ta.getAttribute("data-module");
      var key = ta.getAttribute("data-key");
      if (!payload[module]) payload[module] = {};
      payload[module][key] = ta.value.trim();
    });

    return payload;
  }

  function renderLeads(matches) {
    var box = document.getElementById("leads");
    box.innerHTML = "";

    if (!matches || !matches.length) {
      var empty = document.createElement("div");
      empty.className = "lead";
      empty.innerHTML =
        '<div class="stamp" style="transform:none">Inconclusive</div>' +
        '<p class="qmark" style="margin-top:14px">The account did not resolve onto a mapped concept. ' +
        "Sometimes the record simply reads: UNKNOWN.</p>";
      box.appendChild(empty);
      return;
    }

    box.className = "grid grid-2";
    matches.forEach(function (m) {
      var el = document.createElement("div");
      el.className = "lead";

      var chips = (m.evidence || [])
        .map(function (e) { return '<span class="chip">' + escapeHtml(e) + "</span>"; })
        .join("");

      var qmark = m.unresolved
        ? '<p class="qmark">Still unknown: ' + escapeHtml(m.unresolved) + "</p>"
        : "";

      var stub = m.defined ? "" : ' <span class="tag tag-unknown" style="font-size:9px">Not yet investigated</span>';

      el.innerHTML =
        '<h4>' + escapeHtml(m.concept) + stub + "</h4>" +
        '<div class="score">Signal strength · ' + Number(m.score).toFixed(0) + "</div>" +
        '<div class="chips">' + chips + "</div>" +
        qmark +
        '<div style="margin-top:12px"><a href="/atlas/' + encodeURIComponent(m.concept) + '">Open concept file →</a></div>';
      box.appendChild(el);
    });
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function submit() {
    var btn = document.getElementById("submit-btn");
    var err = document.getElementById("submit-error");
    err.style.display = "none";
    btn.disabled = true;
    btn.textContent = "Filing…";

    fetch(postUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(collect()),
    })
      .then(function (r) {
        if (!r.ok) throw new Error("The bureau could not file the case.");
        return r.json();
      })
      .then(function (data) {
        document.getElementById("done-number").textContent = data.case_number;
        document.getElementById("view-case").setAttribute("href", data.archive_url);
        renderLeads(data.matches);
        show(steps.indexOf(stage.querySelector('[data-step="done"]')));
      })
      .catch(function (e) {
        btn.disabled = false;
        btn.textContent = "Seal & file the case →";
        err.textContent = e.message || "Something went wrong. Please try again.";
        err.style.display = "block";
      });
  }

  // Wiring
  stage.querySelectorAll("[data-advance]").forEach(function (b) {
    b.addEventListener("click", function () { show(current + 1); });
  });
  stage.querySelectorAll("[data-back]").forEach(function (b) {
    b.addEventListener("click", function () { show(current - 1); });
  });
  document.getElementById("submit-btn").addEventListener("click", submit);

  // Ctrl/Cmd+Enter advances from a textarea.
  stage.addEventListener("keydown", function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
      var adv = steps[current].querySelector("[data-advance]");
      if (adv) { e.preventDefault(); adv.click(); }
    }
  });

  updateProgress();
})();
