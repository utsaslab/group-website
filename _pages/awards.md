---
title: "Awards"
layout: gridlay
sitemap: false
permalink: /awards/
---

<p style="font-size: 1.2rem;">Honors and awards received by our group and its members.</p>

<ul style="font-size: 1.2rem;">
{% for award in site.data.awards %}
  {% if award.paper %}
    {% assign award_name = award.name %}
    {% bibliography --template award --query @*[key={{ award.paper }}] %}
  {% else %}
    <li>{{ award.name }}</li>
  {% endif %}
{% endfor %}
</ul>

