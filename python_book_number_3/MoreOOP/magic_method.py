# class Car:
#   def __init__(self, name, manufacturer, year, price):
#     self.name = name
#     self.manufacturer = manufacturer
#     self.year = year
#     self.price = price
#   def __add__(self, other):
#     return self.price + other.price

# if __name__ == "__main__":
#   car1 = Car("A Class", "Toyota", 2017, 700000)
#   car2 = Car("A Class", "Toyota", 2017, 700000)
#   print(car1 + car2)
# ... existing code ...
# class Car:
#   def __init__(self, name, manufacturer, year, price):
#     self.name = name
#     self.manufacturer = manufacturer
#     self.year = year
#     self.price = price
  
#   def __repr__(self):
#     return "Car('{}', '{}', {})".format(self.name, self.manufacturer, self.year)

#   def __str__(self):
#     return "{} {} {}".format(self.name, self.manufacturer, self.year)
# if __name__ == "__main__":
#   car1 = Car("A Class", "Toyota", 2017, 700000)
#   print(car1)
#   print(car1.__repr__())

class Car:
  def __init__(self, name, manufacturer, year, price):
    self.name = name
    self.manufacturer = manufacturer
    self.year = year
    self._price = price

  @property
  def price(self):
    return '${:.2f}'.format(self._price)

  @price.setter
  def price(self, new_price):
    if not isinstance(new_price, (float, int)):
      print("invalid data for price")
    elif new_price < 0:
      print("Price can't be negative")
    else:
      self._price = new_price

if __name__ == "__main__":
  car1 = Car("A Class", "Toyota", 2017, 700000)
  car1.price = -1000000
  print(car1.price)
