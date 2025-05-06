# def find_fib(n):
#   if n <= 2:
#     return 1
#   fib_x, fib_next = 1, 1
#   i = 3
#   while i <= n:
#     i += 1
#     fib_x, fib_next = fib_next, fib_x + fib_next
#   return fib_next

# for x in range(1, 11):
#   print(find_fib(x))


# def find_fib(n):
#   if n <= 2:
#     return 1
#   fib_x, fib_next = 1, 1
#   i = 3 
#   while i <= n:
#     i += 1
#     fib_x, fib_next = fib_next, fib_x + fib_next
#     return fib_next

# for x in range(1, 11):
#   print(find_fib(x))

# def find_fib(n):
#   list_fib = []
#   if n <= 2:
#     return 1
#   fib_x, fib_next = 1, 1
#   i = 3
#   while i <= n:
#     i += 1
#     fib_x, fib_next = fib_next, fib_x + fib_next
#   list_fib.append(fib_next)
#   return list_fib
# fib_nubmer = input("number fib")
# fib_nubmer = int(fib_nubmer)
# for x in range(1, fib_nubmer + 1):
#   print(find_fib(x))

def list_fib(n):
  fib_list = [1,1]
  if n <= 2:
    return fib_list[:n]
  fib_x, fib_next = 1, 1
  i = 3
  while i <= n:
    i += 1
    fib_x, fib_next = fib_next, fib_x + fib_next
    fib_list.append(fib_next)
  return fib_list
for x in range(1, 11):
  print(list_fib(x))