# airflow-dags
This repository contains DAGs used to test Airflow functionality.

## Notes
* Don't use `if __name__ == '__main__'`. Airflow does not seem to pick up
the DAG if you do.

## Local Development
For setup on Mac:
* Add mysql_config path
* Add LD_LIBRARY_PATH
* Install nvm
* Install npm
* Install webpack
* yarn build
* Configuration options are specified in $AIRFLOW_HOME (automatically created). If any configuration options are problematic, look there to find the proper configuration setting.
