---
layout: page
title: Jardin numérique de Fabrice Liut
id: home
permalink: /
---

# Hello ! 👋

<p style="padding: 3em 1em; background: #f5f7ff; border-radius: 4px;">
  bienvenue dans mon [[jardin numérique]]. premières orientations pour vos explorations.
  découvrez comment [[Prendre soin de soi]] - [[Prendre soin du collectif]] - [[Prendre soin du monde]].
  apprenez-en plus sur les [[designs]], le concept de [[Second Brain]] et sur l'une de mes expérimentations de communauté, [[Archipel Kyosei]].
  Il y a bien plus à découvrir encore, laissez vous porter par votre curiosité...
</p>

<strong>Dernières notes à jour</strong>
<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes | limit: 10 %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>

## axes de travail et de recherche
avant tout, voici [[mon intention du moment]] qui précise pourquoi je me lève le matin, ça donne du contexte pour tout ce que je partage ensuite.

je porte une casquette de "chief of staff externe" : j'accompagne les directions générales d'entreprises avec une posture de génératiste.

- [[pourquoi travailler avec un généraliste plutôt qu’un spécialiste?]]
- [[pour quoi travailler ensemble]]

pour compléter les orientations principales précédentes, voilà quelques sujets qui sont au coeur de mes explorations :
- [[régénératif]]
- [[bio-inspiration]]
- [[complexité]] - [[système complexe]]
- [[présentation générale du design systémique]]
- [[simplexité]]
- [[metagame]]

je ne saurais expliquer pourquoi, mais j'ai toujours voulu tout analyser, décortiquer pour comprendre, sentir et peut-être réussir un jour à [[décoder la vie]]... et même si "je sais que je ne sais rien" cela n'enlève pas le plaisir des nouvelles découvertes.

---

*en vous balandant entre ces premières pages vous pourrez en découvrir d'autres qui ne sont pas accessible via cet index...
Au fil de l'[[évolutions des notes]] vous pourrez rebondir de notes en notes, à la manière d'un Wikipedia mais sur des sujets de recherche personnels et très souvent, en mutations! Je vous souhaite une belle exploration ! ⛵*

<style>
  .wrapper {
    max-width: 46em;
  }
</style>
