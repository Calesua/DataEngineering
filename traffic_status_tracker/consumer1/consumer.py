from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType, TimestampType
from pyspark.sql.functions import from_json, col, window, avg

# Spark Structured Streaming

# Create a Spark session
spark = SparkSession.builder \
    .appName("KafkaConsumer") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN") # Only show WARN and error messages (Ignore INFO and DEBUG)

# Read from Kafka topic: Starts from the earliest if no checkpoint is found (created at writeStream)
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "traffic-events") \
    .option("startingOffsets", "earliest") \
    .load()

# Transform message from bytes to dataframe
# Dataframe header: "json_str"
# Dataframe row: "string in JSON format"
df_json = df_raw.selectExpr("CAST(value AS STRING) as json_str")

# Message schema
schema = StructType() \
    .add("location", StringType()) \
    .add("traffic_level", IntegerType()) \
    .add("timestamp", TimestampType())

# Parse JSON - Dataframe with json keys as columns
df_parsed = df_json.select(from_json(col("json_str"), schema).alias("data")).select("data.*")

df_agg = df_parsed \
    .withWatermark("timestamp", "1 hour") \
    .groupBy(
        window(col("timestamp"), "1 hour", "1 hour", "30 minutes"),
        col("location")
    ) \
    .agg(avg("traffic_level").alias("avg_traffic"))
# .withWatermark("timestamp", "1 minute") Ignore data delayed more than 1 min respect to the last batch

# Write the results
query = df_agg.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("checkpointLocation", "/app/checkpoints") \
    .trigger(processingTime="5 seconds") \
    .start() \
# .format can be can be "orc", "json", "csv", etc.
# .option("path", "path/to/destination/dir")
# eg.: .option("path", "/app/output") \

query.awaitTermination()