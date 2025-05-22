# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# point = Point(1, 2)
# print(point.x, point.y)

import collections 

Student = collections.namedtuple('Student', ['name', 'age', 'grade'])
student = Student('akash', '22', 'A')
print(student[1])
print(student.name)