from abc import ABC, abstractmethod
class Vehicle(ABC):
  def __init__(self, name, manufacturer, color):
    self.name = name
    self.manufacturer = manufacturer
    self.color = color
  
  def turn(self, direction):
    print("Turning", self.name, "to", direction)
  
  @abstractmethod
  def change_gear(self, gear_name):
    pass

class Car(Vehicle):

  def __init__(self, name, manufacturer, color, year):
    super().__init__(name, manufacturer, color)
    self.year = year

  def change_gear(self, gear_name):
    print("Change gear to", gear_name)

if __name__ == "__main__":
  car1 = Car("A Class", "Toyota", "Black", 2017)
  print(car1.name)
  car1.change_gear("D")
  car1.turn("Right")