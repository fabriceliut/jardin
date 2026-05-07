---
layout: page
title: Tags
permalink: /tags
---

{% assign maturity_list = "seed,wip,v1,updated,evergreen,stale" | split: "," %}
{% assign type_list     = "note,article,moc,log,ressource"       | split: "," %}
{% assign workflow_list = "to_update,to_refactor,to_publish,candidate_post" | split: "," %}
{% assign taxonomy_all  = "seed,wip,v1,updated,evergreen,stale,note,article,moc,log,ressource,to_update,to_refactor,to_publish,candidate_post" | split: "," %}

{% assign all_tags = "" | split: "" %}
{% for note in site.notes %}
  {% for tag in note.tags %}
    {% unless all_tags contains tag %}
      {% assign all_tags = all_tags | push: tag %}
    {% endunless %}
  {% endfor %}
{% endfor %}
{% assign all_tags = all_tags | sort %}

{% assign topic_tags = "" | split: "" %}
{% for tag in all_tags %}
  {% unless taxonomy_all contains tag %}
    {% assign topic_tags = topic_tags | push: tag %}
  {% endunless %}
{% endfor %}

<div class="tags-page tags-v2">

  <!-- Filter module -->
  <div class="tags-filter-module">
    <input type="search" id="tag-search" class="tags-search-input"
           placeholder="Rechercher un tag…" aria-label="Rechercher un tag" autocomplete="off">
    <div class="tags-group-pills" role="group" aria-label="Filtrer par groupe">
      <button class="tag-group-pill active" data-group="all">Tous</button>
      <button class="tag-group-pill" data-group="maturity">Maturité</button>
      <button class="tag-group-pill" data-group="type">Type</button>
      <button class="tag-group-pill" data-group="workflow">Workflow</button>
      <button class="tag-group-pill" data-group="topic">Thèmes</button>
    </div>
  </div>

  <p class="tags-no-results" hidden>Aucun tag ne correspond à cette recherche.</p>

  <!-- ── Maturité ── -->
  <section class="tag-group" data-group="maturity">
    <div class="tag-group-header">
      <h2 class="tag-group-title">Maturité</h2>
      <p class="tag-group-desc">Statut d'avancement de chaque note</p>
    </div>
    <div class="tag-accordions">
    {% for tag in maturity_list %}
      {% assign tagged_notes = site.notes | where_exp: "item", "item.tags contains tag" | sort: "title" %}
      {% if tagged_notes.size > 0 %}
      <details class="tag-accordion" data-tag="{{ tag }}" id="{{ tag | slugify }}">
        <summary class="tag-accordion-summary">
          <span class="tag-badge">{{ tag }}</span>
          {% if tag == "seed" %}<span class="tag-accordion-desc">Idée fraîche ou brouillon</span>
          {% elsif tag == "wip" %}<span class="tag-accordion-desc">En construction</span>
          {% elsif tag == "v1" %}<span class="tag-accordion-desc">Première version publiable</span>
          {% elsif tag == "updated" %}<span class="tag-accordion-desc">Enrichie depuis la V1</span>
          {% elsif tag == "evergreen" %}<span class="tag-accordion-desc">Note stable et fondatrice</span>
          {% elsif tag == "stale" %}<span class="tag-accordion-desc">À réviser — contenu daté</span>
          {% endif %}
          <span class="tag-accordion-count">{{ tagged_notes.size }}</span>
          <span class="tag-accordion-chevron" aria-hidden="true"></span>
        </summary>
        <ul class="tag-notes-list">
          {% for note in tagged_notes %}
          <li><a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
          {% endfor %}
        </ul>
      </details>
      {% endif %}
    {% endfor %}
    </div>
  </section>

  <!-- ── Type de note ── -->
  <section class="tag-group" data-group="type">
    <div class="tag-group-header">
      <h2 class="tag-group-title">Type de note</h2>
      <p class="tag-group-desc">Rôle de la note dans le jardin</p>
    </div>
    <div class="tag-accordions">
    {% for tag in type_list %}
      {% assign tagged_notes = site.notes | where_exp: "item", "item.tags contains tag" | sort: "title" %}
      {% if tagged_notes.size > 0 %}
      <details class="tag-accordion" data-tag="{{ tag }}" id="{{ tag | slugify }}">
        <summary class="tag-accordion-summary">
          <span class="tag-badge">{{ tag }}</span>
          {% if tag == "note" %}<span class="tag-accordion-desc">Note d'idée classique</span>
          {% elsif tag == "article" %}<span class="tag-accordion-desc">Texte rédigé, proche billet</span>
          {% elsif tag == "moc" %}<span class="tag-accordion-desc">Carte / index de liens</span>
          {% elsif tag == "log" %}<span class="tag-accordion-desc">Journal, retour d'expérience</span>
          {% elsif tag == "ressource" %}<span class="tag-accordion-desc">Fiche, liens, citations</span>
          {% endif %}
          <span class="tag-accordion-count">{{ tagged_notes.size }}</span>
          <span class="tag-accordion-chevron" aria-hidden="true"></span>
        </summary>
        <ul class="tag-notes-list">
          {% for note in tagged_notes %}
          <li><a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
          {% endfor %}
        </ul>
      </details>
      {% endif %}
    {% endfor %}
    </div>
  </section>

  <!-- ── Workflow ── -->
  <section class="tag-group" data-group="workflow">
    <div class="tag-group-header">
      <h2 class="tag-group-title">Workflow</h2>
      <p class="tag-group-desc">Actions en attente sur ces notes</p>
    </div>
    <div class="tag-accordions">
    {% for tag in workflow_list %}
      {% assign tagged_notes = site.notes | where_exp: "item", "item.tags contains tag" | sort: "title" %}
      {% if tagged_notes.size > 0 %}
      <details class="tag-accordion" data-tag="{{ tag }}" id="{{ tag | slugify }}">
        <summary class="tag-accordion-summary">
          <span class="tag-badge">{{ tag }}</span>
          {% if tag == "to_update" %}<span class="tag-accordion-desc">À mettre à jour</span>
          {% elsif tag == "to_refactor" %}<span class="tag-accordion-desc">À retravailler en profondeur</span>
          {% elsif tag == "to_publish" %}<span class="tag-accordion-desc">Prête à être publiée</span>
          {% elsif tag == "candidate_post" %}<span class="tag-accordion-desc">Bonne base pour post public</span>
          {% endif %}
          <span class="tag-accordion-count">{{ tagged_notes.size }}</span>
          <span class="tag-accordion-chevron" aria-hidden="true"></span>
        </summary>
        <ul class="tag-notes-list">
          {% for note in tagged_notes %}
          <li><a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
          {% endfor %}
        </ul>
      </details>
      {% endif %}
    {% endfor %}
    </div>
  </section>

  <!-- ── Thèmes ── -->
  {% if topic_tags.size > 0 %}
  <section class="tag-group" data-group="topic">
    <div class="tag-group-header">
      <h2 class="tag-group-title">Thèmes</h2>
      <p class="tag-group-desc">Tags de contenu et d'exploration</p>
    </div>
    <div class="tag-accordions">
    {% for tag in topic_tags %}
      {% assign tagged_notes = site.notes | where_exp: "item", "item.tags contains tag" | sort: "title" %}
      {% if tagged_notes.size > 0 %}
      <details class="tag-accordion" data-tag="{{ tag }}" id="{{ tag | slugify }}">
        <summary class="tag-accordion-summary">
          <span class="tag-badge">{{ tag }}</span>
          <span class="tag-accordion-count">{{ tagged_notes.size }}</span>
          <span class="tag-accordion-chevron" aria-hidden="true"></span>
        </summary>
        <ul class="tag-notes-list">
          {% for note in tagged_notes %}
          <li><a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
          {% endfor %}
        </ul>
      </details>
      {% endif %}
    {% endfor %}
    </div>
  </section>
  {% endif %}

