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


def test_main_html_wires_all_three_families_and_preconnect():
    head = (ROOT / "overrides" / "main.html").read_text(encoding="utf-8")
    for needle in ["Fraunces", "Inter", "IBM+Plex+Mono", "fonts.gstatic.com"]:
        assert needle in head, f"overrides/main.html does not load {needle}"
    assert head.count("preconnect") >= 2, "expected two font preconnects"
