import os
import requests
import pandas as pd
import time

def fetch_crypto_data(coin_id="bitcoin", days=90, currency="usd"):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    output_dir = os.path.join(base_dir, "data", "raw")
    os.makedirs(output_dir, exist_ok=True)

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": currency, "days": days}
    response = requests.get(url, params=params).json()

    df = pd.DataFrame(response["prices"], columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    filename = os.path.join(output_dir, f"crypto_{coin_id}.csv")
    df.to_csv(filename, index=False)

    print(f"✅ Crypto data for {coin_id} saved to {filename}")

if __name__ == "__main__":
    for coin in ["bitcoin", "ethereum"]:
        fetch_crypto_data(coin_id=coin)
        time.sleep(1.2)  # ✅ Respect API rate limits
