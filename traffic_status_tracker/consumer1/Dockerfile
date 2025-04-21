FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y netcat-openbsd
RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "kafka", "9092", "--", "python", "consumer.py"]