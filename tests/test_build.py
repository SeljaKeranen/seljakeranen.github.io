"""The site builds strict, every internal link resolves, every image has alt."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path

EXTERNAL = ("http://", "https://", "//", "mailto:", "tel:", "data:", "javascript:")


class _Extract(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.imgs: list[dict] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("a", "link") and a.get("href"):
            self.links.append(a["href"])
        if tag in ("script", "img") and a.get("src"):
            self.links.append(a["src"])
        if tag == "img":
            self.imgs.append(a)


def _pages(site: Path) -> list[Path]:
    return sorted(site.rglob("*.html"))


def _resolve(base: Path, url: str, site: Path) -> Path | None:
    url = url.split("#", 1)[0].split("?", 1)[0]
    if not url or url.startswith(EXTERNAL):
        return None
    target = (site / url.lstrip("/")) if url.startswith("/") else (base.parent / url)
    target = target.resolve()
    if site.resolve() not in target.parents and target != site.resolve():
        return None  # escapes the site root; not ours to validate
    return target


def _exists(target: Path) -> bool:
    if target.is_file():
        return True
    if (target / "index.html").is_file():
        return True
    return target.suffix == "" and target.with_suffix(".html").is_file()


def test_expected_pages_built(site: Path):
    for rel in [
        "index.html",
        "about/index.html",
        "archive/index.html",
        "blog/index.html",
        "404.html",
    ]:
        assert (site / rel).is_file(), f"missing built page: {rel}"


def test_internal_links_resolve(site: Path):
    broken: list[str] = []
    for page in _pages(site):
        parser = _Extract()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in parser.links:
            target = _resolve(page, href, site)
            if target is not None and not _exists(target):
                broken.append(f"{page.relative_to(site)} -> {href}")
    assert not broken, "broken internal links:\n" + "\n".join(broken)


def test_every_image_has_alt(site: Path):
    missing: list[str] = []
    for page in _pages(site):
        parser = _Extract()
        parser.feed(page.read_text(encoding="utf-8"))
        for img in parser.imgs:
            if "alt" not in img:
                missing.append(f"{page.relative_to(site)}: {img.get('src')}")
    assert not missing, "images without an alt attribute:\n" + "\n".join(missing)


def test_home_has_hero_and_latest(site: Path):
    html = (site / "index.html").read_text(encoding="utf-8")
    assert "folio-hero__title" in html
    assert "folio-card__title" in html  # the hook injected at least one post
    assert "640 720" in html  # the inlined hero SVG survived minification


def test_notes_category_page_exists(site: Path):
    # The masthead links to /blog/category/notes/ on every page; if the last
    # Notes-tagged post ever loses that category the link would 404. Fail here,
    # at build time, instead of silently in production.
    assert (site / "blog" / "category" / "notes" / "index.html").is_file(), (
        "no Notes category page — the header 'Notes' link would 404; "
        "keep at least one post categorised Notes"
    )


def test_post_has_editorial_dateline_above_title(site: Path):
    posts = list((site / "blog").rglob("index.html"))
    articles = [p for p in posts if "article__meta" in p.read_text(encoding="utf-8")]
    assert articles, "no post rendered the editorial dateline (.article__meta)"
    html = articles[0].read_text(encoding="utf-8")
    assert html.index("article__meta") < html.index("<h1"), (
        "the dateline must sit above the article title"
    )
