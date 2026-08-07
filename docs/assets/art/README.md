# The line-art system

Hand-drawn SVG line-art, one visual universe: an 1890s survey folio. Historic
architecture, botanical specimens, and landscapes rendered as engraved plates —
contours, faint grids, lens rings, coordinate ticks, and one clay benchmark ▲.
No raster photography; nothing that looks machine-generated.

## Shared vocabulary

All pieces are drawn from the same marks, so they read as one hand:

| Element        | Role                                  | Colour              |
| -------------- | ------------------------------------- | ------------------- |
| survey grid    | faint graph-paper ground              | ink @ 6%            |
| contour lines  | hills, lakes, ground                  | sage @ ~34%         |
| structure line | architecture, specimens (primary)     | ink @ ~72%          |
| lens ring      | plate / instrument circle             | ink @ ~34%          |
| benchmark ▲    | the one accent, used once per drawing | clay `#A66F5B`      |
| mono label     | `FIG.` / `BM` plate annotations       | ink @ ~50%          |

## Theming

- The **homepage hero** SVG is written *inline* in `overrides/home.html`, so its
  strokes use the page's CSS variables (`--line-ink`, `--contour`, `--accent`, …)
  and re-ink on the light/dark **palette toggle** (not just the OS scheme).
- The five card motifs here are loaded via `<img>`, so they are self-contained
  documents that re-ink by the viewer's **OS colour scheme** via an internal
  `@media (prefers-color-scheme: dark)` block. (An `<img>` cannot see the site's
  toggle — an accepted limitation.)

## The five motifs (category → art, see `hooks/hero_art.py`)

| File                        | viewBox   | Category            |
| --------------------------- | --------- | ------------------- |
| `floating-architecture.svg` | 480 × 360 | Systems             |
| `gardens-structures.svg`    | 480 × 360 | Field / Craft       |
| `botanical-studies.svg`     | 320 × 400 | Notes (+ default)   |
| `landscape-diagram.svg`     | 560 × 320 | Evals               |
| `architectural-fragment.svg`| 360 × 420 | Tools (+ 404)       |

`../favicon.svg` distils the glasshouse gable + benchmark into a 32 × 32 mark.

## Replacing with commissioned art

To drop in raster illustrations later, keep the filenames and the ~4:3 / 3:4
framing, and update `CATEGORY_ART` in `hooks/hero_art.py` if the extensions
change. Match the palette (limestone, ink, sage, one rare clay) and the 40–60%
negative space so the universe stays coherent.
