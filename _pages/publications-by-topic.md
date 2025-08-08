---
title: "Publications by Topic"
layout: gridlay
sitemap: false
permalink: /publications-by-topic/
---
<style>
.jumbotron{
    padding:3%;
    padding-bottom:10px;
    padding-top:10px;
    margin-top:10px;
    margin-bottom:30px;
}
</style>

<div markdown="0">
{% for keyword in site.data.sorted_keywords %}
<details class="jumbotron">
  <summary>{{ keyword }}</summary>
  <div class="year-list">
    {% assign total_pubs = site.data.publications_by_keyword[keyword] | size %}
    {% for entry in site.data.publications_by_keyword[keyword] %}
      {{ total_pubs | minus: forloop.index0 }}. {% include publication_entry.html %}
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
