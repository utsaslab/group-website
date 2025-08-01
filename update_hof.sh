echo "Getting data from DBLP"
curl -s https://sparql.dblp.org/sparql -H "Accept: text/tab-separated-values" -H "Content-type: application/sparql-query" --data "PREFIX dblp: <https://dblp.org/rdf/schema#>                                                                                          
                                                                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>                                                                                 
                                                                            SELECT ?name ?affiliation (COUNT(DISTINCT ?publ) as ?freq) (?pers as ?dblp) (SAMPLE(?orcids) as ?orcid) WHERE {                      
                                                                              VALUES ?stream { <https://dblp.org/streams/conf/sosp> <https://dblp.org/streams/conf/osdi> } .                                     
                                                                              ?publ dblp:publishedInStream ?stream .                                                                                             
                                                                              ?publ dblp:authoredBy ?pers .                                                                                                      
                                                                              ?pers rdfs:label ?name .                                                                                                           
                                                                              OPTIONAL { ?pers dblp:primaryAffiliation ?affiliation . }                                                                          
                                                                              OPTIONAL { ?pers dblp:orcid ?orcids . }                                                                                            
                                                                            }                                                                                                                                    
                                                                            GROUP BY ?name ?affiliation ?pers                                                                                                    
                                                                            ORDER BY DESC(?freq)                                                                                                                 
                                                                            LIMIT 120                             " > _data/hof-raw.tsv

echo "Creating new CSV file"
python update_hof_from_tsv.py

