from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2025, 8, 10),
    schedule="@daily",
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello from Airflow!'"
    )

    task1