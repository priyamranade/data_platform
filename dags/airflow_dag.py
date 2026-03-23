from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pyspark

def analyze_transactions():
    """Transaction analytics for Priyam's data platform"""
    transactions = [
        {"id": 1, "amount": 100.50, "status": "success"},
        {"id": 2, "amount": 250.00, "status": "failed"},
        {"id": 3, "amount": 75.25, "status": "success"},
        {"id": 4, "amount": 1800.00, "status": "success"},
        {"id": 5, "amount": 45.99, "status": "pending"},
        {"id": 6, "amount": 320.75, "status": "success"},
        {"id": 7, "amount": 99.99, "status": "failed"}
    ]
    
    success_txns = [t for t in transactions if t["status"] == "success"]
    total_success = sum(t["amount"] for t in success_txns)
    
    print(f"🎉 Processed {len(transactions)} transactions")
    print(f"✅ {len(success_txns)} successful = ${total_success:.2f}")
    print(f"📊 Success rate: {len(success_txns)/len(transactions)*100:.1f}%")
    return "SUCCESS"

# Airflow 3.1.7 SYNTAX (schedule NOT schedule_interval)
with DAG(
    dag_id="priyam_transactions_airflow3",
    start_date=datetime(2026, 3, 6),
    schedule="*/30 * * * *",  # FIXED: Airflow 3.x syntax
    catchup=False,
    tags=["priyam", "data-engineer", "transactions"]
) as dag:

    analytics_task = PythonOperator(
        task_id="analyze_transactions",
        python_callable=analyze_transactions
    )
