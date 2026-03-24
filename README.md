# 🚀 Production Data Platform

**Complete Data Engineering Platform by Priyam Rana**

## 🎯 What This Project Does
Modern **data platform** with **orchestration**, **processing**, **monitoring**, and **visualization**:

# 🚀 Production Data Platform

**Tested Stack: Docker 29.2.1 + Git 2.53.0.windows.2 + Airflow 2.11.0**

## 📋 Prerequisites (Exact Versions - Tested)

| Tool | Version | Download |
|------|---------|----------|
| **Docker Desktop** | **29.2.1** | [Docker Desktop](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe) |
| **Git** | **2.53.0.windows.2** | [Git for Windows](https://git-scm.com/download/win) |
| **RAM** | **8GB+** | 11+ services running |

### **Windows Install (5 minutes)**
```powershell
# 1. Docker Desktop 29.2.1 → Restart PC
# 2. Git 2.53.0.windows.2 → Next → Next → Finish
# 3. Verify: docker --version && git --version

### 🏗️ COMPLETE SERVICES (11 Containers)

| Service | Role | URL | Tech |
|---------|------|-----|------|
| **Airflow** | Orchestration | localhost:8080 | Scheduler + Worker |
| **Django** | Dashboard | localhost:8000 | Terminal UI |
| **Grafana** | Visualization | localhost:3000 | Dashboards |
| **Prometheus** | Metrics | localhost:9090 | Time-series |
| **Loki** | Logs | localhost:3100 | Centralized |
| **Fluentbit** | Log Forwarding | Internal | Logs → Loki |
| **StatsD Exporter** | App Metrics | Internal | StatsD → Prometheus |
| **Postgres** | Metadata | Internal | Airflow DB |
| **Redis** | Queue | Internal | Celery |
| **Git-sync** | DAGs | Internal | Auto-updates |
| **PySpark** | Processing | Worker | Data Lake |


## 🚀 Quick Start (2 minutes)
```powershell
git clone https://github.com/priyamranade/data_platform
cd data_platform
copy .env.example .env
docker compose up -d
