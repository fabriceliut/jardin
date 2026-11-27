---
layout: page
title: Rechercher
permalink: /search
id: search
---

<div class="search-wrapper">
  <input
    type="search"
    id="search-input"
    class="search-input"
    placeholder="Rechercher une note…"
    autocomplete="off"
    autofocus
  />
  <div id="search-results" class="search-results"></div>
  <p id="search-status" class="search-status" role="status"></p>
</div>

<script>
(function() {
  let notes;
  let loadFailed = false;
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  const status = document.getElementById('search-status');
  const params = new URLSearchParams(window.location.search);
  input.value = params.get('q') || '';

  function normalize(text) {
    return text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }

  function search() {
    const query = input.value.trim();
    const words = normalize(query).split(/\s+/).filter(word => word.length > 1);
    results.replaceChildren();
    status.textContent = '';
    if (!words.length) return;
    if (!notes) {
      status.textContent = loadFailed ? 'Erreur de chargement de l’index.' : 'Chargement de l’index…';
      return;
    }

    const matches = [];
    for (const note of notes) {
      if (!words.every(word => note.normalizedTitle.includes(word) || note.normalizedText.includes(word))) continue;
      const score = words.reduce((sum, word) => sum + (note.normalizedTitle.includes(word) ? 3 : 1), 0);
      matches.push({ note, score });
    }
    matches.sort((a, b) => b.score - a.score);
    const shown = matches.slice(0, 20);
    status.textContent = !shown.length
      ? 'Aucun résultat pour « ' + query + ' »'
      : shown.length < matches.length
        ? shown.length + ' résultats affichés sur ' + matches.length
        : shown.length + (shown.length === 1 ? ' résultat' : ' résultats');

    for (const { note } of shown) {
      const link = document.createElement('a');
      link.className = 'search-result-card';
      link.href = note.url;
      const title = document.createElement('span');
      title.className = 'search-result-title';
      highlight(title, note.title, words);
      const excerpt = document.createElement('span');
      excerpt.className = 'search-result-excerpt';
      highlight(excerpt, note.excerpt, words);
      link.append(title, excerpt);
      results.append(link);
    }
  }

  function highlight(element, text, words) {
    const escaped = words.map(word => word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
    const regex = new RegExp(escaped.join('|'), 'gi');
    let start = 0;
    for (const match of text.matchAll(regex)) {
      element.append(text.slice(start, match.index));
      const mark = document.createElement('mark');
      mark.textContent = match[0];
      element.append(mark);
      start = match.index + match[0].length;
    }
    element.append(text.slice(start));
  }

  let timer;
  input.addEventListener('input', function() {
    clearTimeout(timer);
    timer = setTimeout(search, 150);
  });

  search();
  fetch('{{ site.baseurl }}/search.json')
    .then(response => {
      if (!response.ok) throw new Error('Index inaccessible');
      return response.json();
    })
    .then(data => {
      notes = data.map(note => ({
        ...note,
        normalizedTitle: normalize(note.title),
        normalizedText: normalize(note.text || note.excerpt || '')
      }));
    })
    .catch(() => { loadFailed = true; })
    .finally(search);
})();
</script>
