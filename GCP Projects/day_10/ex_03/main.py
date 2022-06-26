from flask import Flask, render_template
from concurrent import futures
from google.cloud import pubsub_v1
from google.cloud import datastore

import time


app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')



@app.route('/')
def root():
    return "Hello"

def send_msg():
    project_id = "core-port-327608"
    topic_id = "Fully-automated"

    publisher = pubsub_v1.PublisherClient()

    topic_path = publisher.topic_path(project_id, topic_id)

    data = "This is a message from Flask"

    data = data.encode("utf-8")
  
    future = publisher.publish(topic_path, data)
    print(future.result())

    print(f"Published messages to {topic_path}.")

@app.route('/publish',methods=["POST"])
def publish():
    send_msg()
    return render_template("publish.html")

@app.route('/publish',methods=["GET"])
def publish_GET():
    return render_template("publish.html")

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    client = datastore.Client()
    task = datastore.Entity(client.key("Task"))
    task.update(
    {
        "MSG": str(message.data),
     
    }
)
    client.put(task)
    message.ack()

def recv_mesg():
    
    project_id = "core-port-327608"
    subscription_id = "my-sub-3"
    timeout = 5.0

    subscriber = pubsub_v1.SubscriberClient()

    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    
    
 

@app.route('/pull',methods=["GET"])
def pull():
    recv_mesg()
    client = datastore.Client()

    query = client.query(kind="Task")
    results = list(query.fetch())

    list1=[]
    for row in results:
        list1.append(row["MSG"])
    print(list1)
    return render_template("pull.html",value=list1,value2=len(results))

if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)