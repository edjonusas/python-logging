1. install python packages

pip install kafka-python
pip install python-decouple

2. create .env file and add info

ELK_VERSION=8.5.0
KAFKA_SERVER_HOST="localhost:9092"

3. install and run docker

docker-compose up

4. create kafka topic

kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic [topic_name]

5. Add elasticsearch template

example elsaticsearch-template-log.json

6. run script

python producer.py
