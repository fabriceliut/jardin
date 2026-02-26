# Changelog — redesign ready to deploy

All notable changes made for the redesign are recorded here.

## [Unreleased]
- Fixed TOC (Sommaire): links are now simple anchor links with smooth scroll, no tooltip on hover.
  - `link-previews.html`: skip links inside `.toc` to prevent tooltip popup.
  - `note.html`: TOC links use `scrollIntoView({ behavior: 'smooth' })` for smooth navigation.
  - `_typography.scss`: added `scroll-margin-top` on headings so they don't stick to viewport top.
- Reworked primary stylesheet (`_sass/_style.scss`) to a minimal, readable, accessible design:
  - System fonts, improved typographic scale, responsive `clamp()` sizes, `max-width: 85ch` wrapper.
  - Improved paragraph rhythm, headings spacing, lists, tables, blockquotes, code and pre styling.
  - Focus styles using `:focus-visible` for accessibility.
- Cleaned code block styles in `_sass/_code.scss` (no negative margins, consistent font size).
- Preload stylesheet and lazy-load images in `_includes/head.html` for better perceived performance.
- Simplified nav (`_includes/nav.html`) and semantic footer (`_includes/footer.html`).
- Added `Dockerfile` and `README.DEV.md` with instructions to preview the site locally in a container.
- Added GitHub Actions workflow `.github/workflows/jekyll-build.yml` to validate site builds on push/PR.

## Notes before pushing live
- Netlify is already configured via `netlify.toml` (build command: `jekyll build --trace`, publish `_site`).
- If you use GitHub Pages, enable a deployment action or use the `gh-pages` branch. CI will validate the build.
- Run the Docker preview locally to check visuals if your host Ruby env is problematic.