</div>

<script>
(function () {
  var searchInput = document.getElementById('tag-search');
  var pills = document.querySelectorAll('.tag-group-pill');
  var groups = document.querySelectorAll('.tag-group');
  var noResults = document.querySelector('.tags-no-results');
  var activeGroup = 'all';

  function applyFilters() {
    var query = searchInput.value.toLowerCase().trim();
    var anyVisible = false;

    groups.forEach(function (group) {
      var groupName = group.dataset.group;
      var groupMatches = activeGroup === 'all' || activeGroup === groupName;
      var groupHasVisible = false;

      group.querySelectorAll('.tag-accordion').forEach(function (acc) {
        var tagName = acc.dataset.tag.toLowerCase();
        var visible = groupMatches && (!query || tagName.includes(query));
        acc.hidden = !visible;
        if (visible) { groupHasVisible = true; anyVisible = true; }
      });

      group.hidden = !groupHasVisible;
    });

    noResults.hidden = anyVisible;
  }

  searchInput.addEventListener('input', applyFilters);

  pills.forEach(function (pill) {
    pill.addEventListener('click', function () {
      pills.forEach(function (p) { p.classList.remove('active'); });
      pill.classList.add('active');
      activeGroup = pill.dataset.group;
      applyFilters();
    });
  });

  // Open accordion when arriving from a #hash link
  var hash = window.location.hash;
  if (hash) {
    var target = document.querySelector(hash);
    if (target && target.tagName === 'DETAILS') { target.open = true; }
  }
})();
</script>
