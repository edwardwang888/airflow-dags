# airflow-dags
This repository contains DAGs used to test Airflow functionality.

## Notes
* Don't use `if __name__ == '__main__'`. Airflow does not seem to pick up
the DAG if you do.
