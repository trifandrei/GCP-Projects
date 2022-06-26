from flask import Flask, render_template ,request, jsonify
from google.cloud import datastore
import json


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
    json_formatted_str = json.dumps(jsonString, indent=2)
    
    return jsonString, 200


@app.route('/user/<int:id>', methods=['GET'])
def get_by_id(id):

    client = datastore.Client()
    query = client.query(kind="Management")
    query.add_filter('id', "=",id)
    results = list(query.fetch())
    jsonString = json.dumps(results)
    json_formatted_str = json.dumps(jsonString, indent=2)
    
    return  json_formatted_str, 200

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_by_id(id):

    client = datastore.Client()
    key = client.key("Management")
    entity = datastore.Entity(key=key)

    query = client.query(kind="Management")
    query.add_filter('id', "=",id)
    results = list(query.fetch())

    
    entity.update(results[0])
    client.delete(results[0].key)
    
    return "Delete success", 200

@app.route('/user/<int:id>', methods=['PUT'])
def update_by_id(id):

    client = datastore.Client()
    key = client.key("Management")
    entity = datastore.Entity(key=key)

    query = client.query(kind="Management")
    query.add_filter('id', "=",id)
    results = list(query.fetch())
   
    data = request.get_json()
    new_email = data.get('email', '')
    new_name = data.get('name', '')


    entity.update(results[0])
    entity.update({'email': new_email, 'name':new_name})
  
   
    client.put(entity)
    
    return "Update success", 200

@app.route('/user/<int:id>', methods=['PATCH'])
def correct_by_id(id):

    client = datastore.Client()
    key = client.key("Management")
    entity = datastore.Entity(key=key)

    query = client.query(kind="Management")
    query.add_filter('id', "=",id)
    results = list(query.fetch())
   
    data = request.get_json()
    new_email = data.get('email', '')

    entity.update(results[0])
    entity.update({'email': new_email})
  
   
    client.put(entity)
    
    return "PATCH success", 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)