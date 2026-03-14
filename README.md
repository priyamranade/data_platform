# 🚀 Production Data Platform

**Complete Data Engineering Platform by Priyam Rana**

## 🎯 What This Project Does
Modern **data platform** with **orchestration**, **processing**, **monitoring**, and **visualization**:

## 🏗️ Architecture (9 Services)

| Service | Role | URL | Tech |
|---------|------|-----|------|
| **Airflow** | Orchestration | localhost:8080 | Scheduler + Worker |
| **Django** | Dashboard | localhost:8000 | Terminal UI |
| **Grafana** | Visualization | localhost:3000 | Dashboards |
| **Prometheus** | Metrics | localhost:9090 | Time-series |
| **Loki** | Logs | localhost:3100 | Centralized |
| **Postgres** | Metadata | Internal | Airflow DB |
| **Redis** | Queue | Internal | Celery |
| **Git-sync** | DAGs | Internal | Auto-updates |
| **PySpark** | Processing | Worker | Data Lake | -- can be configured if the spark build is installed using docker airflow services.

## 🚀 Quick Start (2 minutes)
```powershell
git clone https://github.com/priyamranade/data_platform
cd data_platform
copy .env.example .env
docker compose up -d
