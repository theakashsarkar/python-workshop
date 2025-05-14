def is_anagram(s1: str, s2: str) -> bool:
  # s1 = "".join(sorted(s1))
  # s2 = "".join(sorted(s2))
  # return True if s1 == s2 else False
  dt1 = dict()
  for c in s1:
    if c in dt1:
      dt1[c] += 1
    else:
      dt1[c] = 1
  for c in s2:
    if c not in dt1:
      return False
    else:
      dt1[c] -= 1
  for v in dt1.values():
    if v != 0:
      return False
  return True
print(is_anagram("listen", "silent"))
print(is_anagram("listen", "silents"))