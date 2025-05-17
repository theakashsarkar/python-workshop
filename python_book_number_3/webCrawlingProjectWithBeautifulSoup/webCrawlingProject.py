# import requests
# from bs4 import BeautifulSoup

# def find_products_info(html_doc):
#   soup = BeautifulSoup(html_doc, 'html.parser')
#   # product_main = soup.find('div', class_='product_main')
#   # name = product_main.h1.string
#   product_desc = soup.find('div', id='product_description')
#   desc = product_desc.find_next('p').string
  
#   article = soup.find('article', class_='product_page')
#   table = article.find('table')
#   upc = table.tr
#   upc = upc.td.string
#   product_type = upc.find_next('tr')
#   product_type = product_type.td.string
#   price = product_type.find_next('tr').find_next('tr')
#   price = price.td.string

#   product_gallery = soup.find('div', id='product_gallery', class_='carousel')
#   item_active = product_gallery.find('div', class_='item active')
#   image_base = "http://books.toscrape.com/"
#   product_image = image_base + item_active.img.get('src').replace("../../", "")

#   print(name)
#   print(desc)
#   print(upc)
#   print(product_type)
#   print(price)
#   print(product_image)

# if __name__ == '__main__':
#   url_list = [
#     'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
#   ]
#   for url in url_list:
#     r = requests.get(url)
#     html_doc = r.text
#     find_products_info(html_doc)
#     print()

import requests
from bs4 import BeautifulSoup

def find_products_info(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    products = soup.find_all('article', class_='product_pod')
    
    for product in products:
      try:
          title = product.h3.a.get('title', 'No title available')
          price_elem = product.find('p', class_='price_color')
          price = price_elem.string if price_elem else 'Price not available'

          avail_elem = product.find('p', class_='instock availability')  # Updated class name
          availability = avail_elem.string if avail_elem else 'Availability unknown'
            
          product_url = product.find('h3').a.get('href', '')
          if product_url and not product_url.startswith('http'):
            product_url = 'https://books.toscrape.com/catalogue/' + product_url.replace('../', '')
            
          print(f"Title: {title}")
          print(f"Price: {price}")
          print(f"Availability: {availability}")
          print(f"Product URL: {product_url}")
          print("-" * 50)
      except AttributeError as e:
        print(f"Error processing product: {e}")
        continue
def get_page_content(url):
    r = requests.get(url)
    return r.text
def extract_product_links(content):
    soup = BeautifulSoup(content, 'html.parser')
    li = soup.find_all("article", class_="product_pod")
    links = [
      'http://books.toscrape.com/catalogue/' + item.find('h3').find('a').get('href') for item in li
    ]
    return links
def get_all_product_links(url):
    all_product_urls = []
    for page in range(1, 51):
      url = "http://books.toscrape.com/catalogue/page-{}.html".format(page)
      print("Crawling", url)
      content = get_page_content(url)
      links = extract_product_links(content)
      all_product_urls.extend(links)
    return all_product_urls
if __name__ == '__main__':
    url_list = [
        'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    ]
    for url in url_list:
        r = requests.get(url)
        html_doc = r.text
        find_products_info(html_doc)
        print()