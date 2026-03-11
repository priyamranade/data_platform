from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'priyam_transactions_pipeline',
    start_date=datetime(2026, 3, 1),
    schedule=None,
    catchup=False,
    tags=['pyspark', 'test']
)

run_pyspark_test = BashOperator(
    task_id='run_pyspark_test',
    bash_command='python /opt/airflow/dags/airflow_dag_script.py',
    dag=dag,
    env={
        'PYSPARK_PYTHON': 'python3',
        'SPARK_LOCAL_DIRS': '/tmp/spark'
    }
)
