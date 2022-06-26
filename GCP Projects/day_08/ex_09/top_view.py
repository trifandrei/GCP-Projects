from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import datastore
from fpdf import FPDF

def topview():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
        SELECT DISTINCT a.display_name ,a.views,b.title, b.favorite_count,c.owner_display_name ,d.location
        FROM `bigquery-public-data.stackoverflow.users` a 
        JOIN 
        `bigquery-public-data.stackoverflow.stackoverflow_posts`b 
        on (a.id=b.owner_user_id )
        join `bigquery-public-data.stackoverflow.posts_answers` c 
        on (b.accepted_answer_id=c.id ) 
        JOIN `bigquery-public-data.stackoverflow.users` d
        on (c.owner_user_id=d.id )
        where  b.favorite_count=(SELECT  MAX(b.favorite_count) FROM `bigquery-public-data.stackoverflow.stackoverflow_posts`b WHERE a.id=b.owner_user_id)
        ORDER BY a.views desc  limit 15
    """)

    results = query_job.result()

    
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("| display name | average views | fav count | post title | answer user name | answer user location |")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    for row in results:
        print("| "+str(row.display_name).ljust(20)+" | "+str(row.views).ljust(15)+" | "+str(row.favorite_count).ljust(10)+" | "+str(row.title).ljust(50)+" | "+str(row.owner_display_name).ljust(20)+" | "+str(row.location).ljust(15))
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
topview()