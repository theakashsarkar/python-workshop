import re
# import requests
# import sys

# url = "https://www.rokomari.com"
# response = requests.get(url)
# if response.ok is False:
#   sys.exit("Could not get response from server")
# page_content = response.text
# # regexp = re.compile(r'<div class="lookInside_imageContainer__A2WcA"><img alt="এক নজরে কুরআন" loading="lazy" width="240" height="320" decoding="async" data-nimg="1" class="lookInside_bookImage__a4vPG" src="(.*?)" style="color: transparent;"></div>', re.S)
# # <div class="lookInside_imageContainer__A2WcA"><img alt="এক নজরে কুরআন" loading="lazy" width="240" height="320" decoding="async" data-nimg="1" class="lookInside_bookImage__a4vPG" src="https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/Eak_Nozore_quran-Dr_Mizanur_Rahman_Azhari-2d298-449989.png" style="color: transparent;"></div>
# # <div class="lookInside_imageContainer__A2WcA"><img alt=" পাইথন দিয়ে প্রোগ্রামিং শেখা" loading="lazy" width="240" height="320" decoding="async" data-nimg="1" class="lookInside_bookImage__a4vPG" src="https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/dfb303496d64_143309.jpg" style="color: transparent;"></div>
# # regexp = re.compile(r'<div class="lookInside_imageContainer__A2WcA">\s*<img alt="(.*?)" loading="lazy" width="240" height="320" decoding="async" data-nimg="1" class="lookInside_bookImage__a4vPG" src="(.*?)" style="color: transparent;"></div>', re.S)
# # result = re.findall(regexp, page_content)

# class Test: 
#   def __init__(self, __id):
#     self.__id = 101
# test = Test(102)
# print(test._Test__id)
# import re
# import sys
# import requests # type: ignore

# url = "https://www.rokomari.com/book/category/2427/math-olympiad"

# try:
#     response = requests.get(url)
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {e}")
#     sys.exit()

# if not response.ok:
#     print('Invalid URL or failed to retrieve the page.')
#     sys.exit()

# html = response.text

# # pattern = re.compile(r'<div\s*class="books-wrapper__item"\s*title="(.*?)"', re.S)
# # pattern = re.compile(r'<div\s+class=\"book-list-wrapper\">\s*<a[^>]*?href=\"([^\"]*)\"[^>]*?title=\"([^\"]*)\".*?<img\s+src=\"([^\"]*)\"',re.S)

# matches = pattern.findall(html)

# if matches:
#     print("Titles found:")
#     for title in matches:
#         print("-", title)
# else:
#     print("No titles found.")
# pattern = re.compile(r'<div\s+class="book-list-wrapper">\s+<a\s+href="(.*?)"\s*title="(.*?)"',re.S)
# import re
# import sys
# import requests
# base_url = "https://www.rokomari.com"
# url = base_url + "/book/author/4207/tamim-shahriar-subeen"

# def responseText(url: str) -> str:
#     try:
#         response = requests.get(url)
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")
#         sys.exit()
#     if response.ok is False:
#         sys.exit("Could not get response from server")
#     return response.text
# html = responseText(url)
# # print(html)
# pattern = re.compile(r'<div\s+class=\"book-list-wrapper\">\s*<a[^>]*?href=\"([^\"]*)\"[^>]*?title=\"([^\"]*)\".*?<img\s+src=\"([^\"]*)\"',re.S)
# matches = pattern.findall(html)
# if matches:
#     for url, title, img_url in matches:
#         print(f"URL: {url}")
#         print(f"Image: {img_url}")
#         print(f"Title: {title}")
# else :
#     print("No matches found.")
import re
import sys
import requests

base_url = "https://www.rokomari.com"
url = base_url + "/book/author/4207/tamim-shahriar-subeen"

def responseText(url: str) -> str:
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit()
    if not response.ok:
        sys.exit("Could not get response from server")
    return response.text

html = responseText(url)

pattern = re.compile(
    r'<a[^>]*?href="(/book/[^"]+)"[^>]*?title="([^"]+)"[^>]*?>\s*<div[^>]*?>\s*<img[^>]*?src="([^"]+)"',
    re.S
)

matches = pattern.findall(html)

if matches:
    for book_url, title, img_url in matches:
        print(f"URL: {base_url + book_url}")
        print(f"Image: {img_url}")
        print(f"Title: {title}\n")
else:
    print("No matches found.")

# def fib_serice(n: int, memo = {}):
#     if n in memo:
#         return memo[n] 
#     if n <= 1:
#         return n
#     memo[n] = fib_serice(n-1) + fib_serice(n-2)
#     return memo[n]
# print(fib_serice(10))