import os
import requests
import pandas as pd
import yaml

# Get base project path
base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, "data")
raw_dir = os.path.join(data_dir, "raw")
os.makedirs(raw_dir, exist_ok=True)

# Load API key
with open(os.path.join(data_dir, "api_keys.yaml")) as f:
    keys = yaml.safe_load(f)
API_KEY = keys["ALPHA_VANTAGE"]

def fetch_forex_data(pair="USD/INR"):
    from_currency, to_currency = pair.split("/")

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_currency,
        "to_symbol": to_currency,
        "apikey": API_KEY,
        "outputsize": "compact"
    }

    response = requests.get(url, params=params).json()

    if "Time Series FX (Daily)" not in response:
        print(f"❌ Error fetching forex data for {pair}: {response.get('Note') or response}")
        return

    data = pd.DataFrame(response["Time Series FX (Daily)"]).T
    data.columns = ["open", "high", "low", "close"]
    data.index = pd.to_datetime(data.index)
    data = data.sort_index()

    filename = os.path.join(raw_dir, f"forex_{from_currency}_{to_currency}.csv")
    data.to_csv(filename)
    print(f"✅ Forex data for {pair} saved to {filename}")

if __name__ == "__main__":
    for pair in ["USD/INR", "EUR/USD"]:
        fetch_forex_data(pair=pair)
