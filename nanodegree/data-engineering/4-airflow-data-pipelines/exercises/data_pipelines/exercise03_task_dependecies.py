import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def hello_world():
    logging.info("Hello World")


def addition():
    logging.info(f"2 + 2 = {2+2}")


def subtraction():
    logging.info(f"6 -2 = {6-2}")


def division():
    logging.info(f"10 / 2 = {int(10/2)}")


dag = DAG(
    "lesson1.exercise3",
    schedule_interval='@hourly',
    start_date=datetime.datetime.now() - datetime.timedelta(days=1))

hello_world_task = PythonOperator(
    task_id="hello_world",
    python_callable=hello_world,
    dag=dag)

# TODO: Define an addition task that calls the `addition` function above
addition_task = PythonOperator(
    task_id = 'addition',
    python_callable = addition,
    dag = dag)
    
# TODO: Define a subtraction task that calls the `subtraction` function above
subtraction_task = PythonOperator(
    task_id = 'subtraction',
    python_callable = subtraction,
    dag = dag)

# TODO: Define a division task that calls the `division` function above
division_task = PythonOperator(
    task_id = 'division',
    python_callable = division,
    dag = dag)

# TODO: Configure the task dependencies such that the graph looks like the following:
#
#                    ->  addition_task
#                   /                 \
#   hello_world_task                   -> division_task
#                   \                 /
#                    ->subtraction_task

hello_world_task >> addition_task
hello_world_task >> subtraction_task
subtraction_task >> division_task
addition_dir_task >> division_task 

