from kafka import KafkaProducer
import json
import string
from random import choices, randrange
from time import sleep

USERS = ['Alice', 'Jane', 'Bob', 'Carol', 'John']


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

topic = 'spark-topic'


def push():
    user = randrange(1, 5, 1)
    amount = randrange(1, 4000)
    status = choices(['Done', 'Created', 'Completed', 'Deleted'])

    producer.send(topic, value={'user_id': user, 'total_amount': amount, 'status': status[0]})
    sleep(10)
    print(f"Sent message to {user}")


if __name__ == '__main__':
    try:
        while True:
            push()
    except KeyboardInterrupt:
        producer.close()
        print("exited from the producer app")
