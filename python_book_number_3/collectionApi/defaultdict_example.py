from collections import defaultdict

dt1 = defaultdict(int)
s1 = "hello"
for c in s1:
  dt1[c] += 1
print(dt1)