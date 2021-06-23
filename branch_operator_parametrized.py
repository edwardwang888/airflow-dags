"""
DAG containing a parametrized branch operator. Parameters are
provided as member variables of the class.

Note: this does not seem to be the recommended way to use a branch
operator. BranchPythonOperator can accomplish the same tasks in a
much cleaner manner.

Tested on: v2.1.0
"""

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.branch import BaseBranchOperator
from airflow.utils.dates import days_ago


class ParametrizedBranchOperator(BaseBranchOperator):
    def __init__(self, *args, myvar, downstream_tasks, **kwargs):
        self.myvar = myvar
        self.downstream_tasks = downstream_tasks
        super().__init__(*args, **kwargs)

    def choose_branch(self, context):
        print(f'myvar is: {self.myvar}')
        return self.downstream_tasks if self.myvar else []


if __name__ == '__main__':
    dag = DAG(
        dag_id='parametrized_branch_operator',
        schedule_interval=None,
        start_date=days_ago(0),
        catchup=False
    )

    dummy = DummyOperator(
        task_id='dummy',
        dag=dag
    )

    branch = ParametrizedBranchOperator(
        task_id='branch',
        myvar=0,
        downstream_tasks=dummy.task_id,
        dag=dag
    )

    branch >> dummy
