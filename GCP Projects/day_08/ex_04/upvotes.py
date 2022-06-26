from google.cloud import bigquery
from google.oauth2 import service_account
import json


def votes_file():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
        SELECT   a.display_name, a.up_votes, a.website_url 
        FROM
        `bigquery-public-data.stackoverflow.users` a
        WHERE a.website_url LIKE '%.com%'
        ORDER BY a.up_votes desc 
        LIMIT 15""")

    results = query_job.result()

    deict={row.display_name:[row.up_votes,row.website_url] for row in results }
 
    with open("result.json", 'w') as outfile:
        json.dump(deict, outfile)


votes_file()