---
title: "Team"
layout: gridlay
sitemap: false
permalink: /team/
---

## Team

## PI

{% for member in site.data.pi %}

<div class="jumbotron">
<div class="row">
<div class="col-sm-2">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-9 col-xs-12">
<h4>{% if member.website %}<a href="{{ member.website }}" target="_blank">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</h4>
<i>{{ member.info }}</i><br>

{% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %} {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %} {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %} {% if member.twitter %} <a href="https://twitter.com/{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}

<ul style="overflow: hidden">
<li> {{ member.education[0] }} </li>
<li> {{ member.education[1] }} </li>
</ul>
</div>
</div>
</div>

{% endfor %}

## Current Students and Postdocs

<div class='jumbotron'>
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}

<div class="row">
{% endif %}

<div class="col-sm-2">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-4 col-xs-12" markdown="0">
  <h4>{% if member.website %}<a href="{{ member.website }}" target="_blank">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</h4>
  <i>{{ member.info }}<br></i>

{% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
{% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
{% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %}
{% if member.twitter %} <a href="https://twitter.com/{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}

</div>
<!-- </div> -->

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}

</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}

</div>
{% endif %}
</div>

## Alumni

<div class="jumbotron">
{% assign phd_total = 0 %}
{% for a in site.data.alumni %}
  {% if a.duration contains 'PhD' %}
    {% unless a.duration contains 'co-advised' %}
      {% assign phd_total = phd_total | plus: 1 %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% assign phd_counter = phd_total %}
{% assign number_printed = 0 %}
{% for member in site.data.alumni %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}

<div class="row">
{% endif %}

<div class="col-sm-2">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
  <div class="col-sm-4 col-xs-12" markdown="0">
    <h4>{% if member.website %}<a href="{{ member.website }}" target="_blank">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</h4>
    <i>{% if member.duration contains 'PhD' %}{% unless member.duration contains 'co-advised' %}PhD #{{ phd_counter }}{% assign phd_counter = phd_counter | minus: 1 %}{% else %}{{ member.duration }}{% endunless %}{% else %}{{ member.duration }}{% endif %}<br>Role: {{ member.info }}</i>
    <ul style="overflow: hidden">
    </ul>
  </div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}

</div>
{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}

</div>
{% endif %}
</div>

## Staff

<div class="jumbotron">
{% assign number_printed = 0 %}
{% for member in site.data.staff %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}

<div class="row">
{% endif %}

<div class="col-sm-2">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-4 col-xs-12">
  <h4>{% if member.website %}<a href="{{ member.website }}" target="_blank">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</h4>
  <i>{{ member.info }}<br></i>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}

</div>
{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}

</div>
{% endif %}
</div>

