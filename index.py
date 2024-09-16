import requests
from bs4 import BeautifulSoup

url = "https://www.readhub.cn/daily"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
req = requests.get(url, headers=headers)
bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find("head").prettify())
print(bs.find("div", class_="style_card__8X4rP style_daily__tt3_7 border-1px").prettify())
with open("index.html", "w", encoding="utf-8") as d:
    d.write(bs.find("head").prettify()+bs.find("div", class_="style_card__8X4rP style_daily__tt3_7 border-1px").prettify())
