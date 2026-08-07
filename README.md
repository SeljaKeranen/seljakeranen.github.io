# seljakeranen.github.io

Personal site and blog, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
and deployed to GitHub Pages.

## Local preview

```bash
uv venv                                   # once
uv pip install -r requirements-doc.txt    # once
uv run mkdocs serve                        # live preview at http://127.0.0.1:8000
```

## Writing a post

Add a Markdown file under `docs/blog/posts/`. Front matter drives the date,
author, and excerpt cut:

```markdown
---
date: 2026-08-07
authors:
  - selja
categories:
  - Notes
---

# Post title

First paragraph shows up as the excerpt on the blog index.

<!-- more -->

The rest of the post.
```

## Deploy

Push to `main`. The `Deploy site` GitHub Action builds with `mkdocs build --strict`
and publishes to GitHub Pages automatically. Nothing to do by hand.
