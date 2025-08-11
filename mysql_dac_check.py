from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator
from datetime import datetime

def query_mysql():
    hook = MySqlHook(mysql_conn_id='mysql_default')
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    results = cursor.fetchall()
    print("Tables in MySQL database:")
    for row in results:
        print(row)
    cursor.close()
    conn.close()

with DAG(
    dag_id='example_mysql_connection',
    start_date=datetime(2025, 1, 1),
    schedule=None,  # updated: no schedule, only manual trigger
    catchup=False,
    tags=['example'],
) as dag:
    run_query = PythonOperator(
        task_id='query_mysql',
        python_callable=query_mysql,
    )
