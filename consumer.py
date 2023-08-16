__author__ = 'milicamihajlovic1991@gmail.com'
__desc__ = """ This script is used to collect the data from Kafka user_topic, 
           write locally to the json file and export to minio bucket"""

from kafka import KafkaConsumer
import json
from minio import Minio
from minio.error import S3Error
import os
import pandas as pd

client = Minio("127.0.0.1:9000", "minio", "minio123", secure=False)
if not client.bucket_exists("userbucket"):
    try:
        client.make_bucket("userbucket")
    except S3Error as identifier:
        raise

if __name__ == '__main__':
    consumer = KafkaConsumer('user_topic', bootstrap_servers=['127.0.0.1:9092'],
                             auto_offset_reset='earliest', group_id=None, consumer_timeout_ms=5000)

    for user in consumer:
        user_dict = json.loads(user.value)
        df = pd.DataFrame([user_dict])
        path = './data-files/user_' + str(user_dict['user_id']) + '.json'
        df.to_json(path, orient='records')
        with open(path, 'rb') as file:
            statdata = os.stat(path)
            client.put_object('userbucket', 'user_' + str(user_dict['user_id']) + '.json', file, statdata.st_size)

    consumer.close()
