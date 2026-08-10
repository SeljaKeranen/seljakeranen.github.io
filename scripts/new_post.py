#!/usr/bin/env python3
"""Scaffold a new journal post with valid front matter.

    python scripts/new_post.py "Small systems scale differently" --category Notes

Writes docs/blog/posts/<slug>.md (refusing to clobber an existing file). The
category must be one of the closed set the site knows how to theme and validate.
Pure standard library.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

# Keep in sync with hooks/hero_art.py (CATEGORY_ART) and tests/test_frontmatter.py.
CATEGORIES = ["Systems", "Evals", "Tools", "Field", "Craft", "Notes"]
POSTS_DIR = Path(__file__).resolve().parent.parent / "docs" / "blog" / "posts"

TEMPLATE = """\
---
date: {date}
authors: [selja]
categories: [{category}]
draft: {draft}
description: One sentence on what this covers — it becomes the excerpt and meta description.
---

# {title}

The opening paragraph is the excerpt shown on the blog index and homepage.
Say the interesting thing first.

<!-- more -->

Write the rest here.
"""


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new journal post.")
    parser.add_argument("title", help="Post title")
    parser.add_argument("--category", default="Notes", choices=CATEGORIES)
    parser.add_argument(
        "--date", default=dt.date.today().isoformat(), help="ISO date (default: today)"
    )
    parser.add_argument("--slug", help="Override the auto-generated slug")
    parser.add_argument(
        "--draft",
        action="store_true",
        help="Mark as draft (visible on `mkdocs serve`, excluded from the build)",
    )
    args = parser.parse_args(argv)

    slug = args.slug or slugify(args.title)
    if not slug:
        parser.error("could not derive a slug from the title; pass --slug")

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    path = POSTS_DIR / f"{slug}.md"
    if path.exists():
        print(f"refusing to overwrite existing post: {path}", file=sys.stderr)
        return 1

    path.write_text(
        TEMPLATE.format(
            date=args.date,
            category=args.category,
            title=args.title,
            draft=str(args.draft).lower(),
        ),
        encoding="utf-8",
    )
    rel = path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path
    print(f"created {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
