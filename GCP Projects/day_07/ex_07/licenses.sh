
bq query --nouse_legacy_sql \
'SELECT  DISTINCT licenses ,count(*) as nr FROM `bigquery-public-data.libraries_io.projects` 
group by licenses order by nr desc  '

