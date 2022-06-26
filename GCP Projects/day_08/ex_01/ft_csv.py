from google.cloud import bigquery
from google.oauth2 import service_account
import csv


def csv_top10():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
    SELECT user_display_name,score 
    FROM `bigquery-public-data.stackoverflow.comments` 
    order by score desc LIMIT 10 """)

    results = query_job.result()
   

    header = ["user_display_name", "highest_score"]

    list1=[]
    list2=[]
    for row in results:
        list1.append(str(row.user_display_name))
        list2.append(str(row.score))

    file = open("result.csv", "w")
    writer = csv.writer(file)

    writer.writerow(header)
    for w in range(len(list1)):
      writer.writerow([list1[w], list2[w]])
    


csv_top10()