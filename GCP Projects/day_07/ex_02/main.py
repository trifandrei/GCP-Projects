from flask import Flask, render_template ,request, jsonify
import requests
import json


app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')


@app.route('/')
def root():
    if request.method=="GET":
      print(request.get_json())

    return render_template("index.html")
    
@app.route('/', methods=['POST'])
def get_vac():
    text = request.form['country']
    data=requests.get("https://restcountries.com/v3.1/name/{0}?fullText=true".format(text)).content

    if "404" not in str(data) :
       data2=requests.get("https://covid-api.mmediagroup.fr/v1/vaccines?country={0}".format(text)).content
      
       y=json.loads(data2)
       t=y["All"]

    
    return render_template("index2.html",value=t["people_vaccinated"])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)