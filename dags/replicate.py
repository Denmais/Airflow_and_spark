from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

from python.replicate import replicate


with DAG(
    dag_id="replicate",
    start_date=datetime(2023, 12, 11),
    catchup=False,
    schedule_interval=None,
    tags=["replicate"],
) as dag:

    spark_replicate = PythonOperator(
        task_id="spark_replicate",
        python_callable=replicate
    )

spark_replicate
