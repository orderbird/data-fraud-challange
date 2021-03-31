from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def hello(ds):
 print(f'Hello world, have a great {ds}!')


dag = DAG('hello_world',
         description='Hello world example',
         schedule_interval='0 12 * * *',
         start_date=datetime(2015, 3, 14),
         catchup=False)

with dag:
    hello_operator = PythonOperator(task_id='hello_task', 
                                    python_callable=hello)
    list_operator = BashOperator(task_id='list_task', 
                                 bash_command='ls -la /opt/airflow/data')
    hello_operator >> list_operator
