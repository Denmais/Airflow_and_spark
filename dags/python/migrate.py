import psycopg2
import mysql.connector


def connect_cursor():
    conn_dwh = psycopg2.connect(dbname="mydb",
                                user="user",
                                password="password",
                                host="db",
                                port="5432",
                                )
    return conn_dwh


def connect_cursor_mysql():
    cnx = mysql.connector.connect(user="user", password="password",
                                  host="mysql",
                                  database="db")
    return cnx


def pg_init_migration():
    pg_conn = connect_cursor()
    with open("/opt/airflow/dags/sql/post.sql") as file:
        sql_query = file.read()
    cur = pg_conn.cursor()
    cur.execute(sql_query)
    pg_conn.commit()
    pg_conn.close()


def mysql_init_migration():
    msql_conn = connect_cursor_mysql()
    with open("/opt/airflow/dags/sql/msql.sql") as file:
        sql_query = file.read()
    cur = msql_conn.cursor()
    cur.execute(sql_query)
    cur.close()
    msql_conn.close()
