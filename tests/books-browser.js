() => {
  // Execute with chrome-devtools-axi eval on /books/. No browser dependency added.
  const assert = (ok, message) => { if (!ok) throw new Error(message); };
  const shelf = document.querySelector('[data-books-shelf]');
  assert(shelf, 'Books page is loaded');
  const visible = (element) => element.getClientRects().length > 0;
  const select = shelf.querySelector('select');
  const original = select.value;
  const results = [];
  for (const option of select.options) {
    select.value = option.value;
    select.dispatchEvent(new Event('change', { bubbles: true }));
    const nodes = [...shelf.querySelectorAll('[data-book-link]')].filter(visible);
    const notes = [...shelf.querySelectorAll('[data-book-note]')].filter(visible);
    assert(nodes.length === notes.length, option.value + ': graph and notes count match');
    for (const node of nodes) {
      const note = document.getElementById(new URL(node.href).hash.slice(1));
      assert(note && visible(note), 'Visible graph link reaches visible note');
      assert(option.value === 'all' || note.dataset.theme === option.value, 'Theme matches');
    }
    for (const branches of [...shelf.querySelectorAll('.book-branches')].filter(visible)) {
      assert(getComputedStyle(branches).display === 'grid', 'Material must not override graph layout');
      for (const row of branches.children) {
        const edge = row.querySelector('svg').getBoundingClientRect();
        const node = row.querySelector('a').getBoundingClientRect();
        const bounds = row.getBoundingClientRect();
        assert(Math.abs(edge.height - bounds.height) < 1,
          'SVG connectors span their complete row');
        assert(Math.abs(edge.top + edge.height / 2 - node.top - node.height / 2) < 1,
          'Connectors reach the book node centre');
      }
      const links = [...branches.querySelectorAll('a')];
      if (links.length > 1) {
        const left = links[0].getBoundingClientRect();
        const right = links[1].getBoundingClientRect();
        assert(right.left > left.right && Math.abs(right.top - left.top) < 40,
          'Book nodes occupy both sides of their connecting spine');
      }
    }
    assert(document.documentElement.scrollWidth <= innerWidth + 1, 'No horizontal overflow');
    results.push({ theme: option.value, visibleNotes: notes.length });
  }
  select.value = original;
  select.dispatchEvent(new Event('change', { bubbles: true }));
  const first = [...shelf.querySelectorAll('[data-book-link]')].find(visible);
  const note = document.getElementById(new URL(first.href).hash.slice(1));
  first.click();
  assert(note.open, 'Graph link opens its note');
  first.focus();
  first.click();
  assert(document.activeElement === note.querySelector('summary'),
    'Reopening the same graph fragment must keep keyboard focus on the note');
  return { viewport: innerWidth, filters: results, result: 'pass' };
}
