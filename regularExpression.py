import re
import os

# s = "Afganistan, America, Banlgadesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"
# countries = s.split(",")
# print(countries)
# li = [item for item in countries if item.endswith("land")]
# print(li)

# li = [item for item in countries if item.endswith("land") or item.endswith("lands")]
# print(li)

# li = re.fchindall(r'(\w+lands+)', s)
# print(li)

# match = re.search('Bangla', 'Bangladesh')
# print(match.group)

s = "Bangladesh"
# match = re.search('dets', 'Bangladesh')
# print(match.group())

# match = re.search('.',s)
# print(match.group())

# match = re.search('B.+h', s)
# match = re.search('B.+?h', s)
# text = "Phone number: 01828527818"
# match = re.search('\d+', text)
text = "house number: 5, phone number: 01828527818, 01811111111, 0192222222, 01322222222, 00000000000000 123-123"
# match = re.search('\d{3}\s*\d{8}', text)
# match = re.findall('\d{3}\s*\d{8}',text)
# match = re.findall(r'01[356789]\s*\d{8}',text)
# print(match)

# fileName = "a.txt"
# mode = 'r'
# content = ''
# try: 
#   with open(fileName, mode) as fp:
#     content = fp.read()
# except FileNotFoundError:
#   print("File Not Found")

# print(re.findall(r'Country$',content, re.IGNORECASE))
# print(re.findall(r'Country$$', content, re.I))
# print(content)
# print(re.findall(r'^.*?$', content, re.MULTILINE))

# string = "<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominu</li>"
# pattern = r'<li>(.*?)</li>'
# result = re.findall(pattern, s)
# print(result)

# capt = re.compile(pattern)
# result = capt.findall(string)
# print(result)

# text = "This is line 1. Date is 2017/06/01. And there is another date: 2017-07-01. The third and final date is 2017/08/30."
# pat = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
# print(pat)
# result = pat.findall(text)
# print(result)
# print(dir(pat))

# string = "Abcd 1234 - 33"
# result = re.sub(r'\d', '0', string)
# print(result)

# string = "22/07/2017, 20/01/2017, 01/01/2018"
# # newString = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', string)
# newString = re.sub(r'(\d{2})/(\d{2})/(\d{4})', '\g<3>-\g<2>-\g<1>', string)
# print(newString)

fileName = "player.html"
mode = "r"
content = ''
try:
  with open(fileName, mode) as fp:
    content = fp.read()
except FileNotFoundError:
  print("File Not Found")

# pattern = r'<li>\s*(.*?)\s*<ol>\s*(.*?)</ol>\s*</li>'
pattern = r'<li>\s*(.*?)\s*<ol>(.*?)<li>(.*?)</li></ol>\s*</li>'
# player_pattern = r'<li>(.*?)</li>'

# result = re.findall(pattern, content, re.DOTALL)
# for country, player in result:
#   country = country.strip()
#   players = re.findall(player_pattern, player, re.DOTALL)
#   players = [play.strip() for play in players]
#   # print(country + ' ' + '- ' + ',' . join(players) )

# print(result)


# text = "Email your feedback here: book@subeen.com book@subeen thank you book_py.book@subeen.com"
# result = re.findall(r'(\w+@\w+.\w+)', text)
# print(result)
# result = re.findall(r'[.\w]+@\w+[.]\w+', text)
# print(result)


text = "book at subeen.com, book At subeen.com, book (at) subeen dot com, book [at] subeen [dot] com"
# text = re.sub(r'\s+[\(\[]*\s*at\s[\)\]*\s+', '@', text, flags=re.I)
# print(text)
text = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+','@', text,flags=re.I)
result = re.sub(r'\[at\]', '@', text, flags=re.I)
result = re.sub(r'dot', '.', result, flags=re.I)
result = re.sub(r'\s*\[dot\]\s*','.', result, flags=re.I)
# print(result)

dir_name = "rokmari_com"
# os.mkdir(dir_name)

# def create_dir(name):
#   try: 
#     os.mkdir(name)
#   except FileExistsError:
#     print(name, "already exists")
# create_dir(dir_name)



