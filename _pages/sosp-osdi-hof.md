---
title: "SOSP/OSDI Hall of Fame"
layout: gridlay
sitemap: false
permalink: /sosp-osdi-hof/
---

### Systems Research: SOSP/OSDI Hall of Fame

Authors are ranked by total number of SOSP and OSDI papers (the top conferences for systems research). Authors with same number of papers have the same rank.

For display purposes, within each rank, authors are sorted by last name. Top 100 (approximately) authors are shown.

Disclaimers: A real Hall of Fame should be determined by impact, not paper count.
Data pulled from [DBLP](https://dblp.org) using SPARQL.
Please direct all queries about data to DBLP.

Author information updated manually. Please let me know if there is a mistake.

Inspired by [ISCA Hall of Fame](http://pages.cs.wisc.edu/~arch/www/iscabibhall.html) and [MICRO Hall of Fame](http://newsletter.sigmicro.org/micro-hof.txt/view).

Updated: July 2025.

Reflects data up-to OSDI 25.

<table class="table table-striped">
  <thead>
    <tr>
      <th>Rank</th>
      <th>Author</th>
      <th>Affiliation</th>
      <th>Publications</th>
    </tr>
  </thead>
  <tbody>
    {% assign author_info = site.data["hof-authors"] %}
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
        {% assign affiliation = "" %}
        {% for info in author_info %}
          {% if info.name == author.name %}
            {% assign affiliation = info.affiliation %}
            {% break %}
          {% endif %}
        {% endfor %}
      <tr>
        <td>{{ rank }}</td>
        <td><a href="{{ author.dblp }}">{{ author.name }}</a></td>
        <td>{{ affiliation }}</td>
        <td>{{ author.freq }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>

