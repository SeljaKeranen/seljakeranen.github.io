"""Accessible navigation contracts in the generated public HTML.

Pixel geometry and keyboard interaction are exercised with the browser acceptance
script; these tests keep the built search trigger and intro destinations intact.
"""

from html.parser import HTMLParser
from pathlib import Path


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.triggers = []
        self.ids = set()
        self.intro_links = []
        self.in_intro = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if "folio-search-trigger" in classes:
            self.triggers.append((tag, attrs))
        if "folio-intro-links" in classes:
            self.in_intro = True
        if self.in_intro and tag == "a":
            self.intro_links.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "div":
            self.in_intro = False


def test_search_trigger_is_named_native_button(site: Path):
    for rel in ("index.html", "blog/index.html", "notes/index.html", "404.html"):
        nav = Navigation()
        nav.feed((site / rel).read_text())
        assert len(nav.triggers) == 1
        tag, attrs = nav.triggers[0]
        assert tag == "button"
        assert attrs.get("type") == "button"
        assert attrs.get("aria-label") == "Search"
        assert attrs.get("aria-controls") in nav.ids
        assert attrs.get("aria-expanded") == "false"


def test_intro_links_reach_blog_and_working_notes(site: Path):
    nav = Navigation()
    nav.feed((site / "index.html").read_text())
    assert nav.intro_links == ["blog/", "notes/"]
