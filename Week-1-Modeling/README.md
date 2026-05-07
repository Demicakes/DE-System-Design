# Week 1: Data Modeling (Star Schema)

## The Goal
To design a scalable database structure for a ride-sharing app.

## Why a Star Schema?
- **Speed:** By using `INT` IDs in the Fact table, queries run faster.
- **Maintenance:** We can update a city name in one place (`dim_locations`) without touching millions of ride records.
- **Accuracy:** The `REFERENCES` constraint prevents us from entering fake data.

### Star vs. Snowflake: Why Star?
In this project, I implemented a **Star Schema**. 

- **Star Schema:** Denormalized dimensions. Fewer joins = Faster queries.
- **Snowflake Schema:** Normalized dimensions. More joins = Lower storage, but higher compute cost.

**Decision:** At a scale of millions of rides, the cost of "Compute" (running the query) outweighs the cost of "Storage." Therefore, the Star Schema is the preferred modern architecture for this analytical use case.