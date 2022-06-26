from concurrent import futures
from google.cloud import pubsub_v1
from typing import Callable
import time

project_id = "core-port-327608"
topic_id = "starting-with-UI"

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_id)

for i in range(0, 5):
    data = "This is sent from code message id: "+str(i+1)

    data = data.encode("utf-8")
   
    future = publisher.publish(topic_path, data)
    print(future.result())
    time.sleep(10)
print(f"Published messages to {topic_path}.")