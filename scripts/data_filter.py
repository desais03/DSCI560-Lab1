from bs4 import BeautifulSoup
import csv

print("Reading HTML file...")

with open("../data/raw_data/web_data.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

print("Filtering news data...")

# Extract news articles
articles = soup.find_all("a")

news_data = []

for article in articles:
    title = article.get_text(strip=True)
    link = article.get("href")

# Keep only valid entries
    if title and link and "http" in link:
        news_data.append([title, link])

# Save news CSV
with open("../data/processed_data/news_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])
    writer.writerows(news_data[:20])

print("News CSV created!")

# Dummy market data (since CNBC structure is complex)
print("Storing market data...")

market_data = [
    ["DOW", "Up", "+0.5%"],
    ["NASDAQ", "Down", "-0.3%"]
]

with open("../data/processed_data/market_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Symbol", "Position", "Change"])
    writer.writerows(market_data)

print("Market CSV created!")


