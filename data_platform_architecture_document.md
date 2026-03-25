# 📊 Data Platform Architecture Document

## 1. Overview

This project is a **containerized data platform** designed to:
- Orchestrate data workflows using Apache Airflow
- Process data using Python / PySpark tasks
- Centralize logs using Fluent Bit + Loki
- Visualize logs and metrics using Grafana
- Monitor system health using Prometheus

---

## 2. High-Level Architecture

The system is composed of the following layers:

### 2.1 Orchestration Layer
- Apache Airflow Scheduler → triggers workflows (DAGs)
- Airflow Workers → execute tasks
- Celery Executor → enables distributed task execution

### 2.2 Processing Layer
- Python / PySpark jobs
- Business logic execution
- Data transformations

### 2.3 Logging Layer
- Airflow generates logs per task
- Logs stored in shared volume
- Fluent Bit collects logs
- Loki stores and indexes logs
- Grafana visualizes logs

### 2.4 Monitoring Layer
- StatsD exporter collects Airflow metrics
- Prometheus stores metrics
- Grafana displays dashboards

### 2.5 Storage Layer
- PostgreSQL → Airflow metadata database
- Docker Volumes:
  - airflow-dags
  - airflow-logs
  - postgres-db

---

## 3. Design Patterns Used

### 3.1 Pipeline Pattern
- DAG-based workflow execution
- Sequential + parallel task orchestration

### 3.2 Observer Pattern (Logging)
- Fluent Bit observes log files
- Pushes updates to Loki in near real-time

### 3.3 Producer-Consumer Pattern
- Airflow Workers → Producers (generate logs)
- Fluent Bit → Consumer (reads logs)

### 3.4 Sidecar Pattern (Conceptual)
- Fluent Bit acts as a logging sidecar
- Decouples logging from application logic

### 3.5 Centralized Logging Pattern
- All logs aggregated in Loki
- Queryable via labels

### 3.6 Infrastructure as Code
- Entire system defined using Docker Compose

---

## 4. Data Flow

### Step-by-step Flow:

1. User triggers DAG (manual or scheduled)
2. Airflow Scheduler schedules tasks
3. Worker executes task
4. Task generates logs
5. Logs written to /opt/airflow/logs
6. Fluent Bit tails log files
7. Logs sent to Loki
8. Grafana queries Loki for visualization

---

## 5. Log Processing Flow

- Input: Tail plugin reads log files
- Parsing: Optional parsing via Fluent Bit
- Labeling: Adds metadata (job=airflow)
- Output: Sent to Loki via HTTP

---

## 6. Key Components

### Airflow
- DAG orchestration
- Task scheduling
- Retry and failure handling

### Redis
- Message broker for Celery

### PostgreSQL
- Stores metadata (task state, DAG runs)

### Fluent Bit
- Lightweight log collector
- Reads from file system

### Loki
- Log aggregation system
- Label-based indexing

### Grafana
- Visualization layer
- Dashboards for logs and metrics

### Prometheus
- Metrics storage

### StatsD Exporter
- Converts Airflow metrics to Prometheus format

### git-sync
- Syncs DAGs from GitHub

---

## 7. Scalability Considerations

- Celery Executor allows horizontal scaling
- Workers can be increased independently
- Logging pipeline is decoupled
- Loki handles high-volume logs efficiently

---

## 8. Fault Tolerance

- Airflow retries failed tasks
- Redis ensures message durability
- Logs persist in volumes
- Services restart automatically (Docker restart policies)

---

## 9. Deployment Strategy

- Single command deployment using Docker Compose
- Environment variables for configuration
- Volume-based persistence

---

## 10. Future Improvements

- Add alerting (Grafana alerts)
- Add log parsing for structured logs
- Introduce Kubernetes for scaling
- Add authentication for Grafana

---

## 11. Summary

This project demonstrates a **modern data platform architecture** combining:
- Workflow orchestration
- Distributed execution
- Centralized logging
- Metrics monitoring

It follows industry best practices and is suitable for real-world data engineering pipelines.


---

# 📌 Flow Diagram Document (GitHub Friendly)

> This section is formatted using Markdown-compatible diagrams so it renders cleanly on GitHub.

## 1. End-to-End System Flow

```text
User / Scheduler
        │
        ▼
Airflow Scheduler
        │
        ▼
Airflow Worker (Celery)
        │
        ▼
DAG Task Execution (Python / PySpark)
        │
        ▼
Log Generation (/opt/airflow/logs)
        │
        ▼
Fluent Bit (Log Collector)
        │
        ▼
Loki (Log Storage)
        │
        ▼
Grafana (Visualization)
```

---

## 2. Detailed Component Flow

```text
+----------------------+
|  GitHub Repository   |
+----------------------+
           │
           ▼
+----------------------+
|      git-sync        |
+----------------------+
           │
           ▼
+----------------------+
| airflow-dags volume  |
+----------------------+
           │
           ▼
+----------------------+
| Airflow Scheduler    |
+----------------------+
           │
           ▼
+----------------------+
| Airflow Worker       |
+----------------------+
           │
           ▼
+----------------------+
| Task Execution       |
+----------------------+
           │
           ▼
+----------------------+
| airflow-logs volume  |
+----------------------+
           │
           ▼
+----------------------+
| Fluent Bit           |
+----------------------+
           │
           ▼
+----------------------+
| Loki                 |
+----------------------+
           │
           ▼
+----------------------+
| Grafana              |
+----------------------+
```

---

## 3. Metrics Flow

```text
Airflow
   │
   ▼
StatsD Exporter
   │
   ▼
Prometheus
   │
   ▼
Grafana
```

---

## 4. Docker-Level Flow

```text
+---------------------------------------------------+
|               Docker Compose Network              |
|---------------------------------------------------|
|                                                   |
|  Airflow → Redis → Worker Execution               |
|      │                                            |
|      ▼                                            |
|  Logs Volume → Fluent Bit → Loki → Grafana        |
|                                                   |
|  Metrics → StatsD → Prometheus → Grafana          |
|                                                   |
+---------------------------------------------------+
```

---

## 5. Key Flow Explanations

- DAG Flow → Controls execution of tasks
- Log Flow → Captures and centralizes logs
- Metrics Flow → Tracks system performance
- Sync Flow → Keeps DAGs updated from GitHub

---



This system follows a clear pipeline:
- Airflow orchestrates tasks
- Tasks generate logs
- Logs are collected by Fluent Bit
- Logs are stored in Loki
- Grafana provides visualization

Additionally:
- Prometheus handles metrics
- git-sync ensures DAG updates
