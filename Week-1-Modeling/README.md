# Week 1: Data Modeling & System Architecture

## 🎯 The Objective
To design and deploy a scalable, analytical database schema for a ride-sharing application. This phase focuses on moving from raw requirements to a functional, containerized Data Warehouse environment.

---

## 🏗 The Architecture: Star Schema
I implemented a **Star Schema** to organize the data. This design is the industry standard for analytical workloads (OLAP) as it prioritizes query performance and simplicity for downstream BI tools.

### 1. The Fact Table (`fact_rides`)
*   **Purpose:** Captures the "Event" or "Verb" of a ride.
*   **Key Metrics:** Stores quantitative data like `ride_distance`, `total_amount`, and `duration`.
*   **Efficiency:** Uses Integer Foreign Keys to connect to dimensions, ensuring the fastest possible join speeds.

### 2. Dimension Tables (`dim_users`, `dim_locations`, `dim_drivers`)
*   **Purpose:** Provides the "Context" or "Noun" (The Who, Where, and When).
*   **Design Choice:** These tables are **Denormalized**. 
*   **Architectural Trade-off:** While a *Snowflake Schema* would save storage space by further normalizing dimensions, I opted for a *Star Schema* to reduce "Join Complexity." In modern Data Engineering, we prioritize reducing compute costs (CPU) over storage costs (Disk).

---

## 🐳 The Environment: Dockerized Postgres
To ensure this project is portable and professional, I bypassed traditional Virtual Machines (like CentOS/VirtualBox) in favor of **Docker Compose**.

### Why Docker?
*   **Reproducibility:** The entire system can be rebuilt on any machine with a single command.
*   **Environment-as-Code:** The infrastructure is defined in `docker-compose.yml`, ensuring the "It works on my machine" problem is eliminated.
*   **Automated Initialization:** I utilized **Docker Volumes** to map the SQL scripts in this folder to the container's entry point, allowing the database to self-assemble upon startup.

---

## 🛠 Tech Stack
*   **Database:** PostgreSQL 15 (Alpine Linux Build)
*   **Containerization:** Docker & Docker Compose
*   **Language:** SQL (Data Definition Language)
*   **IDE:** VS Code (integrated with Docker and SQLTools)

---

## 🚦 How to Initialize
To spin up the data warehouse and build the schema:

1. Ensure **Docker Desktop** is running.
2. Open your terminal in the root directory and run:
   ```bash
   docker-compose up -d