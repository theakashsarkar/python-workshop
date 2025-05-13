# def find_index(li, n):
#   if n <= li[0]:
#     return 0
#   if n > li[-1]:
#     return len(li)
#   for i in range(len(li)):
#     if li[i] < n and li[i+1] >= n:
#       return i + 1
#   raise("Couldn't find the right place for n")
# def insort(li, n):
#   i = find_index(li, n)
#   li.append(n)
#   for j in range(len(li)-1, i, -1):
#     li[j] = li[j-1]
#   li[i] = n
#   print(li)
# insort([1, 3, 5, 7], 4)

def find_index(li, n):
  if n <= li[0]:
    return 0
  if n > li[-1]:
    return len(li)
  for i in range(len(li)):
    if li[i] < n and li[i+1] >= n:
      return i + 1
  print("Couldn't find the right place for n")
def insort(li, n):
  i = find_index(li, n)
  li.append(n)
  for j in range(len(li)-1, i, -1):
    li[j] = li[j-1]
  li[i] = n
  return li

if __name__ == "__main__":
  for n in range(11):
    li = [1,2,2,3,4,6,7,8,9]
    print(li, n)
    insort(li, n)
    print()