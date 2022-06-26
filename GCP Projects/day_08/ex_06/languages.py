from google.cloud import bigquery
from google.oauth2 import service_account
import csv


def csv_python():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
        SELECT tags, title, body 
        FROM `bigquery-public-data.stackoverflow.stackoverflow_posts` 
        WHERE tags LIKE '%python%' LIMIT 10000""")

    results = query_job.result()
   

    header = ["post_title", "body", "all_tags."]

    file = open("result.csv", "w")
    writer = csv.writer(file)

    writer.writerow(header)
    for row in results:
      writer.writerow([str(row.title),str(row.body),str(row.tags)])
    


csv_python()