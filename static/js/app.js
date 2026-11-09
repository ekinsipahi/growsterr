// Growth pages (order, success, account). Progressive: every page works without this file.
(function () {
  "use strict";
  var doc = document.documentElement;

  // Analytics stays optional: events go to gtag / dataLayer only when a tag is on the page.
  function track(name, params) {
    try {
      if (typeof window.gtag === "function") window.gtag("event", name, params || {});
      else if (Array.isArray(window.dataLayer)) window.dataLayer.push(Object.assign({ event: name }, params || {}));
    } catch (e) { /* never break the page for analytics */ }
  }
  function readJSON(id) {
    var el = document.getElementById(id);
    if (!el) return null;
    try { return JSON.parse(el.textContent); } catch (e) { return null; }
  }
  function withUserData(name, data) {
    if (!data) return;
    if (data.user_data && typeof window.gtag === "function") window.gtag("set", "user_data", data.user_data);
    delete data.user_data;
    track(name, data);
  }

  // First-touch attribution (UTM + gclid), remembered for the order form.
  var ATTR = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "gclid"];
  var params = new URLSearchParams(location.search);
  var stored = {};
  try { stored = JSON.parse(localStorage.getItem("growsterr_utm") || "{}") || {}; } catch (e) { stored = {}; }
  if (ATTR.some(function (k) { return params.get(k); }) && !stored.utm_source && !stored.gclid) {
    ATTR.forEach(function (k) { stored[k] = params.get(k) || ""; });
    if (stored.gclid && !stored.utm_source) { stored.utm_source = "google"; stored.utm_medium = "cpc"; }
    stored.landing = location.pathname;
    try { localStorage.setItem("growsterr_utm", JSON.stringify(stored)); } catch (e) { /* storage blocked */ }
  }
  // First touch of every visitor, UTM or not: the first page, the outside site that sent them
  // ("google.com"; "" = typed in or an app) and when. Kept until an order carries it.
  var first = null;
  try { first = JSON.parse(localStorage.getItem("growsterr_first") || "null"); } catch (e) { first = null; }
  if (!first) {
    var ref = "";
    try { ref = document.referrer && new URL(document.referrer).origin !== location.origin ? new URL(document.referrer).hostname.replace(/^www\./, "") : ""; } catch (e) { ref = ""; }
    first = { landing: location.pathname, ref: ref, at: new Date().toISOString() };
    try { localStorage.setItem("growsterr_first", JSON.stringify(first)); } catch (e) { /* storage blocked */ }
  }

  /* ---------- The order form ---------- */
  var form = document.querySelector("[data-growth-form]");
  if (form) {
    ["utm_source", "utm_medium", "utm_campaign", "gclid"].forEach(function (k) {
      var input = form.querySelector('[name="' + k + '"]');
      if (input && !input.value) input.value = params.get(k) || stored[k] || "";
    });
    // The page whose button led here (this page itself when the visitor came straight in).
    var src = form.querySelector('[name="source_page"]');
    if (src && !src.value) {
      var from = document.referrer && document.referrer.indexOf(location.origin) === 0 ? document.referrer.slice(location.origin.length) : "";
      src.value = from || location.pathname;
    }
    var setIfEmpty = function (name, value) {
      var input = form.querySelector('[name="' + name + '"]');
      if (input && !input.value && value) input.value = value;
    };
    setIfEmpty("landing_page", stored.landing || first.landing);
    setIfEmpty("referrer", first.ref);
    setIfEmpty("first_visit_at", first.at);

    var texts = readJSON("growth-platform-ui") || {};
    var amount = form.querySelector("[data-order-amount]");
    var pickedPlan = function () { return form.querySelector('input[name="plan"]:checked'); };
    var pickedPlatform = function () { var p = form.querySelector('input[name="platform"]:checked'); return p ? p.value : "instagram"; };
    var item = function (pick) {
      return { item_id: pickedPlatform() + "_" + pick.value, item_name: pick.dataset.name, price: Number(pick.dataset.price), quantity: 1 };
    };

    // Another platform: its words (followers or subscribers, username or handle) everywhere on the page.
    var applyPlatform = function (platform) {
      var set = texts[platform];
      if (!set) return;
      document.querySelectorAll("[data-ui]").forEach(function (el) {
        var path = el.getAttribute("data-ui").split(".");
        var value = set.ui[path[0]];
        if (value === undefined) return;
        if (path.length > 1 && value) value = value[Number(path[1])];
        if (typeof value === "string") el.textContent = value;
      });
      Object.keys(set.plans || {}).forEach(function (key) {
        var card = form.querySelector('[data-plan="' + key + '"]');
        if (!card) return;
        var head = card.querySelector("[data-plan-headline]");
        var list = card.querySelector("[data-plan-items]");
        if (head) head.textContent = set.plans[key].headline;
        if (list) {
          list.textContent = "";
          set.plans[key].items.forEach(function (text) {
            var li = document.createElement("li");
            li.textContent = text;
            list.appendChild(li);
          });
        }
      });
    };

    form.addEventListener("change", function (e) {
      if (e.target.name === "plan") {
        if (amount) amount.textContent = e.target.dataset.amount;
        track("select_item", { item_list_id: "order", items: [item(e.target)] });
      } else if (e.target.name === "platform") {
        applyPlatform(e.target.value);
        form.querySelectorAll("[data-only-platform]").forEach(function (el) {
          el.hidden = el.getAttribute("data-only-platform") !== e.target.value;
        });
        // Keep the language links on the same platform choice.
        document.querySelectorAll('a[href*="/order/?"]').forEach(function (a) {
          try {
            var url = new URL(a.href, location.href);
            if (url.pathname !== location.pathname) return;
            url.searchParams.set("platform", e.target.value);
            a.href = url.pathname + url.search;
          } catch (err) { /* old browser */ }
        });
      }
    });

    var started = false;
    form.addEventListener("focusin", function (e) {
      if (started || e.target.name === "plan" || e.target.name === "platform") return;
      started = true;
      track("form_start", { form_id: "order", language: doc.lang });
    });
    form.addEventListener("submit", function () {
      var pick = pickedPlan();
      if (!pick || form.dataset.payments !== "on") return;  // request mode: generate_lead fires on the success page
      track("begin_checkout", { form_id: "order", language: doc.lang, value: Number(pick.dataset.price), currency: "USD", items: [item(pick)] });
    });
    if (form.dataset.formErrors) {
      track("lead_form_error", { form_id: "order", error_fields: form.dataset.formErrors.slice(0, 100) });
      var firstError = form.querySelector(".field--error input:not([type=hidden])");
      if (firstError) firstError.focus();
    }
  }

  /* ---------- Success and account pages: conversions ---------- */
  withUserData("purchase", readJSON("purchase-event"));
  withUserData("generate_lead", readJSON("lead-event"));
  var signup = readJSON("signup-event");
  if (signup) track("sign_up", signup);

  /* ---------- Dashboard ---------- */
  // Country codes become country names in the page's language.
  var regions = document.querySelectorAll("[data-region]");
  if (regions.length && window.Intl && Intl.DisplayNames) {
    try {
      var names = new Intl.DisplayNames([doc.lang || "en"], { type: "region" });
      regions.forEach(function (el) { var name = names.of(el.dataset.region); if (name) el.textContent = name; });
    } catch (e) { /* unknown code */ }
  }
  // "Show every day" reveals the older days of the table.
  document.querySelectorAll("[data-show-days]").forEach(function (button) {
    button.addEventListener("click", function () {
      var wrap = button.previousElementSibling;
      var more = wrap && wrap.querySelector(".g-days__more");
      if (more) more.hidden = false;
      button.remove();
    });
  });
})();
