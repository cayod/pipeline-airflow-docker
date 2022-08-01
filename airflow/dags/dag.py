from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

today = DT.date.today()
one_day_ago = today - DT.timedelta(days=1)

default_args = {
    'start_date': one_day_ago,
}

templated_command = """
  python3 {{ params.directory }}/{{ params.filename }}
"""


with DAG('pipeline',
         default_args=default_args,
         schedule_interval='@daily') as pipeline:

    task_1 = BashOperator(task_id='download_data',
                          bash_command=templated_command,
                          params={'filename': 'data_download.py',
                                  'directory': '$AIRFLOW_HOME/airflow/step1'})

    task_2 = BashOperator(task_id='upload_data',
                          bash_command=templated_command,
                          params={'filename': 'database_upload.py',
                                  'directory': '$AIRFLOW_HOME/airflow/step2})

    task_3 = BashOperator(task_id='query_databse',
                          bash_command=templated_command,
                          params={'filename': 'query_database.py',
                                  'directory': '$AIRFLOW_HOME/airflow/step2})


# Set the operator dependencies
task_1 >> task_2 >> task_3