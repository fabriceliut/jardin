---
layout: page
title: Jardin numérique de Fabrice Liut
id: home
permalink: /
---
# Hello ! 👋

<div class="intro-card">
  Bienvenue dans mon [[jardin numérique]]. Ici, je partage mes idées, mes méthodes et mes découvertes pour [[Prendre soin de soi]], [[Prendre soin du collectif]] et [[Prendre soin du monde]]. Ce jardin, c'est un espace ouvert où vous pouvez piocher des ressources concrètes, explorer des pistes nouvelles et trouver de l'inspiration pour avancer dans vos propres projets. Laissez-vous guider par votre curiosité, il y a sûrement un sujet qui résonnera avec vos envies ou vos questions du moment. 👇
</div>

<div class="section-label">Dernières notes à jour</div>
<div class="recent-notes-grid">
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes limit:30 %}
    <div class="recent-note-card{% if forloop.index > 10 %} hidden-note{% endif %}">
      <div class="recent-note-date">{{ note.last_modified_at | date: "%d %b %Y" }}</div>
      <a class="recent-note-title" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </div>
  {% endfor %}
</div>
{% if recent_notes.size > 10 %}
<button class="voir-plus-btn" id="voir-plus" onclick="document.querySelectorAll('.hidden-note').forEach(function(el){el.classList.remove('hidden-note')});this.remove()">Voir plus →</button>
{% endif %}

## Axes de travail et de recherche

Avant tout, voici [[mon intention du moment]] qui précise pourquoi je me lève le matin, ça donne du contexte pour tout ce que je partage ensuite.

Je porte une casquette proche d'un "[[chief of staff]]" : j'accompagne les directions générales d'entreprises avec une posture de généraliste.

- [[pourquoi travailler avec un généraliste plutôt qu’un spécialiste?]]
- [[pour quoi travailler ensemble]]
- [[Mon approche sensible avec les directions d'entreprise]]

Pour compléter les orientations principales précédentes, voilà quelques sujets qui sont au cœur de mes explorations :
- [[régénératif]]
- [[bio-inspiration]]
- [[complexité]] — [[système complexe]]
- [[présentation générale du design systémique]]
- [[simplexité]]
- [[metagame]]

Je l'avoue, j'ai toujours eu ce réflexe de tout observer, de décortiquer le moindre détail pour essayer de comprendre comment ça marche — la vie, les relations, les organisations. C'est une démarche un peu "meta", parfois très personnelle, mais qui nourrit tout ce que je fais. Même si je sais qu'on ne peut jamais tout saisir, j'y trouve un vrai plaisir, et souvent, des idées ou des éclairages qui viennent enrichir mes accompagnements et mes projets.

Pour explorer avec moi ces univers, par ici pour tenter de [[décoder la vie]].

---

<div class="home-offre-banner">
  <div class="home-offre-content">
    <h2>🚀 Vous gérez plusieurs projets et vous perdez du temps entre les outils ?</h2>
    <p>Je construis avec vous un système centralisé sur Notion, augmenté par l'IA, pour piloter tous vos projets depuis un seul espace.</p>
    <a href="/offres" class="home-offre-btn">Découvrir l'offre Intégrateur IA →</a>
  </div>
</div>

---

*En vous baladant entre ces premières pages, vous pourrez en découvrir d'autres qui ne sont pas accessibles via cet index... Au fil de l'[[évolutions des notes]] vous pourrez rebondir de notes en notes, à la manière d'un Wikipédia mais sur des sujets de recherche personnels et très souvent, en mutations ! Je vous souhaite une belle exploration ! ⛵*
