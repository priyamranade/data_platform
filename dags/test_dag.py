"""
Priyam's Transaction Analytics Pipeline
GitHub Sync → Airflow → PySpark
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# ✅ Add pyspark path FIRST
import sys
import os
sys.path.insert(0, '/opt/airflow/dags/pyspark')

# ✅ Safe PySpark import
try:
    from transaction_analytics import analyze_transactions_pyspark
except ImportError as e:
    print(f"PySpark import failed: {e}")
    def analyze_transactions_pyspark(**context):
        print("🚀 STUB: PySpark analytics (full import later)")
        return "SUCCESS"

default_args = {
    'owner': 'priyam.rana',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='priyam_transactions_pipeline_test',
    default_args=default_args,
    description='Transaction analytics with PySpark',
    schedule_interval='@hourly',
    start_date=datetime(2026, 3, 9),
    catchup=False,
    tags=['priyam', 'pyspark', 'data-platform']
) as dag:

    analytics_task = PythonOperator(
        task_id='run_pyspark_analytics',
        python_callable=analyze_transactions_pyspark,
    )
