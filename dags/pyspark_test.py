from pyspark.sql import SparkSession

def pyspark_task():
    spark = SparkSession.builder \
        .appName("TestPySpark") \
        .config("spark.jars", "/opt/spark/jars/*") \
        .getOrCreate()
    
    df = spark.range(1000).toDF("number")
    print(f"Row count: {df.count()}")
    spark.stop()
