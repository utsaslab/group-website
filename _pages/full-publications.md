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

{% assign preprints = site.bibliography | where: 'type', 'unpublished' %}
{% unless preprints == empty %}
<details class="jumbotron">
<summary><h3>Preprints</h3></summary>
{% bibliography --template bibtemplate --query @unpublished %}
</details>
{% endunless %}

{% assign conf = site.bibliography | where_exp: 'e', "e.type == 'inproceedings' and e.group != 'workshop'" %}
{% unless conf == empty %}
<details class="jumbotron">
<summary><h3>Refereed conference proceedings</h3></summary>
{% bibliography --template bibtemplate --query @inproceedings{group != 'workshop'} %}
</details>
{% endunless %}

{% assign journal = site.bibliography | where: 'type', 'article' %}
{% unless journal == empty %}
<details class="jumbotron">
<summary><h3>Refereed journal articles</h3></summary>
{% bibliography --template bibtemplate --query @article %}
</details>
{% endunless %}

{% assign workshop = site.bibliography | where: 'group', 'workshop' %}
{% unless workshop == empty %}
<details class="jumbotron">
<summary><h3>Workshop papers</h3></summary>
{% bibliography --template bibtemplate --query @*{group = 'workshop'} %}
</details>
{% endunless %}
