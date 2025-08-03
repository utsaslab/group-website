---
title: "Full Publications"
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

<div class="jumbotron">
### Preprints
{% bibliography --template bibtemplate --query @unpublished %}
</div>

<div class="jumbotron">
### Refereed conference proceedings
{% bibliography --template bibtemplate --query @inproceedings[group!=workshop] %}
</div>

<div class="jumbotron">
### Refereed journal articles
{% bibliography --template bibtemplate --query @article %}
</div>

<div class="jumbotron">
### Workshop papers
{% bibliography --template bibtemplate --query @*[group=workshop] %}
</div>
