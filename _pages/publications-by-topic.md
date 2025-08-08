---
title: "Publications by Topic"
layout: gridlay
sitemap: false
permalink: /publications-by-topic/
---

<div markdown="0">
{% for keyword in site.data.sorted_keywords %}
<details class="year-details">
  <summary class="year-heading">{{ keyword }}</summary>
  <div class="year-list">
    {% for entry in site.data.publications_by_keyword[keyword] %}
      {{ forloop.index }}. {% include publication_entry.html %}
    {% endfor %}
  </div>
</details>
{% endfor %}

<script>
function toggleBibtex(key) {
    var x = document.getElementById('a' + key);
    if (x.style.display === 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}
function toggleAbstract(key) {
    var x = document.getElementById('b' + key);
    if (x.style.display === 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}
</script>
</div>
