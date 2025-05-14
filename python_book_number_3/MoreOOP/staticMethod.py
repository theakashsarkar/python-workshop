class Car:
  count = 0
  def __init__(self, name, manufacturer, color, year):
    print("Creating a car")
    self.name = name
    self.manufacturer = manufacturer
    self.color = color
    self.year = year
    Car.count += 1
  def change_gear(self, gear_name):
    print("Changing gear to", gear_name)
  @classmethod
  def desplay_count(cls):
    print("Car Count", cls.count)
  @classmethod
  def reset_count(cls):
    cls.count = 0
  @classmethod
  def reset_display_count(cls):
    cls.reset_count()
    cls.desplay_count()

if __name__ == "__main__":
  myCar1 = Car("A Class", "Toyota", "Black", 2017)
  myCar2 = Car("A Class", "Toyota", "Black", 2017)
  myCar3 = Car("A Class", "Toyota", "Black", 2017)
  Car.desplay_count()
  Car.reset_count()
  Car.desplay_count()