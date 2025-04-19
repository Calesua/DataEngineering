from datetime import datetime
import json
import random
import time

from kafka import KafkaProducer

from event import TrafficEvent


producer = KafkaProducer(
    bootstrap_servers="localhost:9093",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


while True:
    event = TrafficEvent(
        "location": random.choice(["Madrid", "Barcelona", "Sevilla"]),
        "traffic_level": random.randint(0, 100),
        "timestamp": datetime.now().isoformat()
        )

    producer.send(topic ="traffic-events", value=event)
    print(f"Sent ({datetime.now()}):{event}")
    time.sleep(5)
