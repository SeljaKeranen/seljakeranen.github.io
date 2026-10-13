() => {
  // Run at 320px with a vertical scrollbar, after document.fonts.ready.
  const width = document.documentElement.clientWidth;
  const links = [...document.querySelectorAll('.folio-nav__link')];
  if (links.length !== 4) throw new Error('Expected all four navigation links');
  return links.map((link) => {
    const range = document.createRange();
    range.selectNodeContents(link);
    const bounds = range.getBoundingClientRect();
    if (bounds.left < 0 || bounds.right > width) {
      throw new Error(`${link.textContent} clipped: ${bounds.left}–${bounds.right}, viewport ${width}`);
    }
    return { label: link.textContent, left: bounds.left, right: bounds.right, width };
  });
}
