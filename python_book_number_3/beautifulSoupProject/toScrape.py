from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
category_div = soup.find('div', class_='side_categories')
links = category_div.find_all('a')
for link in links:
    name, url = link.string, link.get('href')
    name = name.strip()
    print(name, "|", url)
    