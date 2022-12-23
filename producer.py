from decouple import config
import sys
from kafka import KafkaProducer

KAFKA_SERVER_HOST = config('KAFKA_SERVER_HOST')

# Open the file and read the lines
def read_file(file_url):
    try:
        with open(file_url, 'r') as file:
            data_list = file.readlines()
            return data_list
    except:
        print("Error: could not open or read file:", file_url)
        sys.exit()

# Iterate through the logs and send each one to Kafka
def send_to_kafka(data_list, topic_name):
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER_HOST])
        for data in data_list:
            producer.send(topic_name, data.encode())
            print('Success: data was send to kafka:', data)
        producer.flush()
    except:
        print('Error: producer can\'t send data to kafka')
        sys.exit()

def main():
    log_list = read_file('logs/log.txt')
    send_to_kafka(log_list, 'logs')

main()