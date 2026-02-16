# Notes de développement

## Prérequis

- Ruby ≥ 3.2, Bundler ≥ 2.4
- Ou Docker

## Lancer le site en local

```bash
# Avec Docker
docker build -t jardin-jekyll .
docker run --rm -it -p 4000:4000 -v "$PWD":/srv/jekyll jardin-jekyll

# Ou directement
bundle install
bundle exec jekyll serve --livereload
```

Le site est accessible sur `http://localhost:4000`.

## Build de production

```bash
bundle exec jekyll build
# Le résultat est dans _site/
```

## Architecture SCSS

Les styles sont répartis en 11 partials dans `_sass/`, importés par `styles.scss` :

| Partial | Contenu |
|---------|---------|
| `_tokens` | Design tokens, custom properties, dark mode mixin, reset, body |
| `_nav` | Navigation fixe, glassmorphism, logo, liens |
| `_typography` | Headings, paragraphes, listes, images, code, blockquotes, tables, liens |
| `_content` | Grille de note (3fr/1fr), backlinks, tooltips, theme toggle |
| `_homepage` | Intro-card, grille des notes récentes, bouton "Voir plus" |
| `_toc` | Table des matières repliable (`<details>`) |
| `_footer` | Footer et navigation de pied |
| `_search` | Page de recherche (input, résultats, surlignage) |
| `_utilities` | Skip link, sr-only, reduced-motion, sélection, 404, graphe |
| `_code` | Coloration syntaxique (tokens Highlight.js) |
| `_normalize` | Reset navigateur (normalize.css) |

## Dark mode

3 états cycliques : auto → sombre → clair → auto.

- Détection OS : `@media (prefers-color-scheme: dark)` sur `:root:not([data-theme="light"])`
- Override manuel : attribut `data-theme` sur `<html>`, persisté en `localStorage`
- Anti-FOUC : script inline dans `<head>` qui applique le thème avant le premier paint

## Plugins Jekyll

- **`bidirectional_links_generator.rb`** : transforme `[[wikilinks]]` en liens HTML, génère les backlinks, convertit `![[image.ext]]` en `<img>`, produit `notes_graph.json`
- **`jekyll-last-modified-at`** : date de dernière modification (basée sur git)
- **`jekyll-sitemap`** : génération automatique du sitemap.xml

## SEO

- Open Graph + Twitter Cards dans `_includes/head.html`
- JSON-LD (WebSite schema)
- Flux Atom personnalisé : `feed.xml` (20 dernières notes modifiées)
- Sitemap : `sitemap.xml` (plugin)
- Favicon emoji : 🌱

## Conseils

- Lancer un audit Lighthouse après tout changement visuel majeur
- Les images supportent `loading="lazy"` (script dans head.html)
- Le graphe D3 est chargé en lazy sur `window.load`
