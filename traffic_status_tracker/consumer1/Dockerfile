# Image with pySpark and Java already installed
FROM jupyter/pyspark-notebook

WORKDIR /app
COPY . /app

RUN mkdir -p /app/checkpoints /app/output

RUN pip install --no-cache-dir -r requirements.txt

CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1", "consumer.py"]