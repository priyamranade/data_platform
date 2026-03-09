def analyze_transactions_pyspark(**context):
    """PySpark transaction analytics for Priyam's data platform"""
    
    # Mock transaction data (replace with S3/Kafka in production)
    transactions = [
        {"id": 1, "amount": 100.50, "status": "success"},
        {"id": 2, "amount": 250.00, "status": "failed"},
        {"id": 3, "amount": 75.25, "status": "success"},
        {"id": 4, "amount": 1800.00, "status": "success"},
        {"id": 5, "amount": 45.99, "status": "pending"},
        {"id": 6, "amount": 320.75, "status": "success"},
        {"id": 7, "amount": 99.99, "status": "failed"}
    ]
    
    # Convert to Spark DataFrame (production: read from S3)
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder \
        .appName("PriyamTransactionAnalytics") \
        .master("local[*]") \
        .getOrCreate()
    
    # Create DataFrame
    df = spark.createDataFrame(transactions)
    
    # PySpark transformations (bronze → silver)
    success_txns = df.filter(df.status == "success")
    total_success = success_txns.agg({"amount": "sum"}).collect()[0][0]
    
    # Business metrics
    total_records = df.count()
    success_count = success_txns.count()
    success_rate = (success_count / total_records) * 100
    
    # Log results (visible in Airflow UI)
    print(f"🎉 Processed {total_records} transactions")
    print(f"✅ {success_count} successful = ${total_success:.2f}")
    print(f"📊 Success rate: {success_rate:.1f}%")
    
    # Write results (production: S3 bronze layer)
    success_txns.write.mode("overwrite").parquet("/tmp/bronze/success_transactions")
    
    spark.stop()
    return f"SUCCESS: {success_count} txns processed"
