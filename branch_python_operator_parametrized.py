"""
DAG with parametrized BranchPythonOperator.

Tested on: v2.1.0
"""

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.dates import days_ago


def branch_decision(myvar, tasks):
    return tasks if myvar else []


dag = DAG(
    dag_id='branch_python_operator',
    schedule_interval=None,
    start_date=days_ago(0),
    catchup=False
)

dummy = DummyOperator(
    task_id='dummy',
    dag=dag
)

branch = BranchPythonOperator(
    task_id='branch',
    python_callable=branch_decision,
    op_kwargs={
        'myvar': 0,
        'tasks': dummy.task_id
    },
    dag=dag
)

branch >> dummy
