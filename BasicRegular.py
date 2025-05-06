import re
# pattern = "hello"
# text = "hello world"
# result = re.search(pattern, text)
# print(result)

# text = "The price is $19.99"
# pattern = "price."
# pattern1 = "99$"
# print(re.search(pattern1, text))

# text = "The yearn is 2023"
# pattern = r"[0-9]"
# print(re.findall(pattern,text))

# pattern2 = r"[a-zA-Z]"
# print(re.findall(pattern2, text))
# text = "hello hellooo world"
# pattern = r"hello+?"
# pattern1 = r"o{2,3}"
# print(re.findall(pattern1, text))
text = "Email: user@example.com"
pattern = r"(\w+)@(\w+)\.(\w+)"
match = re.search(pattern, text)
print(match.span())
if match:
  print(match.group())
  print(match.group(0))