# Working in this repository

Personal editorial site + journal for Selja Keränen, built with **Material for
MkDocs** and deployed to GitHub Pages. The look is deliberate — read this before
changing markup, styles, or structure.

## Commands

```bash
make install     # venv + dev/doc deps (uv)
make serve       # live preview at http://127.0.0.1:8000
make build       # strict production build (must stay green)
make test        # strict build + frontmatter + design invariants
make new TITLE="…" CATEGORY=Notes   # scaffold a post
make hooks       # install pre-commit
```

`mkdocs build --strict` is the contract. It must exit clean; CI and pre-commit
enforce it.

## Writing a post

Scaffold with `make new` (preferred) or add `docs/blog/posts/<kebab-slug>.md`:

```markdown
---
date: 2026-08-07
authors: [selja]
categories: [Notes]
description: One sentence (≤ ~160 chars) — this is the excerpt and the meta description.
---

# Post title

The opening paragraph is the excerpt shown on the blog index and homepage.

<!-- more -->

The rest of the post.
```

The first paragraph (before `<!-- more -->`) is the excerpt — make it earn the
click. `description` drives the homepage card and the `<meta>` description.

For a retrospective notebook entry, `date` is the date of the source notes.
Set `notebook_date: true` and `written: YYYY-MM-DD` to show the write-up date
separately on the homepage, archive excerpts and article. Never use the notebook
date to imply an earlier publication. Ordinary posts keep the existing dateline.

**Drafts:** add `draft: true` (or `make new … ` then edit, or `scripts/new_post.py
--draft`). Draft posts show on `mkdocs serve` but are excluded from the production
build, so you can work on a piece without publishing it.

### Categories (closed set)

`Systems`, `Evals`, `Tools`, `Field`, `Craft`, `Notes`. The set is enforced by
`tests/test_frontmatter.py` and `scripts/new_post.py`, and each maps to a piece
of line-art on the homepage (see `hooks/hero_art.py` → `CATEGORY_ART`). To add a
category, update all three. Keep at least one post categorised `Notes` so the
`/blog/category/notes/` page (linked from post datelines) resolves —
`test_notes_category_page_exists` guards this. Note this blog *category* `Notes`
is distinct from the top-nav **Notes** *section* at `/notes/` (evergreen pages on
how Selja works, under `docs/notes/`).

## The design system (don't fight it)

- **Colour lives in one file.** Every colour literal is a custom property in
  `docs/stylesheets/tokens.css`. The other four stylesheets reference tokens
  only — `test_design_invariants.py` fails on a stray hex. Add a token; don't
  hard-code.
- **Load order is fixed:** fonts → tokens → theme-overrides → base → layout →
  components (see `extra_css` in `mkdocs.yml`). `fonts.css` only declares the
  self-hosted `@font-face` faces, so it sits ahead of the token-remap chain
  without disturbing it; tokens still define the variables before anything
  consumes them. Material's compiled CSS loads first; our `--md-*` remaps win
  by source order.
- **Three type roles:** Fraunces (display serif, headings only), Inter (body /
  UI), IBM Plex Mono (metadata / code). Fonts are loaded once in
  `overrides/main.html`; `theme.font` is `false` on purpose.
- **The signature is the datum line** (`.datum-line`) — a hairline + graduated
  ticks + one clay benchmark ▲. Clay (`--accent`) is spent sparingly: the active
  nav item, the datum benchmark, the footer close, and one mark inside the art.
- **Imagery** is the hand-drawn SVG system in `docs/assets/art/` — see its
  `README.md`. Keep every drawing in that visual universe.

## Structure

```
docs/            content (index = the Home landing: greeting + prose + latest writing; blog/, notes/, stylesheets/, javascripts/, assets/)
overrides/       forked Material templates (main, home, 404, partials/header, footer, art/)
hooks/           build hooks (hero_art.py: homepage cards, per-post art)
scripts/         author tooling (new_post.py)
tests/           pytest: strict build, link/alt checks, frontmatter, design invariants
```

Nav is three sections, and the wordmark also links **Home**: **Home**
(`index.md`, rendered with `overrides/home.html` — the "Selja here…" greeting +
personal prose, closing with the latest-writing snippet); **Blog** (`/blog/`);
and **Notes** (`/notes/`, evergreen how-I-work pages). The header lives in
`overrides/partials/header.html`; `docs/javascripts/reveal.js` re-derives the
active-section marker (`home` / `blog` / `notes`) across instant navigation, so
keep the two in sync.

## House rules

- Keep the strict build green in the area you touch; report unrelated breakage.
- Never edit files under `site/` — it is generated. Change the source.
- Don't add runtime dependencies to `requirements-doc.txt` without a reason;
  that file is the deploy surface and is pinned deliberately.
- Editorial voice: quiet, concrete, honest. No hype, no emoji.
- Preserve Selja's voice. When editing a draft, make light punctuation and
  grammar fixes only — don't rewrite unless explicitly asked.
