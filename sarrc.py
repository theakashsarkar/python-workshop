# sarrc = ["Bangladesh", "Afghanistan", "India", "Bhutan", "Nepal", "Pakistan", "SriLanka"]

# country = input("Enter the name of the country: ")
# if country in sarrc :
#   print(country, "is a memeber of sarrc")
# else : 
#   print(country, "is not a memeber of sarrc")  
# print("program terminated")


# marks = input("Please enter you marks ")
# marks = int(marks)

# if marks >= 85:
#   grade = "A+"
# elif marks >= 70:
#   grade = "A"
# elif marks >= 60:
#   grade = "A-"
# elif marks >= 50:
#   grade = "B"
# else:
#   grade = "F"
# print("your grade is", grade)

# number = input("Please your number ")
# number = int(number)
# if number % 2 == 0:
#   print("Number is prime: ", number)
# else:
#   print("Number is odd: ", number)

# year = input("Leap Year ")
# year = int(year)
# if year % 4 != 0:
#   print("No")
# else: 
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Yes")
#     else:
#       print("No")
#   else:
#     print("Yes")

# if year % 100 != 0 and year % 4 == 0:
#   print("Leap Year", year)
# elif year % 100 == 0 and year % 400 == 0:
#   print("Leap Year", year)
# else:
#   print(year,"is not leap year")

# result = 0
# for num in range(1, 100):
#   if num % 5 == 0:
#     result += num
#     print(num)
# print("sum is:", result)    

# result = 0
# for num in range(5, 101, 5):
#   if num % 5 == 0:
#     result += num
#     print(num)
# print("sum is:", result)

# li = list(range(11))
# print(li)

# li = list(range(2, 21, 2))
# print(li)

# i = 0
# while i < 5:
#   print(i)
#   i += 1

# i = 5
# while i >= 0:
#   i -= 1
#   print(i)

# number = input("please enter a positive integer: ")
# n = int(number)

# m = 1
# while m <= 10:
#   print(n, "x", m, "=", n*m)
#   m += 1

# while True:
#   n = input("Please enter a number (0 to exit): ")
#   n = int(n)
#   if n == 0:
#     break
#   print("Square of", n, "is", n*n)

# while True:
#   n = input("Please enter a positive number (0 to exit)")
#   n = int(n)
#   if n < 0:
#     print("We only allow positve nubmer. please try again.")
#     continue
#   if n == 0:
#     break
#   print("Square of", n, "is", n*n)

# terminate_program = False
# while not terminate_program:
#   num1 = input("Please enter a number")
#   num1 = int(num1)
#   num2 = input("Please enter a another number")
#   num2 = int(num2)

#   while True:
#     operation = input("Please enter add/sub or quit to exits: ")
#     if operation == "quit":
#       terminate_program = True
#       break
#     if operation not in ["add", "sub"]:
#       print("Unknown operation")
#       continue
#     if operation == "add":
#       print("Result is", num1 + num2)
#       break
#     if operation == "sub":
#       print("Result is", num1 - num2)
#       break


# import turtle;

# def draw_square(side_length):
#   for i in range(4):
#     turtle.forward(side_length)
#     turtle.left(90)

# def myfnc(x, y = 10, z=0):
#   print("X =", x, "y =", y, "z =", z)
# x = 5
# y = 6
# z = 7
# myfnc(x, y, z)  

# def add_number(numbers):
#   result = 0
#   for number in numbers:
#     result += number
#   return result
# result = add_number([1,2,3,4,5])
# print(result)

# def test_func(li):
#   li[0] = 10
# my_list = [1, 2, 3, 4]
# print("before function call", my_list)
# test_func(my_list)
# print("after function call", my_list)

# def average(listNum):
#   result = sum(listNum)
#   averag = result / len(listNum)
#   print(averag)
# average([1,2,3,4,5,6])

# def multiplication_table(number = 1):
#   for i in range(1, 11):
#     print(number, "x", i, "=", number * i)

# multiplication_table()

# country = "North Korea"
# new_country = country.replace("North", "South")
# print(new_country.find("u"))
# print(new_country)

# name = "Mr. Akash"
# if name.startswith("Mr."):
#   print("Dear Sir")

