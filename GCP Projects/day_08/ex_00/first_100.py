from google.cloud import bigquery
from google.oauth2 import service_account


def first_100_comments():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
    SELECT score, text, creation_date
    FROM `bigquery-public-data.stackoverflow.comments`
    LIMIT 100 """)

    results = query_job.result()
    f = open("result.txt", "w")


    for row in results:

        if len(str(row.text))<=120 and len(str(row.score))<=5 :
            f.write("Score:"+str(row.score).ljust(5)+"Comment:"+str(row.text).ljust(120) +"Creation date:"+str(row.creation_date).ljust(10)+"\n")
    
    f.close()


first_100_comments()