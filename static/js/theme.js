// Light / dark: follows the system until the visitor picks one; the choice is remembered.
// The early inline script in base.html applies a saved choice before the first paint.
(function () {
  var root = document.documentElement;
  var COLORS = { light: "#FAF9FF", dark: "#0F0D1F" };
  var system = window.matchMedia ? matchMedia("(prefers-color-scheme: dark)") : null;

  function current() {
    if (root.dataset.theme) return root.dataset.theme;
    return system && system.matches ? "dark" : "light";
  }

  function sync() {
    var theme = current();
    document.querySelectorAll("[data-theme-toggle]").forEach(function (button) {
      button.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    });
    // A picked theme overrides the system one: make the browser UI match it.
    if (root.dataset.theme) {
      document.querySelectorAll('meta[name="theme-color"]').forEach(function (meta) {
        meta.setAttribute("content", COLORS[theme]);
      });
    }
  }

  document.querySelectorAll("[data-theme-toggle]").forEach(function (button) {
    button.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try { localStorage.setItem("theme", next); } catch (e) {}
      sync();
    });
  });
  if (system) {
    if (system.addEventListener) system.addEventListener("change", sync);
    else if (system.addListener) system.addListener(sync);
  }
  sync();
})();
