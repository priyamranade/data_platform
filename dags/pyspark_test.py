from airflow.decorators import dag, task
from datetime import datetime
from pyspark.sql import SparkSession

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["pyspark", "test"]
)
def pyspark_example_dag():

    @task()
    def pyspark_task():
        # Initialize SparkSession inside the task to avoid top-level overhead
        spark = SparkSession.builder \
            .appName("TestPySpark") \
            .config("spark.jars", "/opt/spark/jars/*") \
            .getOrCreate()
        
        try:
            df = spark.range(1000).toDF("number")
            count = df.count()
            print(f"Row count: {count}")
        finally:
            spark.stop() # Ensure session is closed even if task fails

    pyspark_task()

# Instantiate the DAG
pyspark_example_dag()
