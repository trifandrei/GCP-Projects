from google.cloud import bigquery
from google.oauth2 import service_account
import json


def votes_file():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
        SELECT location, AVG(a.reputation)as t1, a.display_name FROM `bigquery-public-data.stackoverflow.users` a 
        group by  a.display_name,location ,a.reputation

        having  a.reputation>=t1
        order by t1 desc limit 10
    """)

    results = query_job.result()

    deict={row.location:{row.t1:[row.display_name]} for row in results }
 
    with open("result.json", 'w') as outfile:
        json.dump(deict, outfile)


votes_file()