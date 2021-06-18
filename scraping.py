import requests
from bs4 import BeautifulSoup    # importする


load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")    # HTMLを解析する

# print(soup.find("title").text)
# print(soup.find("h2").text)

# print(soup.find_all("li"))

for element in soup.find_all('li'):
    print(element.text)

