"""Every journal post has valid, house-style front matter."""

from __future__ import annotations

import datetime as dt
import re

import yaml

from .conftest import DOCS, POSTS

CATEGORIES = {"Systems", "Evals", "Tools", "Field", "Craft", "Notes"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

_authors_file = DOCS / "blog" / ".authors.yml"
VALID_AUTHORS = set((yaml.safe_load(_authors_file.read_text()) or {}).get("authors", {}))

POST_FILES = sorted(POSTS.glob("*.md"))


def _split(text: str) -> tuple[dict, str]:
    assert text.startswith("---"), "post must open with a YAML front-matter block"
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body


def _each_post():
    return [(p.name, p) for p in POST_FILES]


def test_there_are_posts():
    assert POST_FILES, "no posts found under docs/blog/posts/"


def test_posts_have_valid_frontmatter():
    problems: list[str] = []
    for path in POST_FILES:
        name = path.name
        meta, body = _split(path.read_text(encoding="utf-8"))

        if not isinstance(meta.get("date"), (dt.date, dt.datetime)):
            problems.append(f"{name}: 'date' missing or not a real date")

        authors = meta.get("authors") or []
        if not authors:
            problems.append(f"{name}: no authors")
        for a in authors:
            if a not in VALID_AUTHORS:
                problems.append(f"{name}: unknown author '{a}' (not in .authors.yml)")

        cats = meta.get("categories") or []
        if not cats:
            problems.append(f"{name}: no categories")
        for c in cats:
            if c not in CATEGORIES:
                problems.append(f"{name}: category '{c}' not in {sorted(CATEGORIES)}")

        desc = meta.get("description")
        if not isinstance(desc, str) or not desc.strip():
            problems.append(f"{name}: missing description")
        elif len(desc) > 200:
            problems.append(f"{name}: description too long ({len(desc)} > 200 chars)")

        if "<!-- more -->" not in body:
            problems.append(f"{name}: missing <!-- more --> excerpt marker")

        if not SLUG_RE.match(path.stem):
            problems.append(f"{name}: filename is not kebab-case")

    assert not problems, "front-matter problems:\n" + "\n".join(problems)
