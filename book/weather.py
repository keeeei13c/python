import requests


url =("http://weather.livedoor.com/forecast/webservice/jsom/vi?city = 110010")

data = requests.get(url).json()
print(data)



