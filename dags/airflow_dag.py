from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

# ✅ CORRECT PATH for your git-sync structure
# From /opt/airflow/dags/dags/ → ../pyspark/
sys.path.append('/opt/airflow/dags/dags/pyspark')

from transaction_analytics import analyze_transactions_pyspark

with DAG(
    dag_id="priyam_transactions_airflow3",
    start_date=datetime(2026, 3, 6),
    schedule="*/30 * * * *",
    catchup=False,
    tags=["priyam", "data-engineer", "transactions", "pyspark"]
) as dag:

    spark_task = PythonOperator(
        task_id="run_pyspark_analytics",
        python_callable=analyze_transactions_pyspark
    )
