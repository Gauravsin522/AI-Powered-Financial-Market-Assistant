# /data_collection/fetch_all_data.py

import time
import subprocess

scripts = [
    "fetch_stock_data.py",
    "fetch_crypto_data.py",
    "fetch_forex_data.py",
    "fetch_news_data.py"
]

print("\n🚀 Starting unified data fetch pipeline...\n")

for script in scripts:
    print(f"📥 Running {script}...")
    try:
        subprocess.run(
            ["python", f"./data_collection/{script}"],
            check=True
        )
        print(f"✅ {script} executed successfully.\n")
        time.sleep(1)  # Optional: be polite to APIs
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script}: {e}\n")

print("🎉 All data fetch scripts completed.\n")
