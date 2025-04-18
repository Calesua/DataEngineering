from kafka import KafkaConsumer

consumer1 = kafka.KafkaConsumer(*topics, **configs)

producer = KafkaProducer(
    bootstrap_servers="localhost:9093",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)