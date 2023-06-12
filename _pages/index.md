---
layout: page
title: Jardin numérique de Fabrice Liut
id: home
permalink: /
---

# Hello ! 👋

<p style="padding: 3em 1em; background: #f5f7ff; border-radius: 4px;">
  bienvenue dans mon [[jardin numérique]]. premières orientations pour votre exploration.
  découvrez comment [[Prendre soin de soi]] - [[Prendre soin du collectif]] - [[Prendre soin du monde]].
  apprenez-en plus sur les [[designs]], le concept de [[Second Brain]] et sur l'une de mes expérimentations de communauté, [[Archipel Kyosei]].
  Il y a bien plus à découvrir encore, laissez vous porter par votre curiosité...
</p>

## axes de travail et de recherche
avant tout, voici [[mon intention du moment]] qui précise pourquoi je me lève le matin, ça donne du contexte pour tout ce que je partage ensuite.

je me présente désormais comme [[bras droit]] des dirigeants, leaders et CEOs - parce que c'est avec ces humains engagés que je suis le plus utile et le plus efficace.

pour compléter les orientations principales précédentes, voilà quelques sujets qui sont au coeur de mes explorations personnelles:
- [[design régénératif]]
- [[bio-inspiration]]
- [[complexité]] - [[système complexe]]
- [[coopération]]
- [[créer un système de connaissance coopératif]]

quelques concepts, outils, méthodes, formats... qui ont émergé et qui portent ma pratique en tant que designer au quotidien:
- [[pour quoi travailler ensemble]]
- [[guidebook business as non usual]]
- [[Design circulaire sur 1 jour]]
- [[Design systémique sur 3 jours]]
- [[présentation community design 101]] - découvrir cette branche du design
- [[N'achetez plus des outils, services, produits ! Coopérez avec ceux qui les construisent !]]

je ne saurais expliquer pourquoi, mais j'ai toujours voulu tout analyser, décortiquer pour comprendre et peut-être réussir un jour à [[décoder la vie]]... et même si "je sais que je ne sais rien" cela n'enlève pas le plaisir des nouvelles découvertes.
- [[voyager dans le temps]] - c'est quoi le temps et comment bouger dedans?
- Et si [[Il n'y a pas de montagne]] ? - et pas d'objectif à atteindre?
- [[et si tout ça c'était juste un rêve]]

---

## dernières mises à jour

- [[process pour créer des contenus online]]
- [[repartir des bases du vivant]]
- [[repartir de soi et de ses émotions pour changer le monde]]
- [[Ça veut dire quoi impact pour toi]]
- [[et toi ton impact, plutôt dégénératif ou régénératif]]
- [[Prioriser la sobriété et la convivialité pour résoudre nos problèmes humains et à toutes les échelles]]
- [[Vous savez qu’il faut que votre entreprise évolue mais vous ne savez pas comment pousser ça seul]]
- [[comment écrire plus juste sur les réseaux sociaux pour des contenus plus utiles pour votre audience]]
- [[woodstock 99 pour parler d'effondrement]] - est-ce bientôt la fin du festival?
- [[comprendre ce qu'est un projet]] - parce qu'on fait tous des projets tout le temps...
- [[Echec et mat du monopole]] - petite tristesse de la société actuelle
- [[Régénérer est une direction]] - comprendre ce que veut dire régénérer
- Je partage [[Ma vision du Design en 2021]] - parce que je suis engagé à ma manière
- C'est quoi ce site, c'est quoi un [[jardin numérique]] ?
- [[Choisir avec qui et comment travailler en tant qu'indépendant]]
- [[faisons partie de nous]] - [[identité de groupe]] - [[nous avons une mission]]

---

### bac à sujets (à développer) 👇
- [[start with why but stop with why]]
- [[retrouver la confiance en l’intuition]]
- [[Exploration de l'abstraction]]
- [[se raconter des histoires]]
- [[Créer des indicateurs qualitatifs]]
- Bientôt des petits scénarios fictifs comme [[La vie en double face]]

*en vous balandant entre ces premières pages vous pourrez en découvrir d'autres qui ne sont pas accessible via cet index...
Au fil de l'[[évolutions des notes]] vous pourrez rebondir de notes en notes, à la manière d'un Wikipedia mais sur des sujets de recherche personnels et très souvent, en mutations! Je vous souhaite une belle exploration ! ⛵*

---

L'un de mes plus gros travaux en cours c'est la réalisation du [[guidebook de l'approche territoriale NEOZ]] qui adresse la transformation des territoires. *(fin d'écriture en cours)*
<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes | limit: 5 %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>

<style>
  .wrapper {
    max-width: 46em;
  }
</style>
