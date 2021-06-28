import requests
from bs4 import BeautifulSoup

xml = requests.get("https://news.yahoo.co.jp/rss/topics/it.xml")
soup = BeautifulSoup(xml.text,'html.parser')
for news in soup.findAll('item'):
    print(news.title.string)
