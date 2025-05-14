# from dataclasses import dataclass
# @dataclass
# class Car:
#   name: str
#   manufacturer: str
#   year: int
#   price: float

# if __name__ == "__main__":
#   car1 = Car("A Class", "Toyota", 2017, 700000)
#   print(car1)
#   car2 = Car("A Class", "Toyota", 2017, 700000)
#   print(car2)
#   print(car1 == car2)

from dataclasses import dataclass, field, asdict, astuple
@dataclass(order=True)
class Car:
  sort_index: int = field(init=False, repr=False)
  name: str
  manufacturer: str
  year: int 
  price: float

  def __post_init__(self):
    self.sort_index = self.price
if __name__ == "__main__":
  car1 = Car("A Class", "Toyota", 2017, 700000)
  car2 = Car("Prado", "Toyota", 2017, 700000)
  car3 = Car("Corolla", "Toyota", 2021, 32000)
  print(car1)
  print(car2)
  print(car1 > car2)
  print(car2 > car3)
  print(asdict(car1))
  print(astuple(car1))