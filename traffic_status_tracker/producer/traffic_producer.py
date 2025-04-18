from datetime import datetime
import json
from kafka import KafkaProducer
import random
import time


producer = KafkaProducer(
    bootstrap_servers="localhost:9093",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def generate_event():
    return {
        "location": random.choice(["Madrid", "Barcelona", "Sevilla"]),
        "traffic_level": random.randint(0, 100),
        "timestamp": datetime.now().isoformat(),
    }


while True:
    event = generate_event()
    producer.send("traffic-events", event)
    print(f"Enviado ({datetime.now()}):{event}")
    time.sleep(5)
