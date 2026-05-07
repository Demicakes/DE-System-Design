import subprocess
import sys

def run_step(name, path):
    print(f"🚀 Running {name}...")
    result = subprocess.run([sys.executable, path])
    if result.returncode != 0:
        print(f"❌ {name} failed. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    # The order matters!
    run_step("Data Generation", "Scripts/generate_raw_data.py")
    run_step("Bronze to Silver", "Scripts/bronze_to_silver.py")
    run_step("Silver to Gold", "Scripts/silver_to_gold.py")
    
    print("\n✨ Pipeline Complete! Data is ready in Postgres.")