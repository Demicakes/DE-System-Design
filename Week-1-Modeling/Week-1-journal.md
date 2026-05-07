# Engineering Journal: Week 1 - Data Modeling & System Design

## 💡 The "Self-Directed" Pivot: Moving Beyond Legacy Instruction
### Problem: Inefficient Curriculum (DE-Nat4 Bootcamp)
The Generation DE-Nat4 bootcamp curriculum was delivered using a legacy approach that relied heavily on **VirtualBox** and **CentOS** to teach Linux and environment management. 

**The Legacy Approach (Bootcamp):**
- Required manual installation of Virtual Machines (VirtualBox).
- Focused on local OS management (CentOS), which often led to "Tech Support" loops (BIOS settings, RAM allocation, OS updates).
- Resulted in an environment that was difficult to share, reproduce, or deploy to the cloud.

**The Professional Pivot (My Implementation):**
- I recognized that the bootcamp's delivery was out of sync with 2026 industry standards.
- I moved the entire project to **Docker and Docker Compose**.
- **The "Why":** In a modern Data Engineering role, we don't manage individual servers; we manage **containers**. Docker allows me to define the environment as *code*, making it 100% reproducible and ready for any Cloud provider (AWS/GCP/Azure) instantly.

---

## 🛠 Troubleshooting & Technical Milestones

### May 7, 2026: Docker Image Resolution
**Problem:** `Error response from daemon: failed to resolve reference "docker.io/library/postgres:15-alphine"`.
**Action:** Identified a spelling error in the image tag (`alphine` vs `alpine`).
**Lesson:** Precision is the price of admission in DevOps. Corrected the `docker-compose.yml` to use the lightweight Alpine Linux build, reducing the image size by ~90% compared to a standard build.

### Architectural Choice: Star Schema over Snowflake
**Decision:** Chose a **Star Schema** for the Ride-Share analytics model.
**Reasoning:** While the bootcamp touched on normalization, I chose a denormalized Star Schema to optimize for **Read Performance**. In modern analytics, we trade cheap storage (Disk) for faster compute (CPU), reducing join-complexity for downstream Data Analysts.

---

### 🏁 Week 1 Milestone Summary
- [x] Successfully bypassed legacy VM setup for a modern Containerized workflow.
- [x] Built a scalable Star Schema DDL.
- [x] Automated database initialization using Docker Volumes.
- [x] Verified table creation via `psql` command-line tools.