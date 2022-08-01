from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'start_date': days_ago(2)
}

templated_command = """ cd {{ params.directory }}
                    python3 {{ params.sub_directory }}{{ params.filename }} {{ execution_date }}
"""

with DAG('pipeline',
         default_args=default_args,
         schedule_interval='@daily') as pipeline:

    task_1 = BashOperator(task_id='task_1',
                          bash_command=templated_command,
                          params={'filename': 'data_download.py',
                                  'sub_directory': 'step1/',
                                  'directory': '$AIRFLOW_HOME/dags/'})

    task_2 = BashOperator(task_id='task_2',
                          bash_command=templated_command,
                          params={'filename': 'database_upload.py',
                                  'sub_directory': 'step2/',
                                  'directory': '$AIRFLOW_HOME/dags/'})

    task_3 = BashOperator(task_id='task_3',
                          bash_command=templated_command,
                          params={'filename': 'query_database.py',
                                  'sub_directory': 'step2/',
                                  'directory': '$AIRFLOW_HOME/dags/'})


# Set the operator dependencies
task_1 >> task_2 >> task_3
