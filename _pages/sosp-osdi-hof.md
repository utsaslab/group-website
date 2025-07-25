---
title: "SOSP/OSDI Hall of Fame"
layout: gridlay
sitemap: false
permalink: /sosp-osdi-hof/
---

This page lists authors with the most publications in SOSP and OSDI using data from [DBLP](https://dblp.org).

<table class="table table-striped">
  <thead>
    <tr>
      <th>Rank</th>
      <th>Author</th>
      <th>Publications</th>
    </tr>
  </thead>
  <tbody>
    {% assign authors = site.data.hof | sort: 'freq' | reverse %}
    {% assign last_freq = '' %}
    {% assign rank = 0 %}
    {% assign index = 0 %}
    {% for author in authors %}
      {% assign index = index | plus: 1 %}
      {% if author.freq != last_freq %}
        {% assign rank = index %}
        {% assign last_freq = author.freq %}
      {% endif %}
      <tr>
        <td>{{ rank }}</td>
        <td><a href="{{ author.dblp }}">{{ author.name }}</a></td>
        <td>{{ author.freq }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>

