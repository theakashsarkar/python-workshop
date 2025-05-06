import re
import sys
import requests
import os
from typing import List, Tuple


baseUrl = "https://www.rokomari.com"
authorPath = "/book/author/4207/tamim-shahriar-subeen"
pattern = re.compile(r'<a[^>]*?href=\"(/book/[^\"]+)[^>]*?title=\"([^\"]+)\"[^>]*?>\s*<div[^>]*?>\s*<img[^>]*?src=\"([^\"]+)')

def create_directory(directoryPath: str) -> None:
  if not os.path.exists(directoryPath):
    os.makedirs(directoryPath)
    print(f"Directory '{directoryPath}' created successfully.")
  else:
    print(f"Directory '{directoryPath}' already exists.")

def download_image(imgUrl: str, fileName: str) -> None:
  with open(fileName, 'wb') as f:
    response = requests.get(imgUrl)
    f.write(response.content)

def getPageContent(url: str) -> str:
  try: 
    response = requests.get(url)
  except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit()
  if response.ok is False:
    print("Could not get response from server")
    sys.exit()
  return response.text

def extractBookInfo(html: str) -> List[Tuple[str, str, str]]:
  return pattern.findall(html)

def getAuthorBooks(baseUrl: str, authorPath: str) -> None:
  fullPath = f"{baseUrl}{authorPath}"
  html = getPageContent(fullPath)
  books = extractBookInfo(html)

  if books:
    for url, title, img_url in books:
      print(f"URL: {url}")
      print(f"Image: {img_url}")
      print(f"Title: {title}\n")
  else:
    print("No matches found.")
getAuthorBooks(baseUrl, authorPath)