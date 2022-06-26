
bq query --nouse_legacy_sql \
'SELECT a.name, a.platform, a.description FROM `bigquery-public-data.libraries_io.projects`  a
join `bigquery-public-data.libraries_io.projects_with_repository_fields` b
on (a.repository_id=b.id) order by b.repository_contributors_count desc limit 1'