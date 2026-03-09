"""
Priyam's PySpark Transaction Analytics
"""
def analyze_transactions_pyspark(**context):
    """Main analytics function - runs in Airflow worker"""
    print("🚀 Starting Priyam's PySpark Transaction Analytics...")
    
    try:
        # ✅ Initialize Spark (works in Docker)
        from pyspark.sql import SparkSession
        
        spark = SparkSession.builder \
            .appName("PriyamTransactionAnalytics") \
            .master("local[*]") \
            .config("spark.sql.adaptive.enabled", "true") \
            .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
            .getOrCreate()
        
        print("✅ PySpark session created successfully!")
        
        # ✅ Your analytics logic here
        df = spark.range(1000).toDF("transaction_id")
        result = df.groupBy("transaction_id % 10").count()
        print(f"✅ Analytics complete: {result.count()} partitions")
        
        spark.stop()
        return "SUCCESS"
        
    except Exception as e:
        print(f"❌ PySpark error: {str(e)}")
        return f"FAILED: {str(e)}"
