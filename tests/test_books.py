"""Contracts of the rendered public Books page, including its no-JS content."""

from html.parser import HTMLParser


class Shelf(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.nodes = {}
        self.notes = {}
        self.fields = {}
        self.text = {}
        self.note = None
        self.capture = None
        self.options = []
        self.groups = set()
        self.controls = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if "data-book-link" in attrs:
            self.nodes[attrs["href"][1:]] = attrs["aria-label"]
        if "data-book-note" in attrs:
            self.note = attrs["id"]
            self.notes[self.note] = attrs
            self.fields[self.note] = []
            self.text[self.note] = ""
        if self.note and tag == "dt":
            self.capture = ""
        if tag == "option":
            self.options.append(attrs["value"])
        if "data-book-theme" in attrs:
            self.groups.add(attrs["data-book-theme"])
        if "books-filter" in attrs.get("class", "").split():
            self.controls = attrs

    def handle_data(self, data):
        if self.capture is not None:
            self.capture += data
        if self.note:
            self.text[self.note] += data

    def handle_endtag(self, tag):
        if tag == "dt" and self.capture is not None:
            self.fields[self.note].append(self.capture.strip())
            self.capture = None
        if tag == "details":
            self.note = None


def read_shelf(site):
    shelf = Shelf()
    shelf.feed((site / "books/index.html").read_text())
    return shelf


def test_every_graph_node_reaches_one_equivalent_note(site):
    shelf = read_shelf(site)
    assert len(shelf.ids) == len(set(shelf.ids))
    assert len(shelf.notes) == 35
    assert shelf.nodes.keys() == shelf.notes.keys()
    for book_id, label in shelf.nodes.items():
        assert label.removesuffix(" (video)") in shelf.text[book_id]
        assert shelf.notes[book_id]["data-theme"] in shelf.groups
        assert "What I liked" in shelf.fields[book_id]
        assert "What I didn't" in shelf.fields[book_id]


def test_no_js_has_complete_notes_and_no_inert_filter(site):
    shelf = read_shelf(site)
    assert "hidden" in shelf.controls
    assert set(shelf.options) == shelf.groups | {"all"}
    assert all("hidden" not in note for note in shelf.notes.values())
    assert "Still to add." in shelf.text["atomic-habits"]
    assert "Key takeaway" in shelf.fields["atomic-habits"]
    assert "completion not recorded" in shelf.text["atomic-habits"]


def test_confirmed_additions_and_media_keep_their_status(site):
    shelf = read_shelf(site)
    assert "Read in Swedish" in shelf.text["lessons-in-chemistry"]
    assert "Lektioner i kemi" in shelf.text["lessons-in-chemistry"]
    assert "I loved it!" in shelf.text["lessons-in-chemistry"]
    assert "Theodore Gray" in shelf.text["the-elements"]
    assert "zinc roofs of Paris" in shelf.text["the-elements"]
    assert "The Thinking Machine, and making room for luck" in shelf.text["the-thinking-machine"]
    assert shelf.notes["llm-evals-video"]["data-kind"] == "video"
    assert shelf.notes["how-to-talk-to-ai-and-how-not-to"]["data-kind"] == "book"
