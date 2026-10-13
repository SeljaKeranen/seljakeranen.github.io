# Responsive layout evidence — 13 October 2026

Before: `c7c10b8af0ddf2ef633696e57063b9630eb2676a`. After: `9f2d2f9ce463b7feea0208b92f88579ae9ca607f`, bound by [SHA-256 hashes](source-sha256.json). These hashes identify the captured source before subsequent formatter-only changes. Both were built locally with the repository's unchanged dependency pins. No deployed files were edited.

| Approved fix | Before | After |
| --- | --- | --- |
| Header | 360px: three rows, 183px tall. 1024px: name wraps. | Two intentional rows, 107px tall on phones; one-line name at all six widths. Named Search button supports Enter/Space, focuses the input, and restores focus after Escape. |
| Shared frame | At 1920px, brand x412 and prose x72. | Brand, prose and footer all x412; at 1440px all x172. Prose remains limited to 720px. |
| Type and spacing | Body 21.25–26.125px; first H2 margin 140–211.75px. | Body 17–19px; H2 margin 30–55px. Body remains 19px across Material's 1600px and 2000px root-size steps. |
| Intro and next steps | 360px lead occupies 488px, without immediate next-step links. | Two sentences, 180px lead; “Read the blog” and “How I work” visible on the first phone screen. Later biography retained. |
| Tablet cards | One column at 768px; three at 1024px. | Two columns at both widths; one on phones and three on wide screens. Artwork remains contained without cropping. |

## Before and after

| Width | Homepage before / after | Scrolled cards before / after |
| --- | --- | --- |
| 360 | [Before](before-home-360.png) / [After](after-home-360.png) | [Before](before-cards-360.png) / [After](after-cards-360.png) |
| 390 | [Before](before-home-390.png) / [After](after-home-390.png) | [Before](before-cards-390.png) / [After](after-cards-390.png) |
| 768 | [Before](before-home-768.png) / [After](after-home-768.png) | [Before](before-cards-768.png) / [After](after-cards-768.png) |
| 1024 | [Before](before-home-1024.png) / [After](after-home-1024.png) | [Before](before-cards-1024.png) / [After](after-cards-1024.png) |
| 1440 | [Before](before-home-1440.png) / [After](after-home-1440.png) | [Before](before-cards-1440.png) / [After](after-cards-1440.png) |
| 1920 | [Before](before-home-1920.png) / [After](after-home-1920.png) | [Before](before-cards-1920.png) / [After](after-cards-1920.png) |

[Computed measurements](measurements.json) accompany the captures. Chrome 152, DPR 1, light theme; viewport heights respectively 800/844/1024/768/900/1080px. These are desktop-browser viewport simulations.

## Verification and limits

- Disposable Python 3.14.6 container: baseline and after `mkdocs build --strict` passed; `pytest` **20 passed**; Ruff passed. Used pinned Material 9.7.7, minify 0.8.0, pytest 8.4.2 and Ruff 0.14.4. No dependency changes. Both new generated-HTML tests fail on the baseline as expected.
- Also checked 320, 639/640, 959/960, 1023/1024/1025, 1199/1200, 1279/1280, 1599/1600/1601 and 1999/2000px. Name stays on one line, header controls stay in bounds, body stays within 17–19px, and there is no document overflow.
- Keyboard order remains brand, Home, Blog, Notes, palette, Search. Enter/Space open [search](after-search-360.png); Escape closes it and restores trigger focus. Pointer open/close passed. For the stock unlabeled close arrow only, the test supplied a temporary accessible name/role to locate the existing label for a real pointer click; this was not a source change. The baseline could already reach the search input with Tab: this is not evidence of a baseline keyboard failure.
- Blog, Notes and the sampled article were inspected at 360/768/1440/1920px. [Phone article](after-article-360.png), [desktop code/table](after-code-table-1440.png). Phone [code](after-code-scroll-end-360.png) and [table](after-table-scroll-end-360.png) reach their far edges using their own scroll regions; scroll movement was scripted.
- **200% coverage is reflow emulation, not native browser zoom.** The approved transport's zoom shortcut/profile attempt did not change observed zoom, and it disallowed the internal settings URL. Half-sized CSS viewports with DPR 2 passed layout and keyboard-search checks: [1440 → 720 CSS px](after-zoom-reflow-1440.png), [1024 → 512](after-zoom-reflow-1024.png), [1920 → 960](after-zoom-reflow-1920.png).
- Touch-enabled viewport activation passed, but the driver dispatches mouse clicks. Real touch, native browser zoom, mobile Safari and a full screen-reader audit remain untested. These gaps must not be presented as completed device coverage.
