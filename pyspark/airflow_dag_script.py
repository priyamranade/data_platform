#!/usr/bin/env python3
"""
Simple PySpark test - Creates local sample data → Processes → Saves output
"""
from pyspark.sql import SparkSession
import tempfile

# Create Spark session
spark = SparkSession.builder \
    .appName("TransactionTest") \
    .master("local[*]") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

print("🚀 Starting PySpark test...")

# Create sample transaction data
data = [
    (1, "user1", 100.0, "2026-03-11"),
    (2, "user2", 250.0, "2026-03-11"),
    (3, "user1", 75.0, "2026-03-11"),
    (4, "user3", 300.0, "2026-03-12")
]

df = spark.createDataFrame(data, ["id", "user", "amount", "date"])
print("📊 Sample data created:", df.count())

# Process: Group by user, sum amounts
result = df.groupBy("user").agg({"amount": "sum"}).withColumnRenamed("sum(amount)", "total")
print("📈 Processing complete:", result.show())

# Save to local temp folder (Airflow logs this path)
output_dir = f"{tempfile.gettempdir()}/pyspark_output_{spark.sparkContext.applicationId}"
result.write.mode("overwrite").parquet(output_dir)
print(f"💾 Output saved: {output_dir}")

spark.stop()
print("✅ PySpark test COMPLETE!")
