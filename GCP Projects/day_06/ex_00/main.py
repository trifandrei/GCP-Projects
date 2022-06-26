from flask import Flask, render_template ,request, jsonify
from flask import make_response
import pdfkit
from google.cloud import datastore
import json
import re
import io, csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')


@app.route('/')
def root():
    return "Hy"


@app.route('/user/add',methods=['POST'])
def add():

   client = datastore.Client()
   key = client.key("Management")
   entity = datastore.Entity(key=key)
   data=request.get_json()
   entity.update(data)
   client.put(entity)

   return jsonify(data),200
    
@app.route('/user/list',methods=['GET'])
def get_all():
    
    client = datastore.Client()
    query = client.query(kind="Management")
    query = client.query()
    results = list(query.fetch())
    jsonString = json.dumps(results)
    
    return jsonString


@app.route('/user/<int:id>', methods=['GET'])
def get_by_id(id):

    client = datastore.Client()
    query = client.query(kind="Management")
    query.add_filter('id', "=",id)
    results = list(query.fetch())
    jsonString = json.dumps(results)
    json_formatted_str = json.dumps(jsonString, indent=2)
    
    return  json_formatted_str, 200

@app.route("/pdf/users",methods=['GET'])
def pdf_gen():

    item=get_all()
    str1 = "" 

    for ele in item: 
        str1 += ele  


    pars = re.split(', |{|}|[|]', str1)
   
    str2=""
    for t in pars:
     
        if "email" in t:
            rez=t.split(":")
            str2 =str2+","+rez[1]
    
    rez=re.split(',', str2)
    html = render_template("index.html", value=rez)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response

@app.route("/csv/<min_id>/<max_id>",methods=['GET'])
def csv_gen(min_id,max_id):

    item=get_all()
    rez = []
    
    pars = re.split(', |{|}|[|]| ', item)

    for i in range(1,len(pars)-1):
      print(pars[i])
      if "id" in pars[i] or  "name" in pars[i]:
        rez.append(pars[i+1])
    
    new_rez_index=[]
    new_rez_name=[]
    for i in range(0,len(rez)):
        if rez[i].isnumeric():
            new_rez_index.append(int(rez[i]))
        else:
            new_rez_name.append(rez[i])
        
    print(new_rez_index)
    print(new_rez_name)
    final_rez=[]
    for i in range(0,len(new_rez_index)):
        if new_rez_index[i]>=int(min_id) and new_rez_index[i]<=int(max_id):
            final_rez.append(new_rez_name[i])

    dest = io.StringIO()
    cw = csv.writer(dest,dialect='excel')
    cw.writerows([final_rez])
    output = make_response(dest.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route("/html/another_page",methods=['GET'])
def get_info():
    url = "https://developer.mozilla.org/en-US/docs/Web/HTTP."
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
   
   
    soup = BeautifulSoup( html, 'html.parser')
    f = open("/home/trifandrei/day_06/ex_01/app/templates/public/index2.html", "w")
    f.write(soup.prettify())       
    return render_template("index2.html"),200 

@app.route("/author",methods=['GET'])
def get_img():
    url = "https://developer.mozilla.org/en-US/docs/Web/HTTP."
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
   
    soup = BeautifulSoup( html, 'html.parser')

    images = soup.findAll('img')

    
    if images!=[]:  
        return "",200
    else:
        return "",404

@app.route("/pdf/secure/users",methods=['GET'])
def pdf_gen_small():

    item=get_all()
    str1 = "" 

    for ele in item: 
        str1 += ele  


    pars = re.split(', |{|}|[|]', str1)
   
    str2=""
    for t in pars:
     
        if "email" in t:
            rez=t.split(":")
            str2 =str2+","+rez[1]
    
    rez=re.split(',', str2)
    html = render_template("index.html", value=rez)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)