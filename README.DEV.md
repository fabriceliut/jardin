Prévisualiser et builder localement (contenant Docker)

Commandes rapides :

# Build and run a container that serves the site (local port 4000)
```bash
docker build -t jardin-jekyll .
docker run --rm -it -p 4000:4000 -v "$PWD":/srv/jekyll jardin-jekyll
```

# Ou (si tu as `docker-compose`)
```bash
docker compose up --build
```

Notes:
- Le Dockerfile installe une version propre de Ruby et exécute `bundle exec jekyll serve`.
- Si tu préfères utiliser `bundle` localement, exécute :
```bash
bundle install
bundle exec jekyll serve --livereload
```

Conseils perf et QA visuelle :
- Vérifie les images : utilises `srcset` et `loading="lazy"`.
- Ajoute un petit `critical CSS` si tu veux optimiser le rendu perçu (header + typographie).
- Lance un audit Lighthouse (Performance, Accessibility, Best Practices) et corrige points critiques (unused CSS, large images, render-blocking resources).
