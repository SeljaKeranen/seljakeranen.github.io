"""The rendered journal distinguishes source-note dates from write-up dates."""

from html import unescape
from html.parser import HTMLParser


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def visible(path):
    parser = Text()
    parser.feed(path.read_text())
    return " ".join(unescape(" ".join(parser.parts)).split())


def test_retrospective_dates_are_labelled_everywhere(site):
    article = (
        site
        / "blog/2026/10/11"
        / "a-few-strategy-questions-before-opening-another-repository/index.html"
    )
    for path in (site / "index.html", site / "blog/index.html", article):
        text = visible(path)
        assert "Notebook: October 11, 2026" in text
        assert "Written October 13, 2026" in text


def test_ordinary_post_keeps_its_original_dateline(site):
    article = site / "blog/2026/08/07/starting-a-blog-mostly-to-think-out-loud/index.html"
    text = visible(article)
    assert "August 7, 2026" in text
    assert "Notebook:" not in text
    assert "Written October 13, 2026" not in text
