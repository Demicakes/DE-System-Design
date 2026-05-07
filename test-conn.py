import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="ride_share_warehouse",
        user="engineer",
        password="password123",
        port="5433"
    )
    print("✅ RAW CONNECTION SUCCESSFUL!")
    conn.close()
except Exception as e:
    print(f"❌ RAW CONNECTION FAILED: {e}")