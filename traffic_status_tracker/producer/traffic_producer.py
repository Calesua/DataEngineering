from datetime import datetime
import json
import random
import time

from kafka import KafkaProducer

from event import TrafficEvent

# Instantiate the Kafka producer class
producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v.to_dict()).encode("utf-8"),
)


while True:
    # Instantiate the TrafficEvent class with random values
    event = TrafficEvent(
        location = random.choice(["Madrid", "Barcelona", "Sevilla"]),
        traffic_level = random.randint(0, 100),
        timestamp = datetime.now()
        )

    producer.send(topic ="traffic-events", value=event)
    print(f"Sent ({datetime.now()}):{event}")
    time.sleep(5)
