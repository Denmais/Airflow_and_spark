from kafka import KafkaConsumer
import json
import psycopg2
import signal
import sys

# Параметры подключения к Kafka
bootstrap_servers = 'localhost:9092'
topic = 'spark-topic' 


db_host = 'localhost'
db_port = '5002'
db_name = 'mydb'
db_user = 'user'
db_password = 'password'

# Создание потребителя Kafka
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',  # Начинать чтение самого первого сообщения темы
    enable_auto_commit=True,  # Автоматически фиксировать смещения (offset'ы)
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)


# Функция для вставки данных в PostgreSQL
def insert_into_postgres(data):
    try:
        with conn.cursor() as cursor:
            insert_query = """
            INSERT INTO orders (user_id, total_amount, status)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (
                data['user_id'], data['total_amount'], data['status']
            ))
            conn.commit()
            return True  # Возвращаем True, если вставка успешна
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False  # Возвращаем False, если возникла ошибка

# Чтение данных из Kafka и запись в PostgreSQL
record_count = 0  # Счетчик успешно вставленных записей
print('start')
try:
    for message in consumer:
        data = message.value
        print(data)
        if insert_into_postgres(data):
            record_count += 1  # счетчик для справки
            print(f"Вставляем в PG сообщение: {data}")
except Exception as e:
    print(f"Error consuming messages: {e}")
finally:
    consumer.close()
    conn.close()
    print(f"Успешно обработано {record_count} записей.")  # Выводим общее количество вставленных записей (показывает после остановки кода)