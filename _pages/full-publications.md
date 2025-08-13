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

{% capture preprints %}{% bibliography --template bibtemplate --query @unpublished %}{% endcapture %}
{% assign preprints = preprints | strip %}
{% if preprints contains 'publication-entry' %}

<details class="jumbotron">
<summary style="font-size: 1.2rem; font-weight: 600;">Preprints</summary>
{{ preprints }}
</details>

{% endif %}

{% capture conf %}{% bibliography --template bibtemplate --query @inproceedings[group != workshop] %}{% endcapture %}
{% assign conf = conf | strip %}
{% unless conf == "" %}

<details class="jumbotron">
<summary style="font-size: 1.2rem; font-weight: 600;">Refereed conference proceedings</summary>
{{ conf }}
</details>

{% endunless %}

{% capture journal %}{% bibliography --template bibtemplate --query @article %}{% endcapture %}
{% assign journal = journal | strip %}
{% unless journal == "" %}

<details class="jumbotron">
<summary style="font-size: 1.2rem; font-weight: 600;">Refereed journal articles</summary>
{{ journal }}
</details>

{% endunless %}

{% capture workshop %}{% bibliography --template bibtemplate --query @*[group = workshop] %}{% endcapture %}
{% assign workshop = workshop | strip %}
{% unless workshop == "" %}

<details class="jumbotron">
<summary style="font-size: 1.2rem; font-weight: 600;">Workshop papers</summary>
{{ workshop }}
</details>

{% endunless %}
