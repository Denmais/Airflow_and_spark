import mysql.connector


def connect_cursor_mysql():
    cnx = mysql.connector.connect(user="user", password="password",
                                  host="mysql",
                                  database="db")
    return cnx


def mysql_mart():
    msql_conn = connect_cursor_mysql()
    with open("/opt/airflow/dags/sql/mart.sql") as file:
        sql_query = file.read()
    print(33333)
    print(sql_query)
    cur = msql_conn.cursor()
    cur.execute(sql_query)
    cur.close()
    msql_conn.close()
