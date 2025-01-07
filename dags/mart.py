from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from python.create_mart import mysql_mart


with DAG(
    dag_id="mart",
    start_date=datetime(2023, 10, 11),
    catchup=False,
    schedule_interval=None,
    tags=["mart"],
) as dag:

    msql_mart = PythonOperator(
        task_id="create_mart",
        python_callable=mysql_mart
    )

msql_mart











