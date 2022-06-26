
bq query --nouse_legacy_sql \
'SELECT a.language,COUNT(language) AS t1
FROM `bigquery-public-data.libraries_io.projects`a 
group by    a.language
order by  COUNT(a.language) desc
 LIMIT 15'

