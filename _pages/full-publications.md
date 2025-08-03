---
title: "Full Publications"
layout: gridlay
sitemap: false
permalink: /full-publications/
years: [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
---
[Publications by year]({{ site.url }}{{ site.baseurl }}/publications-by-year/)

**Legend:**<br/>
<button class="btn btn-success btm-sm">PDF</button> paper<br/>
<button class="btn btn-info btm-sm">SLIDES</button> slides<br/>
<button class="btn btn-media btm-sm">VIDEO</button> video<br/>
<button class="btn btn-media btm-sm">AUDIO</button> audio<br/>
<button class="btn btn-danger btm-sm">BIB</button> BibTeX<br/>
<button class="btn btn-warning btm-sm">ABSTRACT</button> abstract

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
{% bibliography --query @unpublished %}
</div>

<div class="jumbotron">
### Refereed conference proceedings
{% bibliography --query @inproceedings[group!=workshop] %}
</div>

<div class="jumbotron">
### Refereed journal articles
{% bibliography --query @article %}
</div>

<div class="jumbotron">
### Workshop papers
{% bibliography --query @*[group=workshop] %}
</div>
