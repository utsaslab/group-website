---
title: "Frequent Authors of SOSP and OSDI"
layout: gridlay
sitemap: false
permalink: /sosp-osdi-authors/
---

This page lists the 100 most frequent authors in the SOSP and OSDI conferences using data from [DBLP](https://dblp.org). The table below is populated dynamically when the page is loaded.

<table class="table table-striped">
  <thead>
    <tr>
      <th>Author</th>
      <th>Affiliation</th>
      <th>Publications</th>
      <th>ORCID</th>
    </tr>
  </thead>
  <tbody id="authors-table">
  </tbody>
</table>

<script>
async function loadAuthors() {
  const query = `PREFIX dblp: <https://dblp.org/rdf/schema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?name ?affiliation (COUNT(DISTINCT ?publ) as ?freq) (?pers as ?dblp) (SAMPLE(?orcids) as ?orcid) WHERE {
  VALUES ?stream { <https://dblp.org/streams/conf/osdi> <https://dblp.org/streams/conf/sosp> } .
  ?publ dblp:publishedInStream ?stream .
  ?publ dblp:authoredBy ?pers .
  ?pers rdfs:label ?name .
  OPTIONAL { ?pers dblp:primaryAffiliation ?affiliation . }
  OPTIONAL { ?pers dblp:orcid ?orcids . }
}
GROUP BY ?name ?affiliation ?pers
ORDER BY DESC(?freq)
LIMIT 100`;

  // DBLP's SPARQL endpoint does not set CORS headers, so direct requests from
  // the browser fail. Use a public CORS proxy. The proxy only forwards the
  // request, so we must POST the query and explicitly request JSON results.
  const url = 'https://cors.isomorphic-git.org/https://dblp.org/sparql';
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        Accept: 'application/sparql-results+json'
      },
      body: 'query=' + encodeURIComponent(query)
    });
    const json = await res.json();
    const rows = json.results.bindings;
    const table = document.getElementById('authors-table');
    rows.forEach(row => {
      const tr = document.createElement('tr');
      const name = row.name.value;
      const aff = row.affiliation ? row.affiliation.value : '';
      const freq = row.freq.value;
      const dblp = row.dblp.value;
      const orcid = row.orcid ? row.orcid.value : '';
      tr.innerHTML = `<td><a href="${dblp}">${name}</a></td><td>${aff}</td><td>${freq}</td><td>${orcid}</td>`;
      table.appendChild(tr);
    });
  } catch (err) {
    const table = document.getElementById('authors-table');
    table.innerHTML = '<tr><td colspan="4">Failed to load data from DBLP.</td></tr>';
  }
}

document.addEventListener('DOMContentLoaded', loadAuthors);
</script>
