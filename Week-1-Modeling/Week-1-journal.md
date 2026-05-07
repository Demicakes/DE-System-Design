# Week 1 : Data Modeling & ETL Pipeline Engineering

## 🎯 Project Phase Goal
To build a scalable, local data environment using the **Medallion Architecture**, moving ride-sharing data from unstructured JSON files into a production-ready PostgreSQL Data Warehouse.



## 🏗️ The System Architecture
I implemented a three-tier pipeline to ensure data quality and auditability:

1.  **Bronze (Raw):** Immutable storage for incoming JSON ride events. I learned the "Golden Rule" of DE: Never modify the source data.
2.  **Silver (Cleaned):** I used Python and Pandas to flatten nested JSON structures and enforce data types (e.g., ensuring `fare_amount` is a float). This stage also adds a `processed_at` timestamp for data lineage.
3.  **Gold (Warehouse):** The final destination. Data is loaded into a PostgreSQL instance running in Docker, providing a structured environment for SQL-based analytics.

## 🛠️ Technical Challenges & Solutions

### 1. Networking & Port Collisions
* **Problem:** Connection to the database failed because Port `5432` was already occupied by a local Postgres service on my Windows machine.
* **Solution:** I implemented **Port Mapping** in `docker-compose.yml`, mapping the host port `5433` to the container port `5432`. This bypassed the conflict without requiring me to uninstall local software.

### 2. State Persistence (The "Ghost" Volume)
* **Problem:** Updating credentials in the `docker-compose.yml` did not work because Postgres had already initialized a data volume with the old password.
* **Solution:** I utilized `docker-compose down -v` and `docker volume prune` to clear the persistent state, forcing a fresh initialization with the correct security settings.

### 3. Repository Orchestration & Cleanup
* **Problem:** As the project grew, the root directory became cluttered with data files and scripts.
* **Solution:** * Reorganized logic into a `/Scripts` directory.
    * Created a `main.py` entry point to orchestrate the entire pipeline flow.
    * Configured `.gitignore` to prevent local data files from being committed to version control, following industry security best practices.

## 🚀 Key Skills Demonstrated
* **Containerization:** Managing multi-service environments with Docker.
* **Schema Enforcement:** Using Pandas to clean and validate data types before SQL ingestion.
* **Workflow Orchestration:** Automating a multi-step ETL process into a single executable pipeline.
* **Project Hygiene:** Organizing a repository for professional collaboration.

## ✅ Final Result
The system successfully ingests raw JSON, processes it into a clean CSV format, and loads it into a PostgreSQL table. The entire flow is now fully automated via `python main.py`.