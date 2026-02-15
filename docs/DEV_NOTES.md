Netlify & GitHub Pages — Deployment notes

Netlify legacy prerendering
 - If Netlify shows: "This project is using legacy prerendering, which is being deprecated":
   1. Open Netlify → your site → Settings → Build & deploy → Legacy prerendering.
   2. Disable the legacy prerendering feature (Jekyll already outputs static HTML).
 - If you prefer, provide a `NETLIFY_AUTH_TOKEN` (with the right scopes) and I can toggle it via the Netlify API.

GitHub Pages
 - This repo contains a `docs/` folder with the generated site. You can serve it from `master/docs`:
   Settings → Pages → Build and deployment → Source → Branch: `master`, Folder: `/docs` → Save.
 - Alternatively the repository includes a GitHub Actions workflow `.github/workflows/pages-deploy.yml` which builds the site and deploys to `gh-pages` on `push` to `master`.
 - If the deploy step fails due to permission (HTTP 403), ensure in Settings → Actions → General that `Workflow permissions` allows `Read and write permissions` for `GITHUB_TOKEN`. If your organization restricts the token, provide a PAT with `repo` scope and add it as `GH_PAGES_TOKEN` secret.

Notes about automation
 - The workflow uses `ruby/setup-ruby`, `bundle install` and `peaceiris/actions-gh-pages@v3` to publish the `_site` directory.
 - The repo already contains `docs/` copy of the last built site; enabling Pages from `master/docs` is the simplest path to a live site without depending on Actions.

If you want, I can:
 - toggle Netlify prerendering via API (you must provide `NETLIFY_AUTH_TOKEN`),
 - enable Pages via the GitHub API (you must provide a PAT with `repo` scope),
 - or run a Lighthouse audit and fix remaining perf/accessibility issues.
