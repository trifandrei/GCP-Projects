
bq query --nouse_legacy_sql \
'SELECT name,ROUND(TIMESTAMP_DIFF(updated_timestamp, created_timestamp, DAY)/30,2) as nr_months
 FROM `bigquery-public-data.libraries_io.projects`  '

