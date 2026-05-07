-- ==========================================
-- 1. DIMENSION TABLES (The "Context")
-- ==========================================

-- WHERE: Stores city and neighborhood details
CREATE TABLE dim_locations (
    location_id INT PRIMARY KEY,    -- Unique ID for the area
    city_name VARCHAR(100),         -- e.g., 'London'
    neighborhood VARCHAR(100),      -- e.g., 'Soho'
    timezone VARCHAR(50)            -- e.g., 'GMT'
);

-- WHO: Stores user and driver details
CREATE TABLE dim_users (
    user_id INT PRIMARY KEY,        -- Unique ID for the person
    user_type VARCHAR(20),          -- 'rider' or 'driver'
    rating DECIMAL(3,2)             -- e.g., 4.95
);

-- ==========================================
-- 2. FACT TABLE (The "Action")
-- ==========================================

-- THE EVENT: The actual ride transaction
CREATE TABLE fact_rides (
    ride_id SERIAL PRIMARY KEY,     -- Auto-incrementing ID for the ride
    
    -- Foreign Keys (Pointers to the Dimensions)
    rider_id INT REFERENCES dim_users(user_id),
    driver_id INT REFERENCES dim_users(user_id),
    location_id INT REFERENCES dim_locations(location_id),
    
    -- Quantitative Metrics (The "Facts")
    fare_amount DECIMAL(10,2),      -- How much was paid
    distance_miles DECIMAL(10,2),   -- How far they went
    ride_timestamp TIMESTAMP        -- When it happened
);