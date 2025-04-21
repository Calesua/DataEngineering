from kafka import KafkaConsumer


consumer1 = kafka.KafkaConsumer(
    bootstrap_servers="localhost:9093",
    client_id ="consumer1",
    group_id="traffic-status-group",
    )


consumer1.subscribe(topics=["traffic-events"])


if bootstrap_connected():
    print("Connected to Kafka broker")
else:
    print("Failed to connect to Kafka broker")