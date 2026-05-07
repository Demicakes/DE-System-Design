import json
import random
from datetime import datetime, timedelta
import os

# Ensure the bronze directory exists
os.makedirs('data/bronze', exist_ok=True)

def generate_ride():
    ride_id = random.randint(1000, 9999)
    # Raw data often has nested structures and inconsistent types
    return {
        "event_id": f"evt_{random.getrandbits(32)}",
        "ride_details": {
            "id": ride_id,
            "user": f"User_{random.randint(1, 50)}",
            "driver_info": {"name": f"Driver_{random.randint(1, 20)}", "rating": random.uniform(3.5, 5.0)},
            "distance_miles": str(round(random.uniform(1.0, 25.0), 2)), # Sent as string to simulate messy API
        },
        "locations": {
            "pickup": random.choice(["Downtown", "Airport", "Suburb", "Train Station"]),
            "dropoff": random.choice(["Downtown", "Airport", "Suburb", "Train Station"])
        },
        "timestamp": (datetime.now() - timedelta(minutes=random.randint(1, 1000))).isoformat(),
        "fare": round(random.uniform(5.0, 100.0), 2)
    }

# Generate 5 raw "Bronze" files
for i in range(5):
    data = generate_ride()
    filename = f"data/bronze/ride_{data['ride_details']['id']}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Generated Bronze Data: {filename}")