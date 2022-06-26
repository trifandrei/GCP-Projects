from google.cloud import bigquery
from google.oauth2 import service_account
import json


def popular_file():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
        SELECT   a.display_name, COUNT(b.post_id) AS t1
        FROM
        `bigquery-public-data.stackoverflow.users` a
        INNER JOIN
        `bigquery-public-data.stackoverflow.comments` b
        ON
        (a.id=b.user_id ) 
        GROUP BY
        a.display_name
        ORDER BY t1 desc 
        LIMIT 10 """)

    results = query_job.result()
    f = open("result.txt", "w")


    for row in results:
            f.write(str(row.display_name)+"->"+str(row.t1)+" "+"comments."+"\n")
    
    f.close()


popular_file()