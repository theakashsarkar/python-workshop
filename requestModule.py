# import requests
# url = "https://englishtherapy.com.bd/about-us/"
# response = requests.get(url)
# print(response.reason)

# fp = open("test.txt", "w")
# fp.write("this file was create using python")
# print(type(fp))
# fp.close()

# # with open("test.txt", "w") as f:
# #   f.write("Hello, Python\n")
# # print(f)
# with open("test.txt", "a") as f:
#   f.write("Hello bangladesh")

import requests
import os
import webbrowser as wb
import sys
# url = "https://englishtherapy.com.bd/about-us/"
# response = requests.get(url)
# with open("dimik.html", "w") as f:
#   f.write(response.text,)
# file_path = os.path.realpath("dimik.html")
# wb.open("file://" + file_path)
# print(file_path)
# img_url = "https://letsenhance.io/static/73136da51c245e80edc6ccfe44888a99/1015f/MainBefore.jpg"
# response = requests.get(img_url)
# with open("image.png", "wb") as f:
#   f.write(response.content)

# img_url = sys.argv[1]
# response = requests.get(img_url)
# file_name = sys.argv[2]
# with open("image.png","wb") as f:
#   f.write(response.content)

# lines = ["This is first line", "This is second line", "This is third line"]
# with open("test.txt", "w") as fp:
#   for line in lines:
#     fp.write(line+"\n")

# with open("test.txt", 'r') as fp:
#   content = fp.read()
#   print(content)

# with open("test.txt", "r") as fp:
#   lines = fp.readline()
#   print(lines)
#   for line in lines:
#     print('line')

# with open("test.txt", "r") as fp:
#   for line in fp:
#     print(line)

# with open("test.txt", "r") as fp:
#   print(fp.read())


# countrys = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo", "Congo",  "Egypt","Libya", "Morocco", "Nigeria", "Rwanda","Príncipe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan"]
# def checkCharacter(fileName, countryName):
#   with open(fileName,"a") as fp:
#     fp.write(countryName+"\n")
# for country in countrys:
#   if country[0] == "A":
#     checkCharacter('a.txt', country)
#   if country[0] == "B":
#     checkCharacter('b.txt',country)

# def div(a, b):
#   try:
#     return a/b
#   except ZeroDivisionError:
#     print("Can not divide by zero")
# print(div(10, 2))
# print(div(3, 0))
# print(div(9, 3))

import io

fileName = "ab.txt"
mode = "r"
try:
  with open(fileName, mode) as fp:
    content = fp.read()
    print(content)
except FileNotFoundError:
  print(fileName, "Not found. pleas check if the file's name is correct")
except io.UnsupportedOperation:
  print("Are you sure", fileName, "is readable?")