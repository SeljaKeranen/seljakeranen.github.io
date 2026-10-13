/* The rendered map and shelf are complete without JavaScript. Enhance only the
 * theme filter and opening a note reached by a graph link or a shared fragment.
 * Material swaps the article on instant navigation, so bind each new shelf once.
 */
(function () {
  function revealFragment(shelf) {
    var id;
    try {
      id = decodeURIComponent(location.hash.slice(1));
    } catch (_) {
      return;
    }
    var target = document.getElementById(id);
    if (!target || !shelf.contains(target)) return;
    var group = target.closest("[data-book-theme]");
    if (group && group.hidden) {
      var filter = shelf.querySelector("select");
      filter.value = "all";
      filter.dispatchEvent(new Event("change"));
    }
    if (target.matches("[data-book-note]")) {
      target.open = true;
      target.querySelector("summary").focus({ preventScroll: true });
      target.scrollIntoView({ block: "start" });
    }
  }

  document$.subscribe(function () {
    var shelf = document.querySelector("[data-books-shelf]");
    if (!shelf) return;
    if (!shelf.dataset.ready) {
      var filter = shelf.querySelector("select");
      var groups = shelf.querySelectorAll("[data-book-theme]");
      var count = shelf.querySelector(".books-count");
      function update() {
        groups.forEach(function (group) {
          group.hidden = filter.value !== "all" && group.dataset.bookTheme !== filter.value;
        });
        var visible = Array.from(shelf.querySelectorAll("[data-book-note]")).filter(
          function (note) {
            return !note.closest("[data-book-theme]").hidden;
          },
        );
        var books = visible.filter(function (note) {
          return note.dataset.kind === "book";
        }).length;
        var videos = visible.length - books;
        count.textContent =
          books +
          (books === 1 ? " book" : " books") +
          (videos ? " · " + videos + (videos === 1 ? " video note" : " video notes") : "");
      }
      filter.addEventListener("change", update);
      // Handle local graph links before Material's instant-navigation listener.
      // Native navigation to an already-current fragment would otherwise
      // move focus back to the body after we focus the note summary.
      shelf.addEventListener("click", function (event) {
        var link = event.target.closest("a[data-book-link]");
        if (
          !link ||
          event.button !== 0 ||
          event.metaKey ||
          event.ctrlKey ||
          event.shiftKey ||
          event.altKey
        )
          return;
        event.preventDefault();
        event.stopPropagation();
        if (link.hash !== location.hash) location.hash = link.hash;
        revealFragment(shelf);
      });
      shelf.querySelector(".books-filter").hidden = false;
      shelf.dataset.ready = "true";
      update();
    }
    revealFragment(shelf);
  });
  window.addEventListener("hashchange", function () {
    var shelf = document.querySelector("[data-books-shelf]");
    if (shelf) revealFragment(shelf);
  });
})();
