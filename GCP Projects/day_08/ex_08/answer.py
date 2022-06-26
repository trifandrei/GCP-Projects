from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import datastore
from fpdf import FPDF

def answar_post():

    credentials = service_account.Credentials.from_service_account_file('/home/trifandrei/day_08/ex_00/core-port-327608-91362b46a210.json')

    project_id = 'core-port-327608'
    client = bigquery.Client(credentials= credentials,project=project_id)   

    query_job = client.query("""
        SELECT DISTINCT a.title,a.answer_count,b.body, 
        TIMESTAMP_DIFF(b.creation_date,a.creation_date, MINUTE) AS min1
        FROM `bigquery-public-data.stackoverflow.posts_questions` a 
        JOIN 
        `bigquery-public-data.stackoverflow.stackoverflow_posts` c
        ON (a.id=c.id  )
        JOIN `bigquery-public-data.stackoverflow.posts_answers` b
        ON ( b.id= c.accepted_answer_id )
        order by answer_count desc LIMIT 15
    """)

    results = query_job.result()

    pdf = FPDF()

    for row in results:  
  
        pdf.add_page()
     
        pdf.set_font("Arial", size = 24)
        
        pdf.cell(250, 10, txt = str(row.title), 
                ln = 1, align = 'C')

        pdf.set_font("Arial", size = 12)
        pdf.set_text_color( 255,0, 0)
        pdf.cell(20, 10, txt = str(row.body), 
                ln = 10, align = 'L')

        pdf.set_font("Arial", size = 12)
        pdf.set_text_color( 0,255, 0)
        pdf.cell(20, 10, txt = str(row.min1), 
                ln = 1, align = 'L')
        
    pdf.output("PDF1.pdf")   
    

answar_post()