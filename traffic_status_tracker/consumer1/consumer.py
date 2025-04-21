import json

from kafka import KafkaConsumer


consumer1 = KafkaConsumer(
    bootstrap_servers="kafka:9092",
    client_id ="consumer1",
    group_id="traffic-status-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
    )


consumer1.subscribe(topics=["traffic-events"])

print("Connected. Waiting for messages...")

for message in consumer1:
    print("Received:", message.value)

# if bootstrap_connected():
#     print("Connected to Kafka broker")
# else:
#     print("Failed to connect to Kafka broker")