import requests

url = "https://www.cnbc.com/world/?region=world"

headers = {
   "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
	with open("../data/raw_data/web_data.html","w", encoding="utf-8") as f: f.write(response.text)
	print("Web data saved successfully")
else:
	print("Failed to fetch data:", response.status_code)

