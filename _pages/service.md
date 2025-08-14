---
title: "Service"
layout: gridlay
sitemap: false
permalink: /service/
---
<style>
.jumbotron{
    padding:3%;
    padding-bottom:10px;
    padding-top:10px;
    margin-top:10px;
    margin-bottom:30px;
}
.service-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 1rem;
}
.service-number {
  padding-right: 10px;
}
.year-list {
  margin-top: 10px;
}
</style>

<div markdown="0">

<!-- Current Service -->
{% if site.data.current_service.size > 0 %}
<details class="jumbotron" open>
  <summary style="font-size: 1.2rem; font-weight: 600;">Current Service</summary>
  <div class="year-list">
    {% for role_data in site.data.current_service %}
      {% assign role = role_data[0] %}
      {% assign services = role_data[1] %}
      <div class="service-item" style="margin-left: 20px;">
        <strong>{{ role }}:</strong>&nbsp;{% for service in services %}
          {% assign year = service['Start Date'] | date: '%Y' %}
          {% assign org_name = service.Organization | remove: year | strip %}
          {% if org_name contains ' ' and forloop.index > 1 %}<br>{% endif %}
          <span style="white-space: nowrap;">
          {% if service.Website %}<a href="{{ service.Website }}">{{ org_name }}</a>{% else %}{{ org_name }}{% endif %}
          </span>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </div>
    {% endfor %}
  </div>
</details>
{% endif %}

<!-- Upcoming Service -->
{% if site.data.upcoming_service.size > 0 %}
<details class="jumbotron" open>
  <summary style="font-size: 1.2rem; font-weight: 600;">Upcoming Service (in next 3 months)</summary>
  <div class="year-list">
    {% for role_data in site.data.upcoming_service %}
      {% assign role = role_data[0] %}
      {% assign services = role_data[1] %}
      <div class="service-item" style="margin-left: 20px;">
        <strong>{{ role }}:</strong>&nbsp;{% for service in services %}
          {% assign year = service['Start Date'] | date: '%Y' %}
          {% assign org_name = service.Organization | remove: year | strip %}
          {% if org_name contains ' ' and forloop.index > 1 %}<br>{% endif %}
          <span style="white-space: nowrap;">
          {% if service.Website %}<a href="{{ service.Website }}">{{ org_name }}</a>{% else %}{{ org_name }}{% endif %}
          </span>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </div>
    {% endfor %}
  </div>
</details>
{% endif %}

<!-- All Service -->
{% if site.data.all_service.size > 0 %}
<details class="jumbotron">
  <summary style="font-size: 1.2rem; font-weight: 600;">All Service</summary>
  <div class="year-list">
    {% for year_data in site.data.all_service %}
      {% assign year = year_data[0] %}
      {% assign roles = year_data[1] %}
      <h3 style="font-size: 1.1rem; font-weight: 600;">{{ year }}</h3>
      {% for role_data in roles %}
        {% assign role = role_data[0] %}
        {% assign services = role_data[1] %}
        <div class="service-item" style="margin-left: 20px;">
          <strong>{{ role }}:</strong>&nbsp;{% for service in services %}
            {% assign year_to_remove = service['Start Date'] | date: '%Y' %}
            {% assign org_name = service.Organization | remove: year_to_remove | strip %}
            {% if org_name contains ' ' and forloop.index > 1 %}<br>{% endif %}
            <span style="white-space: nowrap;">
            {% if service.Website %}<a href="{{ service.Website }}">{{ org_name }}</a>{% else %}{{ org_name }}{% endif %}
            </span>{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        </div>
      {% endfor %}
    {% endfor %}
  </div>
</details>
{% endif %}

</div>
