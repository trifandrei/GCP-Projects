from concurrent import futures
from google.cloud import pubsub_v1

import time

project_id = "core-port-327608"
topic_id = "Fully-automated"

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_id)

for i in range(0, 5):
    data = "This is sent from code message id: "+str(i+1)

    data = data.encode("utf-8")
  
    future = publisher.publish(topic_path, data)
    print(future.result())
    time.sleep(1)

print(f"Published messages to {topic_path}.")