---
title: "Awards"
layout: gridlay
sitemap: false
permalink: /awards/
---

<p style="font-size: 1.2rem;">Honors and awards received by our group and its members.</p>

<div class="jumbotron">
<ul style="font-size: 1.2rem;">
{% for award in site.data.awards %}
  <li>{{ award.name }}</li>
{% endfor %}
</ul>
</div>