# str = "A quick brown fox jumps over the lazy dog 123"
# for c in "abcdefghjklmnopqrstuvwxyz":
#   print(c, str.count(c))
# str.isdigit()
# print(str.isdigit())
# digit = ""
# capital = ""
# for c in "123":
#   digit += c
# for c in "abcdefghjklmnopqrstuvwxyz":
#   capital += c  
# print(capital)
# upperCase = ''  
# lowerCase = ''
# digits    = ''
# special   = ''
# def checkString(char):
#   global upperCase, lowerCase, digits, special
#   if char.isupper(): 
#     upperCase += char
#   elif char.islower():
#     lowerCase += char   
#   elif char.isdigit():
#     digits += char
#   else:
#     special += char  

# def spilt_string(string):
#   for char in string:
#     checkString(char)
# inputString = spilt_string(input("Enter the string"))
# print("uppercase ", upperCase)
# print("lowerCase ", lowerCase)
# print("digits", digits)
# print("special", special)

# def swapString(string):
#   word = ''
#   i = 0
#   while i < len(string) - 1:
#     # print(string[i+1] + string[i])
#     word += string[i+1] + string[i]
#     i += 2
#   if len(string) % 2 != 0:
#     word += string[-1]
#   print(word) 
# swapString("Bangladesh") 
# is_palindrome = True
# def palindrome(string):
#   i, j = 0, len(string) - 1
#   while i < j:
#     if string[i] != string[j]:
#       is_palindrome = False
#       break
#     i += 1
#     j -= 1
# string = input("check palindrome")
# palindrome(string)    
# if is_palindrome:
#   print("yes")
# else:
#   print("No")      

# li = ["mango", "banana", "orange"]
# li.insert(0, "apple")
# li.pop()
# item = "apples"
# if item in li:
#   li.remove(item)
# else:
  # print(item, "not in list")
# print(li)

# li = [1,2,3,4]
# li2 = [5,6,7,8]
# li.extend(li2)
# print(li)
# del(li)
# print(li)
# li = []
# for x in range(10):
#   li.append(x)
# print(li)  
# li = [1,2,3]
# li1 = li*3
# print(li1)

# li = ["a", "b", "c"]
# str = "".join(li)
# print(str)

# li = [1,2,3,4]
# new_li = []
# for x in li:
#   new_li.append(2*x)
#  print(new_li)
# new_li = [2 * x for x in li]
# print(new_li)
# new_li = [2 ** x for x in li]
# print(new_li)

# number = (10, 20, 30, 40 ,50 ,60 )
# n1, n2, n3, n4, n5, n6 = number
# print(n1)

# t = n3, n4
# print(t)

# li = [1,2,3,4]
# tpl = (1,2,3)
# A = set(li)
# print(A)

# B = set(tpl)
# print(B)

# a = {1,2,3}
# b = {2, 4, 3}
# c = a & b
# c = a | b
# c = a ^ b
# c = a - b
# print(c)

# dictionary
# marks = [77, 76 ]
import random
# print(random.random())
# print("*******")
# print(random.randint(1,3))


# def compareNumber():
#   global low, high, number
#   input_number = (low + high) // 2 
#   print("My guess is", input_number)
#   attempts += 1
#   if input_number == number:
#     print("Yes, your guess is correct")
#     return True
#   if input_number > number:
#     print("Incorrect! Please try to guest a smaller number.")
#     high = input_number - 1
#   else:
#     print("Incorrect! Please try to guess a larger number.")
#     low = input_number + 1
#   return False

# number = random.randint(1, 1000)
# attempts = 0
# low = 1
# high = 1000
# while True:
#   print("Guess the number (between 1 and 1000): ")
#   if compareNumber():
#     break
# # print("You tried", attempts, "times to find the correct number.")    

# def is_prime1(num):
#   if num < 2:
#     return False
#   prime = True
#   for x in range(2, num):
#     if num % x == 0:
#       print(num, "is divisible by", x)
#       prime = False
#   return prime    

# while True:
#   number = input("Please enter a number (enter 0 to exit): ")
#   number = int(number)
#   if number == 0:
#     break
#   prime = is_prime1(number)
#   if prime is True:
#     print(number, "is a prime number.")
#   else:
#     print(number, "is not a prime number")

# def is_prime2(n):
#   if n < 2:
#     return False
#   if n == 2:
#     return True
#   if n % 2 == 0:
#     print(n, "is divisible by 2")
#     return False
#   prime = True
#   for x in range(3, n):
#     if x % n == 0:
#       print(n,"is divisible by", x)
#       prime = False
#       return prime
#   return prime

# while True:
#   number = input("Please enter a number (enter 0 to exit): ")
#   number = int(number)
#   if number == 0:
#     break
#   prime = is_prime2(number)
#   if prime is True:
#     print(number, "is a prime number.")
#   else:
#     print(number, "is not a prime number")
