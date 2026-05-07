# 🚕 Ride-Share Data Engineering System

An end-to-end data pipeline demonstrating the **Medallion Architecture**. This system ingests raw JSON ride data, transforms it for quality, and loads it into a Dockerized PostgreSQL Data Warehouse.

## 🏗 System Architecture
The project follows the Three-Layer Medallion pattern:
1.  **Bronze (Raw):** Immutable storage of incoming JSON ride events.
2.  **Silver (Cleaned):** Flattened tabular data with enforced types and audit timestamps.
3.  **Gold (Warehouse):** Analysis-ready SQL tables in a PostgreSQL container.

## 🛠 Tech Stack
- **Engine:** Python 3.12 (Pandas, SQLAlchemy)
- **Infrastructure:** Docker & Docker Compose
- **Database:** PostgreSQL 15

## 🚀 Quick Start
1. **Prepare Environment:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt