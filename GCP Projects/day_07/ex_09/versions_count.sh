
bq query --nouse_legacy_sql \
'SELECT distinct   language ,  MAX(versions_count) as max1,
 (SELECT name from `bigquery-public-data.libraries_io.projects`  WHERE    versions_count=(SELECT MAX(versions_count) FROM `bigquery-public-data.libraries_io.projects`) ) 
 FROM `bigquery-public-data.libraries_io.projects`
group by  language
order by max1 desc'

