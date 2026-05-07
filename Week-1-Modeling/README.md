# Week 1: Data Modeling (Star Schema)

## The Goal
To design a scalable database structure for a ride-sharing app.

## Why a Star Schema?
- **Speed:** By using `INT` IDs in the Fact table, queries run faster.
- **Maintenance:** We can update a city name in one place (`dim_locations`) without touching millions of ride records.
- **Accuracy:** The `REFERENCES` constraint prevents us from entering fake data.