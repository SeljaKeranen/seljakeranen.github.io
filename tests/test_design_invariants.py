"""The design system's load-bearing rules, encoded as tests.

These guard the decisions that keep the look coherent: colour lives only in
tokens.css, the three type families are actually wired up, and reduced-motion is
respected. They read source files (no build needed).
"""

from __future__ import annotations

import re

from .conftest import ROOT, STYLES

REQUIRED_TOKENS = [
    "--bg",
    "--text",
    "--text-muted",
    "--green-dark",
    "--green",
    "--stone",
    "--accent",
    "--border",
    "--font-serif",
    "--font-sans",
    "--font-mono",
    "--md-text-font",
    "--md-code-font",
    "--page-width",
    "--article-width",
]
HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")
# Every stylesheet except the one place colour literals are allowed to live.
OTHER_SHEETS = ["theme-overrides.css", "base.css", "layout.css", "components.css"]


def test_tokens_defines_required_custom_properties():
    css = (STYLES / "tokens.css").read_text(encoding="utf-8")
    missing = [t for t in REQUIRED_TOKENS if f"{t}:" not in css]
    assert not missing, f"tokens.css is missing custom properties: {missing}"


def test_no_stray_hex_outside_tokens():
    offenders: list[str] = []
    for name in OTHER_SHEETS:
        for i, line in enumerate((STYLES / name).read_text(encoding="utf-8").splitlines(), 1):
            code = line.split("/*", 1)[0]  # ignore hex mentioned in comments
            if HEX.search(code):
                offenders.append(f"{name}:{i}: {line.strip()}")
    assert not offenders, "colour literals must live in tokens.css only:\n" + "\n".join(offenders)


def test_reduced_motion_is_respected():
    combined = "\n".join(
        (STYLES / n).read_text(encoding="utf-8") for n in ["base.css", "components.css"]
    )
    assert "prefers-reduced-motion" in combined


def test_fonts_are_self_hosted_not_google():
    """All three families load from local @font-face — no third-party font CDN.

    Fonts are vendored under docs/assets/fonts/ and declared in fonts.css, so
    the site makes no request to Google (no visitor IP leak, one fewer
    render-blocking origin). This guards against a regression back to the
    hot-linked Google Fonts stylesheet.
    """
    head = (ROOT / "overrides" / "main.html").read_text(encoding="utf-8")
    fonts_css = (STYLES / "fonts.css").read_text(encoding="utf-8")
    combined = head + fonts_css

    # No hot-link to Google, anywhere in the head or the font stylesheet.
    for banned in ["fonts.googleapis.com", "fonts.gstatic.com"]:
        assert banned not in combined, f"{banned} must not appear — fonts are self-hosted"

    # Every family has a real @font-face in fonts.css.
    for family in ['"Fraunces"', '"Inter"', '"IBM Plex Mono"']:
        assert family in fonts_css, f"fonts.css declares no @font-face for {family}"
    assert fonts_css.count("@font-face") >= 5, "expected @font-face for every vendored face"

    # Above-the-fold faces are preloaded so first paint doesn't reflow.
    assert head.count("rel=\"preload\"") >= 2, "expected the two font preloads in main.html"

    # Every woff2 the CSS or head references actually exists on disk.
    referenced = set(re.findall(r"assets/fonts/([\w.-]+\.woff2)", combined))
    assert referenced, "no vendored woff2 referenced"
    fonts_dir = ROOT / "docs" / "assets" / "fonts"
    for name in referenced:
        assert (fonts_dir / name).is_file(), f"missing vendored font: {name}"
