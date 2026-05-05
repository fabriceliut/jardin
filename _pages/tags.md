---
layout: page
title: Tags
permalink: /tags
---

<div class="tags-page">
{% assign all_tags = "" | split: "" %}
{% for note in site.notes %}
  {% for tag in note.tags %}
    {% unless all_tags contains tag %}
      {% assign all_tags = all_tags | push: tag %}
    {% endunless %}
  {% endfor %}
{% endfor %}
{% assign all_tags = all_tags | sort %}

{% for tag in all_tags %}
<section class="tag-section" id="{{ tag | slugify }}">
  <h2 class="tag-section-title"><span class="tag-badge-large">{{ tag }}</span></h2>
  <ul class="tag-notes-list">
  {% assign tagged_notes = site.notes | where_exp: "note", "note.tags contains tag" | sort: "title" %}
  {% for note in tagged_notes %}
    <li><a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
</div>
