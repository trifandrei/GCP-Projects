from flask import Flask, render_template
from datetime import datetime
import mysql.connector
from mysql.connector.constants import ClientFlag

app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')

@app.route('/')
def root():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   
    config = {
    'user': 'root',
    'password': '123456',
    'host': '35.234.83.32',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
    }
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor() 
    cursor.execute('CREATE DATABASE IF NOT EXISTS testdb')
    cnxn.close()  

    config['database'] = 'testdb'  
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS time_date ("
               "id int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
               "time_STRING VARCHAR(255))")

    cnxn.commit()
    
    query = ("INSERT INTO time_date (time_STRING) VALUES ( %s)")
    cursor.execute(query, (dt_string,))
    cnxn.commit()
    

    cursor.execute("SELECT * FROM time_date order by id desc limit 20")
    myresult = cursor.fetchall()
    
    if len(myresult)>20:
        cursor.execute("delete from time_date order by id asc limit 1")
    return render_template("index.html",value=dt_string,value2=myresult,len=len(myresult))


if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)