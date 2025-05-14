from dataclasses import dataclass
@dataclass
class Car:
  name: str
  manufacturer: str
  year: int
  price: float

if __name__ == "__main__":
  car1 = Car("A Class", "Toyota", 2017, 700000)
  print(car1)
  car2 = Car("A Class", "Toyota", 2017, 700000)
  print(car2)
  print(car1 == car2)