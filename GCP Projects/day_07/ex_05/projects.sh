
bq query --nouse_legacy_sql \
'SELECT a.name, a.description,COUNT(b.dependency_project_id) As count1
FROM `bigquery-public-data.libraries_io.projects`a 
join `bigquery-public-data.libraries_io.dependencies` b
on (a.id=b.project_id)
group by  a.name ,a.description
order by  COUNT(b.dependency_project_id) desc
 LIMIT 100'

