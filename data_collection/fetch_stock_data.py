import os
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker="AAPL", period="1y", interval="1d"):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    output_dir = os.path.join(base_dir, "data", "raw")
    os.makedirs(output_dir, exist_ok=True)

    data = yf.Ticker(ticker).history(period=period, interval=interval)
    data.reset_index(inplace=True)
    filename = os.path.join(output_dir, f"stock_{ticker}.csv")

    data.to_csv(filename, index=False)
    print(f"✅ Stock data for {ticker} saved to {filename}")

if __name__ == "__main__":
    for symbol in ["AAPL", "TSLA", "INFY", "^NSEI"]:
        fetch_stock_data(ticker=symbol)
