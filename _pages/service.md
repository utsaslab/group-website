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
    {% for service in site.data.current_service %}
      <div class="service-item">
        <div class="service-content">{% include service_entry.html service=service %}</div>
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
    {% for service in site.data.upcoming_service %}
      <div class="service-item">
        <div class="service-content">{% include service_entry.html service=service %}</div>
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
        <h4 style="font-size: 1.0rem; font-weight: 600; margin-left: 20px;">{{ role }}</h4>
        {% for service in services %}
          <div class="service-item" style="margin-left: 40px;">
            <div class="service-content">{% include service_entry.html service=service %}</div>
          </div>
        {% endfor %}
      {% endfor %}
    {% endfor %}
  </div>
</details>
{% endif %}

</div>
