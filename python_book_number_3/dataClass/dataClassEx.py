from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = "spam"

# print(DemoDataClass.__annotations__)
# print(DemoDataClass.__doc__)
dc = DemoDataClass(a)
print(dc.b)
dc.a = 10
print(dc.a)
dc.c = "akash"
print(dc.c)
dc.z = "akash2"
print(dc.z)

