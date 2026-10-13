"""Render the public reading shelf once, for both the map and plain notes.

Only curated public content belongs in data/books.json. Private source notes and
reading-status evidence are kept outside this repository.
"""

import json
from pathlib import Path

from mkdocs.utils import get_relative_url

DATA = Path(__file__).resolve().parents[1] / "data" / "books.json"


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "books/index.md":
        return markdown

    shelf = json.loads(DATA.read_text(encoding="utf-8"))
    themes = {theme["id"] for theme in shelf["themes"]}
    ids = set()
    for entry in shelf["entries"]:
        if entry["id"] in ids or entry["theme"] not in themes:
            raise ValueError(f"Duplicate book id or unknown theme: {entry['id']}")
        ids.add(entry["id"])
        if entry.get("post"):
            entry["post_url"] = get_relative_url(entry["post"], page.url)

    template = config.theme.get_env().get_template("partials/books.html")
    return markdown + "\n\n" + template.render(shelf=shelf)
