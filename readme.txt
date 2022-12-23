1. install python packages

pip install kafka-python
pip install python-decouple

2 install and run docker 

docker-compose up

3. create kafka topic 

kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic [topic_name]

4. Add elasticsearch template 

example elsaticsearch-template-log.json

5. run script 

python producer.py