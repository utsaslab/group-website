---
title: "Publications by year"
layout: gridlay
sitemap: false
permalink: /publications-by-year/
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016]
---

<style>
summary.year-heading {
  font-size: 1.25rem;
  font-weight: bold;
  cursor: pointer;
  margin-top: 1rem;
}
</style>

{% for y in page.years %}
<details class="year-details">
  <summary class="year-heading">{{ y }}</summary>
  <div class="year-list">
    {% bibliography --query @*[year={{ y }}] %}
  </div>
</details>
{% endfor %}

<script>
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.year-details').forEach(function (el) {
    el.removeAttribute('open');
  });
});
</script>
