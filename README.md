# 🍔 Burger App: Wide-Column Database (Phase 3)

## 📌 Project Overview
This repository contains **Phase 3** of the Polyglot Data Ecosystem. In this phase, we utilize a **Wide-Column Database (DataStax Astra DB / Cassandra)** to handle massive, write-heavy workloads.

The primary use case implemented here is **User Activity Tracking** (e.g., logging every time a user views an item or adds it to the cart). Wide-Column databases are structurally designed to ingest millions of events per second while keeping data optimally sorted on disk for instantaneous time-series retrieval.

## 🧠 Data Modeling Strategy (Query-Driven Design)
In Cassandra-like systems, we model data strictly based on the queries we intend to run. Our goal is to fetch a user's most recent activity instantly without expensive `ORDER BY` operations.

* **Partition Key (`user_id`):** Ensures all events for a specific user are grouped and stored together on the same physical node for fast retrieval.
* **Clustering Key (`activity_time DESC`):** Automatically sorts the data on the disk as it is written. When we query the data, the newest actions naturally appear at the top.

## 🏗️ Project Structure
* `database.py`: Manages the connection to the Astra DB Data API.
* `crud.py`: Contains the core operations:
  * Table setup and schema definition.
  * Logging user activities (Insert).
  * Fetching time-ordered user history (Select).
* `main.py`: The entry point that orchestrates the simulation of user events.
* `.env`: Environment variables file (ignored in git) storing the `ASTRA_DB_TOKEN`.

## 🚀 Technologies Used
* **Database:** DataStax Astra DB (Wide-Column / Tables mode)
* **Language:** Python 3
* **Libraries:** `astrapy`, `python-dotenv`

## ⚙️ How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

   ASTRA_DB_TOKEN=your_token_here

   python main.py
