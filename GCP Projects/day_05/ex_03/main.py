from flask import Flask, render_template ,request, jsonify
from google.cloud import datastore
import json

app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')

@app.route('/')
def root():
    return "Hy"


@app.route('/api/add',methods=['POST'])
def add():

   client = datastore.Client()
   key = client.key("Task")
   entity = datastore.Entity(key=key)
   data=request.get_json()
   entity.update(data)
   client.put(entity)

   return jsonify(data),200
    
@app.route('/api/list')
def contact():
    
    client = datastore.Client()
    query = client.query(kind="Task")
    query = client.query()
    results = list(query.fetch())
    jsonString = json.dumps(results)
    json_formatted_str = json.dumps(jsonString, indent=2)
    
    return jsonString, 200


if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)