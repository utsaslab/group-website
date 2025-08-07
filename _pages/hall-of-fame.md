---
title: "SOSP/OSDI Hall of Fame"
layout: gridlay
sitemap: false
permalink: /hall-of-fame/
nav: true
---

### Systems Research: SOSP/OSDI Hall of Fame

Authors are ranked by total number of SOSP and OSDI papers (the top conferences for systems research). Several authors can share the same rank and the next rank is incremented by one.

For display purposes, authors sharing the same rank are sorted by last name. The list shows the top 100 authors and includes anyone tied with the last ranked author.

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
      <th>Last 5 Years</th>
    </tr>
  </thead>
  <tbody>
    {% assign author_info = site.data["hof-authors"] %}
    {% assign authors_sorted = site.data.hof | sort: 'freq' | reverse %}
    {% assign total_authors = authors_sorted | size %}
    {% assign authors_by_name = authors_sorted | sort: 'last' %}
    {% assign groups = authors_by_name | group_by: 'freq' | sort: 'name' | reverse %}
    {% assign rank = 0 %}
    {% for group in groups %}
      {% assign rank = rank | plus: 1 %}
      {% for author in group.items %}
        {% assign affiliation = "" %}
        {% for info in author_info %}
          {% if info.name == author.name %}
            {% assign affiliation = info.affiliation %}
            {% break %}
          {% endif %}
        {% endfor %}
        <tr>
          <td>{{ rank }}</td>
          <td><a href="{{ author.dblp }}">{{ author.name }}</a>{% assign lastfive = author.lastfive | plus: 0 %}{% if lastfive >= 15 %} 🚀{% elsif lastfive >= 10 %} 🔥🔥{% elsif lastfive >= 5 %} 🔥{% endif %}</td>
          <td>{{ affiliation }}</td>
          <td>{{ author.freq }}</td>
          <td>{{ author.lastfive }}</td>
        </tr>
      {% endfor %}
    {% endfor %}
  </tbody>
</table>

### Top Institutions

This table lists groups authors in the above table by institution and displays the top 10 institutions. 

<table class="table table-striped">
  <thead>
    <tr>
      <th>Institution</th>
      <th>Authors</th>
    </tr>
  </thead>
  <tbody>
    {% assign author_info = site.data["hof-authors"] %}
    {% assign affiliation_groups = author_info | where_exp: "item", "item.affiliation != ''" | group_by: "affiliation" | sort: "size" | reverse %}
    {% if affiliation_groups.size > 9 %}
      {% assign tenth_size = affiliation_groups[9].size %}
    {% else %}
      {% assign tenth_size = 0 %}
    {% endif %}
    {% for group in affiliation_groups %}
      {% if forloop.index <= 10 or group.size == tenth_size %}
        <tr>
          <td>{{ group.name }}</td>
          <td>{{ group.size }}</td>
        </tr>
      {% else %}
        {% break %}
      {% endif %}
    {% endfor %}
  </tbody>
</table>

