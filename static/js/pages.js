// Money pages on phones: once the hero's buttons scroll out of view, a slim bar keeps the
// preselected package one tap away; it steps aside again at the packages and at the closing
// call to action. Without IntersectionObserver (or JS) the bar simply stays hidden.
(function () {
  var bar = document.querySelector("[data-pg-sticky]");
  var hero = document.querySelector("[data-pg-hero]");
  if (!bar || !hero || !("IntersectionObserver" in window)) return;
  var blockers = Array.prototype.slice.call(document.querySelectorAll("#packages, [data-pg-end], .site-footer"));
  var heroGone = false;
  var inView = new Set();

  function update() {
    var show = heroGone && inView.size === 0;
    bar.classList.toggle("is-shown", show);
    bar.inert = !show;
    bar.setAttribute("aria-hidden", show ? "false" : "true");
  }

  bar.hidden = false;
  bar.inert = true;
  bar.setAttribute("aria-hidden", "true");

  new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      // Gone means scrolled past (above the viewport), not "not reached yet".
      heroGone = !entry.isIntersecting && entry.boundingClientRect.top < 0;
    });
    update();
  }).observe(hero);

  var watcher = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) inView.add(entry.target); else inView.delete(entry.target);
    });
    update();
  });
  blockers.forEach(function (el) { watcher.observe(el); });
})();

// Free tools (templates/pages/_tool.html): computed in the browser, nothing is sent.
(function () {
  var fmt = function (n) { return new Intl.NumberFormat(document.documentElement.lang || "en").format(n); };
  var num = function (form, name) { var v = parseFloat((form.elements[name] || {}).value); return isFinite(v) ? v : NaN; };

  var engagement = document.querySelector('[data-tool="engagement"]');
  if (engagement) {
    engagement.addEventListener("submit", function (e) {
      e.preventDefault();
      var followers = num(engagement, "followers"), likes = num(engagement, "likes"), comments = num(engagement, "comments") || 0;
      var out = engagement.querySelector("output");
      if (!(followers > 0) || !(likes >= 0)) { out.hidden = true; return; }
      var rate = (likes + comments) / followers * 100;
      out.textContent = out.dataset.template.replace("{rate}", new Intl.NumberFormat(document.documentElement.lang || "en", { maximumFractionDigits: 2 }).format(rate));
      out.hidden = false;
    });
  }

  var growth = document.querySelector('[data-tool="growth"]');
  var plansEl = document.getElementById("pg-tool-plans");
  if (growth && plansEl) {
    var plans = JSON.parse(plansEl.textContent);
    growth.addEventListener("submit", function (e) {
      e.preventDefault();
      var current = num(growth, "current") || 0, goal = num(growth, "goal");
      var box = growth.querySelector(".pg-tool__result");
      if (!(goal > 0)) { box.hidden = true; return; }
      box.textContent = "";
      var gap = goal - current;
      if (gap <= 0) { box.textContent = box.dataset.reached; box.hidden = false; return; }
      var list = document.createElement("ul");
      list.className = "pg-tool__plans";
      plans.forEach(function (p) {
        var fast = Math.max(Math.ceil(gap / p.high), 1), slow = Math.max(Math.ceil(gap / p.low), 1);
        var when = slow === 1 ? box.dataset.first
          : fast === slow ? box.dataset.about.replace("{n}", fmt(slow))
          : box.dataset.range.replace("{low}", fmt(fast)).replace("{high}", fmt(slow));
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = p.url; a.textContent = p.name;
        li.appendChild(a);
        li.appendChild(document.createTextNode(": " + when));
        list.appendChild(li);
      });
      box.appendChild(list);
      box.hidden = false;
    });
  }
})();
