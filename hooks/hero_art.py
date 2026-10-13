"""Build hook: homepage "latest writing" + per-post hero art.

Two small, related jobs, kept in one file so there are no cross-hook imports:

1. On the homepage, inject ``recent_posts`` — the three newest posts (title,
   url, date, summary, categories, and a rotating piece of line-art) — which
   ``overrides/home.html`` renders as editorial cards.

2. On every blog post, stamp ``page.meta["hero_art"]`` with the post's
   category art so a template (or an author) can reference it later.

``_iso`` is retained as a small shared date helper for ``_card``.

The art is atmospheric, not semantic: each content category maps to one of the
five line-art motifs purely so the homepage rotates through the visual universe
instead of repeating one drawing. Pure standard library; runs at ``mkdocs
build`` time via the ``hooks:`` entry in ``mkdocs.yml``.
"""

from __future__ import annotations

# Content category -> line-art motif (filenames live in docs/assets/art/).
# Keep the keys in sync with scripts/new_post.py and tests/test_frontmatter.py.
CATEGORY_ART: dict[str, str] = {
    "Systems": "floating-architecture.svg",
    "Evals": "landscape-diagram.svg",
    "Tools": "architectural-fragment.svg",
    "Field": "gardens-structures.svg",
    "Craft": "gardens-structures.svg",
    "Notes": "botanical-studies.svg",
}
DEFAULT_ART = "botanical-studies.svg"
ART_DIR = "assets/art/"


def art_for(categories) -> str:
    """Return the art path for a post, given its category titles/objects."""
    for cat in categories or ():
        title = getattr(cat, "title", cat)
        if title in CATEGORY_ART:
            return ART_DIR + CATEGORY_ART[title]
    return ART_DIR + DEFAULT_ART


def _blog_posts(config):
    """Best-effort access to the Material blog plugin's sorted post list."""
    plugin = config.plugins.get("material/blog")
    if plugin is None:  # entry-point name can vary across installs
        plugin = next(
            (p for p in config.plugins.values() if type(p).__name__ == "BlogPlugin"),
            None,
        )
    view = getattr(plugin, "blog", None)
    return list(getattr(view, "posts", []) or [])


def _iso(value) -> str:
    try:
        return value.isoformat()
    except AttributeError:
        return str(value or "")


def _card(post) -> dict:
    """Shape one post into the minimal dict the homepage template needs.

    Everything is guarded so a bare post (no description, no category) can never
    break ``mkdocs build --strict``.
    """
    cfg = getattr(post, "config", None)
    created = getattr(getattr(cfg, "date", None), "created", None)
    cats = [
        (getattr(c, "title", str(c)), getattr(c, "url", ""))
        for c in (getattr(post, "categories", None) or ())
    ]
    return {
        "title": getattr(post, "title", None) or "Untitled",
        "url": getattr(post, "url", ""),
        "date": created,
        "date_iso": _iso(created),
        "notebook_date": (getattr(post, "meta", {}) or {}).get("notebook_date", False),
        "written": (getattr(post, "meta", {}) or {}).get("written"),
        "summary": (getattr(post, "meta", {}) or {}).get("description"),
        "categories": cats,
        "art": art_for(getattr(post, "categories", None)),
    }


def on_page_context(context, *, page, config, nav):
    """Inject homepage cards; stamp hero art on posts."""
    posts = _blog_posts(config)

    if getattr(page, "is_homepage", False):
        context["recent_posts"] = [_card(p) for p in posts[:3]]
        return context

    if page in posts:
        page.meta["hero_art"] = art_for(getattr(page, "categories", None))

    return context
