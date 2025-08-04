---
title: "Publications by type"
layout: gridlay
sitemap: false
permalink: /full-publications/
years: [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
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

{% capture preprints %}
{% bibliography --template bibtemplate --query @unpublished %}
{% endcapture %}
{% unless preprints | strip == "" %}
<details class="jumbotron">
<summary><h3>Preprints</h3></summary>
{{ preprints }}
</details>
{% endunless %}

{% capture conf %}
{% bibliography --template bibtemplate --query @inproceedings[group!=workshop] %}
{% endcapture %}
{% unless conf | strip == "" %}
<details class="jumbotron">
<summary><h3>Refereed conference proceedings</h3></summary>
{{ conf }}
</details>
{% endunless %}

{% capture journal %}
{% bibliography --template bibtemplate --query @article %}
{% endcapture %}
{% unless journal | strip == "" %}
<details class="jumbotron">
<summary><h3>Refereed journal articles</h3></summary>
{{ journal }}
</details>
{% endunless %}

{% capture workshop %}
{% bibliography --template bibtemplate --query @*[group=workshop] %}
{% endcapture %}
{% unless workshop | strip == "" %}
<details class="jumbotron">
<summary><h3>Workshop papers</h3></summary>
{{ workshop }}
</details>
{% endunless %}
