from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'priyam_transactions_pipeline',  # ← Matches UI expectation
    start_date=datetime(2026, 3, 1),
    schedule=None,
    catchup=False,
    tags=['pyspark', 'transactions']
)

# EXACT PATH to your spark script (same folder)
run_pyspark_processing = BashOperator(
    task_id='run_pyspark_test',  # ← Matches your error
    bash_command='python /opt/airflow/dags/airflow_dag_script.py',  # ← CORRECT PATH
    dag=dag
)
