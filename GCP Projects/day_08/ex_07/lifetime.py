from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import datastore
import json

def liftime_post():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
        SELECT
        a.title  , a.body , 
        TIMESTAMP_DIFF(a.last_activity_date,a.creation_date, HOUR) AS hours
        FROM
        `bigquery-public-data.stackoverflow.stackoverflow_posts` a
        WHERE a.title IS NOT NULL
        ORDER BY hours desc limit 15
    """)

    results = query_job.result()

    
    dict1=[{"liftime":row.hours,"body":str(row.body)[:1499], "title":str(row.title)} for row in results]

    for i in range(0,15):
        client = datastore.Client()
        key = client.key("lifetime")
        entity = datastore.Entity(key=key)
        entity.update(dict1[i])
        client.put(entity)

liftime_post()