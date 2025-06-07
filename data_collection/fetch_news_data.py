import os
import requests
import json
import yaml
from datetime import datetime

# Define base and output paths
base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, "data")
raw_dir = os.path.join(data_dir, "raw")
os.makedirs(raw_dir, exist_ok=True)

# Load API Key
with open(os.path.join(data_dir, "api_keys.yaml")) as f:
    keys = yaml.safe_load(f)
API_KEY = keys["NEWSAPI"]

def fetch_financial_news(query="finance", page_size=100):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params).json()
    articles = response.get("articles", [])

    if not articles:
        print(f"❌ No articles found or API error: {response.get('message', response)}")
        return

    filename = os.path.join(
        raw_dir, f"financial_news_{datetime.today().strftime('%Y%m%d')}.json"
    )
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

    print(f"✅ News data saved to {filename}")

if __name__ == "__main__":
    fetch_financial_news()
