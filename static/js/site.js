// Progressive enhancements. Everything works without this file:
// - the mobile menu is a <details> (here: Escape, outside click, link click and resize close it);
// - header dropdowns (details[data-dropdown]) close on Escape and outside click;
// - [data-tabs]: without JS every panel shows and the switcher links jump to them; here they
//   become real tabs (roles, arrow keys, Home/End, #hash and ?platform= selection).
(function () {
  "use strict";
  var doc = document;

  // Close a <details> on Escape (focus back on its summary) and on a click outside it and `panel`.
  function dismissable(details, panel) {
    var summary = details.querySelector("summary");
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && details.open) {
        details.open = false;
        if (summary) summary.focus();
      }
    });
    doc.addEventListener("click", function (e) {
      if (!details.open || details.contains(e.target) || (panel && panel.contains(e.target))) return;
      details.open = false;
    });
  }

  // Mobile menu: CSS shows the panel next to details.menu[open]; the summary's own expanded
  // state is announced natively.
  var menu = doc.querySelector("[data-menu]");
  if (menu) {
    var summary = menu.querySelector("summary");
    var panel = doc.getElementById(summary.getAttribute("aria-controls"));
    dismissable(menu, panel);
    if (panel) {
      panel.addEventListener("click", function (e) {
        if (e.target.closest && e.target.closest("a")) menu.open = false;
      });
    }
    if (window.matchMedia) {
      var wide = matchMedia("(min-width: 1024px)");
      var onWide = function () { if (wide.matches) menu.open = false; };
      if (wide.addEventListener) wide.addEventListener("change", onWide); else if (wide.addListener) wide.addListener(onWide);
    }
  }

  // Dropdowns (language menu). Its panel scrolls inside itself: show the current language when it opens.
  doc.querySelectorAll("details[data-dropdown]").forEach(function (details) {
    dismissable(details);
    details.addEventListener("toggle", function () {
      var current = details.open && details.querySelector('[aria-current="true"]');
      var panel = current && current.closest(".lang-menu__panel");
      if (!panel || panel.scrollHeight <= panel.clientHeight) return;
      var offset = current.getBoundingClientRect().top - panel.getBoundingClientRect().top;
      panel.scrollTop += offset - (panel.clientHeight - current.offsetHeight) / 2;
    });
  });

  // Tabs.
  doc.querySelectorAll("[data-tabs]").forEach(function (box, n) {
    var list = box.querySelector("[data-tabs-list]");
    if (!list) return;
    var tabs = Array.prototype.slice.call(list.querySelectorAll("[data-tab]"));
    var panels = tabs.map(function (tab) { return box.querySelector('[data-tab-panel="' + tab.dataset.tab + '"]'); });
    if (!tabs.length || panels.indexOf(null) !== -1) return;

    list.setAttribute("role", "tablist");
    tabs.forEach(function (tab, i) {
      var panel = panels[i];
      tab.setAttribute("role", "tab");
      if (!tab.id) tab.id = "tab-" + n + "-" + tab.dataset.tab;
      tab.setAttribute("aria-controls", panel.id);
      panel.setAttribute("role", "tabpanel");
      panel.setAttribute("aria-labelledby", tab.id);
      panel.tabIndex = 0;
      tab.addEventListener("click", function (e) {
        e.preventDefault();
        select(i, false);
        if (history.replaceState) history.replaceState(null, "", "#" + panel.id);
      });
      tab.addEventListener("keydown", function (e) {
        var to = null;
        var rtl = getComputedStyle(list).direction === "rtl";
        if (e.key === "ArrowRight") to = rtl ? i - 1 : i + 1;
        else if (e.key === "ArrowLeft") to = rtl ? i + 1 : i - 1;
        else if (e.key === "Home") to = 0;
        else if (e.key === "End") to = tabs.length - 1;
        if (to === null) return;
        e.preventDefault();
        select((to + tabs.length) % tabs.length, true);
      });
    });

    function select(index, focus) {
      tabs.forEach(function (tab, i) {
        var on = i === index;
        tab.setAttribute("aria-selected", on ? "true" : "false");
        tab.tabIndex = on ? 0 : -1;
        tab.classList.toggle("is-active", on);
        panels[i].classList.toggle("is-active", on);
        panels[i].hidden = !on;
      });
      if (focus) tabs[index].focus();
    }

    // Start on the tab named by the #hash, else the one the server marked active.
    var start = 0;
    tabs.forEach(function (tab, i) { if (tab.classList.contains("is-active")) start = i; });
    var hash = location.hash.slice(1);
    panels.forEach(function (panel, i) { if (hash && panel.id === hash) start = i; });
    select(start, false);
  });
})();
