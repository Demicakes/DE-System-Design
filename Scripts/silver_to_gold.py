import pandas as pd
from sqlalchemy import create_engine
import os

# 1. Connection Details (Matching your docker-compose.yml)
# Format: postgresql://[user]:[password]@[host]:[port]/[database]
DB_URL = "postgresql://engineer:password123@localhost:5433/ride_share_warehouse"
engine = create_engine(DB_URL)

def load_silver_to_gold():
    # 2. Extract from Silver
    silver_file = 'data/silver/cleaned_rides.csv'
    
    if not os.path.exists(silver_file):
        print("❌ Silver file not found. Run bronze_to_silver.py first.")
        return

    df = pd.read_csv(silver_file)

    # 3. Load into Gold (Postgres)
    # We load into a staging table first or directly into our fact table
    try:
        print("🚀 Uploading data to Postgres...")
        df.to_sql('fact_rides', engine, if_exists='append', index=False)
        print(f"✅ Successfully loaded {len(df)} rows into Gold Layer (fact_rides)!")
    except Exception as e:
        print(f"❌ Error loading to Postgres: {e}")

if __name__ == "__main__":
    load_silver_to_gold()