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
  <p id="search-status" class="search-status"></p>
</div>

<script>
(function() {
  let notes = [];
  let input = document.getElementById('search-input');
  let results = document.getElementById('search-results');
  let status = document.getElementById('search-status');

  fetch('{{ site.baseurl }}/search.json')
    .then(r => r.json())
    .then(data => { notes = data; })
    .catch(() => { status.textContent = 'Erreur de chargement de l\'index.'; });

  function normalize(str) {
    return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }

  function search(query) {
    if (!query || query.length < 2) {
      results.innerHTML = '';
      status.textContent = '';
      return;
    }
    let q = normalize(query);
    let words = q.split(/\s+/).filter(w => w.length > 1);
    
    let matches = notes.filter(note => {
      let title = normalize(note.title);
      let excerpt = normalize(note.excerpt);
      let text = title + ' ' + excerpt;
      return words.every(w => text.includes(w));
    }).slice(0, 20);

    if (matches.length === 0) {
      results.innerHTML = '';
      status.textContent = 'Aucun résultat pour « ' + query + ' »';
      return;
    }

    status.textContent = matches.length + ' résultat' + (matches.length > 1 ? 's' : '');
    results.innerHTML = matches.map(note => 
      '<a class="search-result-card" href="' + note.url + '">' +
        '<span class="search-result-title">' + highlight(note.title, words) + '</span>' +
        '<span class="search-result-excerpt">' + highlight(note.excerpt, words) + '</span>' +
      '</a>'
    ).join('');
  }

  function highlight(text, words) {
    if (!text) return '';
    let result = text;
    words.forEach(w => {
      let regex = new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      result = result.replace(regex, '<mark>$1</mark>');
    });
    return result;
  }

  let timer;
  input.addEventListener('input', function() {
    clearTimeout(timer);
    timer = setTimeout(() => search(this.value.trim()), 150);
  });

  // Support ?q= query param
  let params = new URLSearchParams(window.location.search);
  if (params.get('q')) {
    input.value = params.get('q');
    // Wait for JSON to load
    setTimeout(() => search(params.get('q')), 300);
  }
})();
</script>
