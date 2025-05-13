from bisect import bisect_left, bisect_right, bisect
# li = [1, 2, 3, 3, 4, 5, 6, 7, 8]
# print(bisect_left(li, 2))
# print(bisect_right(li, 9))

# def insort(li, n):
#   i = bisect(li, n)
#   li.insert(i, n)
#   print(li)

# if __name__ == "__main__":
#   for n in range(11):
#     li = [1,2,2,3,4,6,7,8,9]
#     print(li, n)
#     insort(li,n)
#     print()

def calculate_grade(marks):
  if marks >= 80:
    grade = "A+"
  elif marks >= 70:
    grade = "A"
  elif marks >= 60:
    grade = "A-"
  elif marks >= 50:
    grade = "B"
  elif marks >= 40:
    grade = "C"
  elif marks >= 33:
    grade = "F"
  return grade

def calculate_grade_bisect(marks):
  grades = ["F", "C", "B", "A-", "A", "A+"]
  grade_thresholds = [33, 40, 50, 60, 70, 80]
  i = bisect(grade_thresholds, marks)
  return grades[i]
if __name__ == "__main__":
  marks = int(input("Enter your marks: "))
  grade = calculate_grade_bisect(marks)
  print(grade)