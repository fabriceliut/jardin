# Jardin Liut.

Mon jardin numérique — un espace ouvert où je partage mes idées, méthodes et découvertes.

🌱 **[jardin.liut.me](https://jardin.liut.me)**

Basé sur le template [digital-garden-jekyll-template](https://github.com/maximevaillancourt/digital-garden-jekyll-template) de [@maximevaillancourt](https://github.com/maximevaillancourt). N'hésitez pas à fork !

---

## Fonctionnalités

- **Jekyll 4.4** — générateur de site statique
- **Liens Obsidian** — syntaxe `[[wikilinks]]` avec backlinks automatiques, embeds `![[image.png]]`, transclusion `![[note]]` et résolution des `aliases:` front matter
- **Tags navigables** — badges par note, page `/tags` listant toutes les notes par tag
- **Aperçu au survol** — tooltips sur les liens internes (fetch + DOMParser, sans iframe)
- **Graphe de notes** — visualisation D3.js des connexions entre notes (chargement lazy)
- **Recherche instantanée** — recherche client-side avec index JSON, accents normalisés, résultats surlignés
- **Table des matières** — générée automatiquement, repliable (composant `<details>`)
- **Dark mode** — 3 états (auto / sombre / clair), persisté en localStorage, sans flash (FOUC)
- **Flux Atom** — feed RSS personnalisé des 20 dernières notes modifiées
- **SEO complet** — Open Graph, Twitter Cards, JSON-LD, sitemap, canonical, `robots.txt`
- **Accessibilité** — `lang="fr"`, skip link, `aria-label`, `aria-current`, `focus-visible`, `prefers-reduced-motion`
- **Design responsive** — typographie fluide (`clamp`), grille adaptative (sidebar 260px fixe), navigation glassmorphism
- **Pagination** — bouton "Voir plus" sur la page d'accueil (30 notes, 10 visibles par défaut)
- **Performance** — fonts async, WebP avatar, cache Netlify optimisé, `overflow-x: clip`, CSS versionné par build

## Stack technique

| Composant | Détail |
|-----------|--------|
| Générateur | Jekyll 4.4.1, Ruby 3.3 |
| Police | Plus Jakarta Sans (graisses : 400, 600, 700, 800) — async |
| Styles | SCSS modulaire (11 partials), `@use`, CSS custom properties |
| Graphe | D3.js v5.16.0 |
| Déploiement | Netlify (auto sur push `master`) |
| Plugins | `jekyll-last-modified-at`, `jekyll-sitemap`, `bidirectional_links_generator.rb`, `open_external_links_in_new_tab.rb` |
| Assets | Avatar WebP (78 KB via `<picture>`), images lazy-loaded |

## Architecture SCSS

```
_sass/
├── _tokens.scss      # Design tokens, dark mode, reset, body, wrapper
├── _nav.scss         # Navigation, glassmorphism, hamburger
├── _typography.scss  # Headings, liens, code, blockquotes, tables, images
├── _content.scss     # Grille note (sidebar 260px), backlinks, tooltips, tags, transclusion
├── _homepage.scss    # Intro-card, grille récente, "Voir plus"
├── _toc.scss         # Table des matières (details/summary)
├── _footer.scss      # Footer
├── _search.scss      # Page recherche
├── _utilities.scss   # Accessibilité, skip-link, graphe, page-content
├── _code.scss        # Coloration syntaxique
└── _normalize.scss   # Reset navigateur
```

## Installation locale

```bash
# Avec Docker
docker build -t jardin-jekyll .
docker run --rm -it -p 4000:4000 -v "$PWD":/srv/jekyll jardin-jekyll

# Ou directement avec Bundler
bundle install
bundle exec jekyll serve --livereload
```

Le site sera accessible sur `http://localhost:4000`.

## Déploiement

Le site se déploie automatiquement sur Netlify à chaque push sur `master`.

[![Netlify Status](https://api.netlify.com/api/v1/badges/8cfa8785-8df8-4aad-ad35-8f1c790b8baf/deploy-status)](https://app.netlify.com/sites/digital-garden-jekyll-template/deploys)

## Note sur GitHub Pages

GitHub Pages ne supporte que partiellement ce template : le plugin custom `bidirectional_links_generator.rb` (graphe + wikilinks) n'est pas compatible par défaut. Utilisez Netlify ou buildez localement puis poussez le résultat.

## Licence

Le code source est disponible sous [licence MIT](LICENSE.md).
