# import re
# import csv
# import requests
# import logging
# import sys

# def get_category_list(content):
#     return category_pat.findall(content)

# def get_page_content(url):
#     try:
#         response = requests.get(url)
#     except requests.exceptions.RequestException as e:
#         logging.error(e)
#     if response.ok:
#         return response.text
#     logging.error('con not get content form url:" + url')
#     return None

# def crawl_website():
#     url = "https://books.toscrape.com/index.html"
#     host_name = "books.toscrape.com"
#     content = get_page_content(url)
#     if content == "":
#         logging.critical("Got empty content from url: " + url)
#         sys.exit(1)
#     category_list = get_category_list(content)
#     for category in category_list:
#         category_url, category_name = category 
#         category_url = "http://" + host_name + "/" + category_url
#         print(category_url)
#         sys.exit(1)
#         crawl_category(category_name, category_url)

# if __name__ == "__main__":
#     # category_pat = re.compile(r'<li>\s*<a[^>]*?href=\"(catalogue/category/books/[^\"]+)\">',  re.MULTILINE | re.DOTALL)
#     # category_pat = re.compile(r'<li><a href=\"(catalogue/category/books/.*?)\">\s*(\w+[\s\w]+\w)\s*?<)',re.MULTILINE | re.DOTALL)
#     category_pat = re.compile(r'<li><a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*<',re.MULTILINE | re.DOTALL)
#     logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename="bookstore_crawler.log", level=logging.DEBUG, filemode="w")
#     with open("book_list.csv", "w") as csvf:
#         csv_writer = csv.DictWriter(csvf, fieldnames=["Name", "Category", "UPC", "URL", "ImageURL", "Price", "Availability", "Description"])
#         csv_writer.writeheader()
#         crawl_website()

import re
import csv
import sys
import requests
import logging

def get_category_list(content):
    # print(content)
    # category_pat = re.compile(r'<li><a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*<', re.MULTILINE | re.DOTALL)
    # result = re.findall(r'<li>\s*<a[^>]*?href=\"(catalogue/category/books/[^\"]+)\">', content,re.MULTILINE | re.DOTALL)
    # result = re.findall(r'<li><a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*<', re.MULTILINE | re.DOTALL)
    result = re.findall(r'<li>\s*<a href=\"(catalogue/category/books_1/.*?)\">\s*(\w+[\s\w]+\w)\s*?</a>', content, re.MULTILINE | re.DOTALL)
    print(result)
    return result

    # return category_pat.findall(content)

def get_page_content(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logging.error(e)
        return None
    if response.ok:
        return response.text
    logging.error(f'Cannot get content from url: {url}')
    return None

def crawl_category(category_name, category_url):
    logging.info(f'Crawling category: {category_name} from {category_url}')
    # Add your category crawling logic here
    # pass

def crawl_website():
    url = "https://books.toscrape.com/index.html"
    host_name = "books.toscrape.com"
    content = get_page_content(url)
    # print(content)
    if content is None:
        logging.critical(f"Got empty content from url: {url}")
        sys.exit(1)
    category_list = get_category_list(content)
    # print(category_list)
    for category in category_list:
        print(category)
        # category_url, category_name = category 
        # print(category)
        # category_url = "https://" + host_name + "/" + category_url
        # crawl_category(category_name, category_url)

if __name__ == "__main__":
    category_pat = re.compile(r'<li><a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*<', re.MULTILINE | re.DOTALL)
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        filename="bookstore_crawler.log",
        level=logging.DEBUG,
        filemode="w"
    )
    with open("book_list.csv", "w", newline='') as csvf:
        csv_writer = csv.DictWriter(csvf, fieldnames=["Name", "Category", "UPC", "URL", "ImageURL", "Price", "Availability", "Description"])
        csv_writer.writeheader()
        crawl_website()