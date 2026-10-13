/* Gentle fade-in for elements marked .reveal.
 *
 * Subscribed to Material's `document$` observable so it re-arms after every
 * instant-navigation swap (a plain DOMContentLoaded listener would fire once
 * and then silently die after the first in-site click).
 *
 * Progressive enhancement: the `.js` flag on <html> is what actually hides
 * .reveal elements, so with JavaScript disabled everything is simply visible.
 * Reduced-motion users get the content with no transition.
 */
document.documentElement.classList.add("js");

document$.subscribe(function () {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.querySelectorAll(".reveal").forEach(function (el) {
      el.classList.add("is-in");
    });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          obs.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.05 },
  );

  document.querySelectorAll(".reveal:not(.is-in)").forEach(function (el) {
    observer.observe(el);
  });
});

// Keep the masthead's active-section marker correct across instant navigation:
// the forked header is not re-rendered on an in-site swap, so its build-time
// aria-current would otherwise go stale. Re-derived from the URL on every swap.
document$.subscribe(function () {
  var p = location.pathname;
  // Anchor every marker at the root so nothing spurious lights up: the Home
  // link is current only on the actual landing ("/" or "/index.html"), matching
  // the strict build-time aria-current in header.html — so 404 and any future
  // top-level page correctly highlight nothing rather than defaulting to Home.
  // The /blog and /notes anchors also stop a post slug containing "notes"/"blog"
  // from hijacking the marker.
  var section = "";
  if (/^\/notes(\/|$)/.test(p)) section = "notes";
  else if (/^\/blog(\/|$)/.test(p)) section = "blog";
  else if (p === "/" || p === "/index.html") section = "home";

  document.querySelectorAll(".folio-nav__link").forEach(function (link) {
    if (link.getAttribute("data-section") === section) {
      link.setAttribute("aria-current", "page");
    } else {
      link.removeAttribute("aria-current");
    }
  });
});

// Give the compact search trigger native keyboard semantics while preserving
// Material's checkbox-driven search panel and its input focus management.
(function () {
  var trigger = document.querySelector(".folio-search-trigger");
  var toggle = document.getElementById("__search");
  if (!trigger || !toggle) return;

  trigger.addEventListener("click", function () {
    toggle.click();
    if (toggle.checked) document.querySelector(".md-search__input").focus();
  });
  toggle.addEventListener("change", function () {
    trigger.setAttribute("aria-expanded", String(toggle.checked));
    if (!toggle.checked && trigger.getClientRects().length) trigger.focus();
  });
})();
