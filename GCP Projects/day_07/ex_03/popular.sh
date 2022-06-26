
bq query --nouse_legacy_sql \
'SELECT name, description, sourcerank, language 
FROM `bigquery-public-data.libraries_io.projects_with_repository_fields`
ORDER BY    sourcerank DESC 
LIMIT 15'