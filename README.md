# seljakeranen.github.io

Personal editorial site and journal for **Selja Keränen** — built with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and deployed
to GitHub Pages. Quiet, text-first, with a hand-drawn survey-plate visual system.

## Quick start

```bash
make install     # venv + dependencies (uv)
make serve       # live preview at http://127.0.0.1:8000
make build       # strict production build
make test        # strict build + frontmatter + design-invariant checks
make new TITLE="A new post" CATEGORY=Notes
```

Run `make` on its own for the full list.

## Writing

Posts live in `docs/blog/posts/`. `make new` scaffolds one with valid front
matter; the full authoring contract (front matter, the closed category set, the
design-token rules, the art system) is in **[AGENTS.md](AGENTS.md)**.

## Layout

```
docs/          content — index (the Home landing), blog/, notes/, books/, stylesheets/, javascripts/, assets/
data/          curated public reading shelf — books.json
overrides/     forked Material templates (masthead, home, 404, footer, reading shelf)
hooks/         build hooks — hero_art.py: homepage cards, per-post art; books.py: reading shelf
scripts/       author tooling — new_post.py
tests/         pytest — strict build, link + alt checks, front matter, design invariants
```

The top nav has four sections — **Home** (`index.md`, the "Selja here…" greeting
+ latest-writing landing), **Blog** (`/blog/`), **Notes** (`/notes/`,
evergreen how-I-work pages), and **Books** (`/books/`, reading notes connected
by theme); the wordmark also links Home.

## Design

- Colour literals live only in `docs/stylesheets/tokens.css`; everything else
  references tokens. Type is Fraunces (display) / Inter (body) / IBM Plex Mono
  (metadata), loaded once in `overrides/main.html`.
- The recurring **datum line** — a hairline, graduated ticks, one clay
  benchmark ▲ — is the site's signature. See [AGENTS.md](AGENTS.md) and
  `docs/assets/art/README.md`.

## Deploy

Push to `main`. `.github/workflows/deploy.yml` builds with
`mkdocs build --strict` and publishes to GitHub Pages. `ci.yml` runs lint +
tests on every push and pull request. Nothing to do by hand.
