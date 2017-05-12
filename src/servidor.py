import requests
from bs4 import BeautifulSoup
url = 'http://gugas02.pythonanywhere.com'
payload= {'expression' : '8*4'}

r = requests.post(url,data=payload)

html_data = r.text
soup= BeautifulSoup.BeautifulSoup(html_data)
index= soup.find(attrs={'name':'expression'}).get('value')

print(index)