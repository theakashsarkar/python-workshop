import re
import requests
import logging
import sys
from typing import Pattern, Tuple, List, Optional
category_pat = re.compile(r'(catalogue/category/books/.*?)\">\s*(\w+[\s\w]+\w)\s*?</a>', re.MULTILINE | re.DOTALL)
next_page_pat = re.compile(r'<li class="next">\s*<a href="(.*?)">next</a></li>', re.MULTILINE | re.DOTALL)
book_list_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')
img_pat = re.compile(r'<div\s*class=\"[^\"]+\">\s*<img\s*src=\"([^\"]+)\"')
desc_url = re.compile(r'<p>([^<]+)</p>')
upc_pat = re.compile(r'<td>(UPC)</td>\s*<td>(.*?)</td>')
price_pat = re.compile(r'<th>Price \(incl. tax\)</th><td>\D+([\d.]+?)</td>')
availability_pat = re.compile(r'<th>Availability</th>\s*<td>(.*?)</td>')

def get_page_content(url: str) -> Optional[str]:
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logging.error(e)
        return None
    if response.ok:
        return response.text
    logging.error(f'Cannot get content from url: {url}')
    return None

def extract_pattern_value(content: str, pattern: Pattern, field_name: str) -> str:
    """Helper function to extract pattern matches with error handling."""
    result = pattern.findall(content)
    if len(result) == 0:
        logging.warning(f"{field_name} not found!")
        return ""
    return result[0]
def get_product_details(content: str):
    image_base = "https://books.toscrape.com/"
    """
        Extract product details from the content.
        Return a dictionary containing the product details.
    """
    img_url = extract_pattern_value(content, img_pat, "Image URL")
    image_url = image_base + img_url.replace("../../", "") if img_url else ""

    product_details = {
        "image_url": image_url,
        "description": extract_pattern_value(content, desc_url, "Description"),
        "upc": extract_pattern_value(content, upc_pat, "UPC"),
        "price": extract_pattern_value(content, price_pat, "Price"),
        "availability": extract_pattern_value(content, availability_pat, "Availability"),
    }
    return product_details


content = get_page_content("https://books.toscrape.com/catalogue/sharp-objects_997/index.html")
print(get_product_details(content))