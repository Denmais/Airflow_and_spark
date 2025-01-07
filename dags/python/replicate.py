from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Row
import os

url = "jdbc:postgresql://db:5432/mydb"
url2 = "jdbc:mysql://mysql:3306/db"

properties = {
    "user": "user",
    "password": "password",
    "driver": "org.postgresql.Driver"
}
properties2 = {
    "user": "user",
    "password": "password",
    "driver": "com.mysql.jdbc.Driver"
}
TABLES = ['users', 'productCategories', 'products', 'orders', 'orderDetails']


def replicate():
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.jars", "/opt/airflow/dags/postgresql-42.7.3.jar, /opt/airflow/dags/mysql-connector-java-8.0.13.jar") \
        .getOrCreate()

    for table in TABLES:

        df = spark.read.\
            jdbc(url=url, table=f"public.{table}", properties=properties)

        df.show()

        df.select(['*'])\
            .write.jdbc(url=url2, table=f"{table}", properties=properties2, mode='append')
