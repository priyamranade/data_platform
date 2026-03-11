from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonVirtualenvOperator  # ← MOVED TO TOP

dag = DAG(
    'priyam_transactions_pipeline',
    start_date=datetime(2026, 3, 1),
    schedule=None,
    catchup=False,
    tags=['pyspark', 'test']
)

def pyspark_test():
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName("PriyamTransactionsTest") \
        .master("local[*]") \
        .getOrCreate()
    
    df = spark.range(1000).toDF("id")
    df.show(5)
    print("✅ PySpark WORKS! Priyam's transaction pipeline LIVE!")
    
    spark.stop()

run_pyspark_test = PythonVirtualenvOperator(
    task_id='run_pyspark_test',
    python_callable=pyspark_test,
    requirements=['pyspark==3.5.0'],
    dag=dag
)
