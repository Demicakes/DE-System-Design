# Week 1 & 2: Data Modeling & ETL Foundations

## 🎯 Project Phase Goal
Build a localized data lake and warehouse environment to move ride-sharing data through a full lifecycle: from raw JSON events to a structured PostgreSQL database.

## 🏗️ Architecture: The Medallion Pattern
I implemented the Medallion Architecture to ensure data quality at every step:

1.  **Bronze (Raw Layer):** Immutable storage. I generated raw JSON files simulating ride events. The rule here: *never touch the raw files.*
2.  **Silver (Cleaned Layer):** Data Transformation. I used Pandas to:
    * Flatten nested JSON structures.
    * Enforce data types (converting strings to floats for `distance` and `fare`).
    * Add audit columns (`processed_at`) for traceability.
3.  **Gold (Curated Layer):** The Data Warehouse. Structured SQL tables in PostgreSQL, optimized for business logic and reporting.


---

## 🛠️ Technical Hurdles & Solutions

### 1. The "Ghost" in the Volume (Docker Persistence)
* **Problem:** I updated my database password in `docker-compose.yml`, but my Python script kept getting a `FATAL: password authentication failed` error.
* **The "Aha!" Moment:** I learned that Postgres initializes its credentials only once in a Docker Volume. Changing the YAML doesn't update an existing volume.
* **Solution:** Used `docker-compose down -v` to wipe the volume and force a fresh initialization with the new credentials.

### 2. The Port 5432 Collision
* **Problem:** Even with the correct password, the connection was rejected.
* **Diagnosis:** Ran `netstat -ano | findstr :5432` and discovered a local instance of Postgres (likely from a previous install) was "camping" on the port.
* **Solution:** Implemented **Port Mapping**. I mapped the host port `5433` to the container port `5432`, creating a private lane for this project.

### 3. Data Integrity & Schema Enforcement
* **Problem:** SQL databases are "Strongly Typed," meaning you can't put a string into a float column.
* **Solution:** I used Pandas `.astype(float)` during the Silver transition. This ensures that the data is "Gold-ready" before it even hits the database door.

---

## 🚀 Key Commands Used
| Goal | Command |
| :--- | :--- |
| **Reset Environment** | `docker-compose down -v` |
| **Check Port Usage** | `netstat -ano \| findstr :5432` |
| **Verify SQL Data** | `docker exec -it de_journal_db psql -U engineer -d ride_share_warehouse -p 5432` |

## ✅ Result
The pipeline successfully processes JSON files and loads them into a relational table. I can now run complex SQL queries on data that started as unstructured text.