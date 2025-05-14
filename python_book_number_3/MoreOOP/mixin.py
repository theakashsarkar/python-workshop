class Car:
  def __init__(self, name, manufacturer, price):
    self.name = name
    self.manufacturer = manufacturer
    self.price = price
  
class CarPriceMixin:
  def clearance_price(self):
    return self.price * 0.7
class ShowRoomCar(Car, CarPriceMixin):
  pass

if __name__ == "__main__":
  c = ShowRoomCar("A Class", "Toyota", 38000)
  print("Clearance price", c.clearance_price()) 