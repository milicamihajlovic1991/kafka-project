__author__ = 'milicamihajlovic1991@gmail.com'
__desc__ = "This script is used to send dummy data to Kafka user_topic (producer) and print the data"

from kafka import KafkaProducer
from datagenerator.data import get_user_data
import json
import time


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=json_serializer)

if __name__ == '__main__':
    i = 0
    while i < 10:
        user = get_user_data()
        print(user)
        try:
            producer.send('user_topic', user)
            time.sleep(2)
            i += 1
        except (ValueError, Exception):
            print(f"Something gets wrong with {user}")

producer.close()
