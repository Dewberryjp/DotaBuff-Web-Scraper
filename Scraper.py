import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://www.dotabuff.com/players/128957251/matches'
response = req.get(url)
print(response.text)