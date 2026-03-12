from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pyspark.sql import SparkSession

def pyspark_test():
    spark = SparkSession.builder \
        .appName("DataPlatformTest") \
        .config("spark.jars", "/opt/spark/jars/*") \
        .master("local[*]") \
        .getOrCreate()
    
    df = spark.range(1000).toDF("id")
    print(f"✅ PySpark working! Rows: {df.count()}")
    spark.stop()

dag = DAG(
    'test_pyspark',
    start_date=datetime(2026, 3, 12),
    schedule_interval=None,
    catchup=False
)

task = PythonOperator(
    task_id='pyspark_test',
    python_callable=pyspark_test,
    dag=dag
)
