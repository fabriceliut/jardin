---
layout: page
title: Jardin numérique de Fabrice Liut
id: home
permalink: /
---

# Hello ! 👋

<p class="intro-box">
  Bienvenue dans mon [[jardin numérique]]. Ici, je partage mes idées, mes méthodes et mes découvertes pour [[Prendre soin de soi]], [[Prendre soin du collectif]] et [[Prendre soin du monde]]. Ce jardin, c'est un espace ouvert où vous pouvez piocher des ressources concrètes, explorer des pistes nouvelles et trouver de l'inspiration pour avancer dans vos propres projets. Laissez-vous guider par votre curiosité, il y a sûrement un sujet qui résonnera avec vos envies ou vos questions du moment. 👇
</p>

<span class="section-label">Dernières notes à jour</span>
<div class="notes-grid">
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes limit: 10 %}
    <a href="{{ site.baseurl }}{{ note.url }}" class="note-card">
      <span class="note-date">{{ note.last_modified_at | date: "%d %b %Y" }}</span>
      <span class="note-title">{{ note.title }}</span>
    </a>
  {% endfor %}
</div>

## Axes de travail et de recherche

<div class="highlight-box">
  <h3>🎯 Intention du moment</h3>
  <p>Avant tout, voici [[mon intention du moment]] qui précise pourquoi je me lève le matin, ça donne du contexte pour tout ce que je partage ensuite.</p>
</div>

<p>Je porte une casquette proche d'un "[[chief of staff]]" : j'accompagne les directions générales d'entreprises avec une posture de généraliste.</p>

<div class="feature-grid">
  <div class="feature-card">[[pourquoi travailler avec un généraliste plutôt qu'un spécialiste?]]</div>
  <div class="feature-card">[[pour quoi travailler ensemble]]</div>
  <div class="feature-card">[[Mon approche sensible avec les directions d'entreprise]]</div>
</div>

<span class="section-label">Sujets d'exploration</span>

<div class="tag-cloud">
  <span class="tag">[[régénératif]]</span>
  <span class="tag">[[bio-inspiration]]</span>
  <span class="tag">[[complexité]]</span>
  <span class="tag">[[système complexe]]</span>
  <span class="tag">[[présentation générale du design systémique]]</span>
  <span class="tag">[[simplexité]]</span>
  <span class="tag">[[metagame]]</span>
</div>

Je l'avoue, j'ai toujours eu ce réflexe de tout observer, de décortiquer le moindre détail pour essayer de comprendre comment ça marche — la vie, les relations, les organisations. C'est une démarche un peu "meta", parfois très personnelle, mais qui nourrit tout ce que je fais. Même si je sais qu'on ne peut jamais tout saisir, j'y trouve un vrai plaisir, et souvent, des idées ou des éclairages qui viennent enrichir mes accompagnements et mes projets.

Pour explorer avec moi ces univers, par ici pour tenter de [[décoder la vie]].

---

*En vous baladant entre ces premières pages vous pourrez en découvrir d'autres qui ne sont pas accessibles via cet index...
Au fil de l'[[évolutions des notes]] vous pourrez rebondir de notes en notes, à la manière d'un Wikipedia mais sur des sujets de recherche personnels et très souvent, en mutations ! Je vous souhaite une belle exploration ! ⛵*
