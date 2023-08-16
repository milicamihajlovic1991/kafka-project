This project is POC for using Kafka. Datagenerator is a package that contains data module and function get_user_data that is used to generate fake users data. 
That data is sent to the Kafka topic (producer.py). Kafka Consumer is used to grab the data and then data is ingested into Minio bucket and written into json files locally (consumer.py).
Project contains docker-compose.yml for Zookeeper, Kafka and Minio.
