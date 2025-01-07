from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

from python.migrate import pg_init_migration, mysql_init_migration

with DAG(
    dag_id="initial_migration",
    start_date=datetime(2023, 12, 1),
    schedule_interval=None,
    catchup=False,
    tags=["migration"],
) as dag:

    postres_migrate = PythonOperator(
        task_id="postgres_migrate",
        python_callable=pg_init_migration
    )

    msql_migrate = PythonOperator(
        task_id="msql_migrate",
        python_callable=mysql_init_migration
    )

postres_migrate >> msql_migrate
