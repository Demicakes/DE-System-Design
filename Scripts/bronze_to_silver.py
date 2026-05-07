import json
import os
import pandas as pd
from datetime import datetime

# 1. Setup paths
BRONZE_PATH = 'data/bronze'
SILVER_PATH = 'data/silver'
os.makedirs(SILVER_PATH, exist_ok=True)

def transform_bronze_to_silver():
    all_rides = []

    # 2. Extract: Loop through every JSON file in Bronze
    for filename in os.listdir(BRONZE_PATH):
        if filename.endswith('.json'):
            with open(os.path.join(BRONZE_PATH, filename), 'r') as f:
                raw_data = json.load(f)
                
                # 3. Transform: Flattening and Cleaning
                # We pull specific values out of the nested JSON
                clean_record = {
                    "ride_id": raw_data['ride_details']['id'],
                    "user_name": raw_data['ride_details']['user'],
                    "driver_name": raw_data['ride_details']['driver_info']['name'],
                    "driver_rating": raw_data['ride_details']['driver_info']['rating'],
                    "distance_miles": float(raw_data['ride_details']['distance_miles']), # Casting String to Float
                    "pickup_location": raw_data['locations']['pickup'],
                    "dropoff_location": raw_data['locations']['dropoff'],
                    "ride_timestamp": raw_data['timestamp'],
                    "fare_amount": raw_data['fare'],
                    "processed_at": datetime.now().isoformat() # Adding an Audit Column
                }
                all_rides.append(clean_record)

    # 4. Load: Convert list of dictionaries to a Table (DataFrame) and save as CSV
    if all_rides:
        df = pd.DataFrame(all_rides)
        output_file = os.path.join(SILVER_PATH, 'cleaned_rides.csv')
        df.to_csv(output_file, index=False)
        print(f"✅ Success! Silver Layer created at: {output_file}")
        print(df.head()) # Preview the clean table
    else:
        print("❌ No Bronze files found to process.")

if __name__ == "__main__":
    transform_bronze_to_silver()