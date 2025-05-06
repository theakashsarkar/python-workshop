import requests
import re

# url = "https://books.toscrape.com/"
# url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
text = response.text
# result = re.findall(r'<div\s+class=\"([^\"]+)\">(.*?)</div>', text, re.MULTILINE | re.DOTALL)
# result = re.findall(r'<li>\s*<a[^>]*?href=\"(catalogue/category/books/[^\"]+)\">', text,  re.MULTILINE | re.DOTALL)
# text = text.replace('\n', '')
# book_pat = re.compile(r'<h3><a href=\"([^\"]+)\" title=\"([^\"]+)\"')
# next_page = re.compile(r'<li class=\"(next)\"<a href=\"([^\"]+)\">next</a></li>')
# next_page = re.compile(r'<li class=\"next\"><a href=\"(.*?)\">next</a></li>')
# next_page = next_page.findall(text)
# findSlash = url.rfind("/")
# next_url = url[0:findSlash+1] + "page-2.html"
# print(url[0:findSlash+1])
# print(next_url)
# book_pat = re.compile(r'<h3><a href=\"([^\"]+)\" title=\"([^\"]+)\">([^\"]+)</a></h3>
# result = book_pat.findall(text)
# for item in result:
#   print(item)
# print(result)

# product_description = re.compile(r'<div id=\"product_description\" class=\"sub-header\">\s*<h2>(.*)</h2>\s*</div>\s*<p>(.*)</p>')
text = """
<table class="table table-striped">
        
        <tbody><tr>
            <th>UPC</th><td>a897fe39b1053632</td>
        </tr>
        
        <tr>
            <th>Product Type</th><td>Books</td>
        </tr>
            <tr>
                <th>Price (excl. tax)</th><td>£51.77</td>
            </tr>
            
                <tr>
                    <th>Price (incl. tax)</th><td>£51.77</td>
                </tr>
                <tr>
                    <th>Tax</th><td>£0.00</td>
                </tr>
            
            <tr>
                <th>Availability</th>
                <td>In stock (22 available)</td>
            </tr>    
            <tr>
                <th>Number of reviews</th>
                <td>0</td>
            </tr>
        
    </tbody></table>"""
product_description = re.compile(r'<th>(.*?)</th><td>(.*?)</td>')
result = product_description.findall(text)
for item in result:
  print(item)

import csv

field_name = ["Name", "Author", "Publisher", "Price", "Category"]
book1 = ["Computer Programming part 1", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "240.00", "Programming"]
book2 = ["Computer Programming part 2", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "250.00", "Programming"]
book3 = ["Computer Programming part 3", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "200.00", "Programming"]

book_list = [book1, book2, book3]
with open("books.csv","w") as csvf:
    csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_name)
    for book1 in book_list:
        csv_writer.writerow(book1)