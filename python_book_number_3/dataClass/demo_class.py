class DemoPlainClass:
    a: int
    b: str = 1.1
    c = 'spam' 

print(DemoPlainClass.__doc__)
# de = DemoPlainClass()
# de.a = 8
# print(de.a)

# import typing
# from dataclasses import dataclass
# @dataclass
# class DemoNTClass(typing.NamedTuple):
#     a: int
#     b: float = 1.1
#     c = 'spam'

# print(DemoNTClass.__annotations__)
# print(DemoNTClass.a)
# print(DemoNTClass.b)
# print(DemoNTClass.__doc__)
# print(nt.b = 2.2)
# print(nt.z)
# nt = DemoNTClass(1)
# nt.a = 10
# print(nt.a)