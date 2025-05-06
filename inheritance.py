class Vehicle:
  """Base class for all vehicles"""
  def __init__(self, name, manufacturer, color):
    self.name = name
    self.manufacturer = manufacturer
    self.color = color
  def drive(self):
    print("Driving", self.manufacturer, self.name)
  def turn(self, direction):
    print("Turning", self.name, "to", direction)
  def brake(self):
    print(self.name, "is stopping")
if __name__ == "__main__":
  v1 = Vehicle("Fusion 110 Ex", "Walton", "Black")
  v2 = Vehicle("softail Delux", "Harley-Davidson", "Blue")
  # v1.drive()
  # v2.drive()
  # v1.turn("left")
  # v2.turn("right")
  # v1.brake()
  # v2.brake()

# class Car(Vehicle):
#   """Car class"""
#   def change_gear(self, gear_name):
#     """Method for changing gear"""
#     print(self.name, "is changing gear to", gear_name)
#   def turn(self, direction):
#     print(self.name, "is turning", direction)
# if __name__ == "__main__":
#   c = Car("Mustang 5.0 GT Coupe", "Ford", "Red")
#   c.drive()
#   c.brake()
#   c.change_gear("P")


# class Vehicle: 
#   """Base class for all vehicles"""
#   def __init__(self, name, manufacturer, color):
#     print("Creating a vehicle")
#     self.name = name
#     self.manufacturer = manufacturer
#     self.color = color

# class Car(Vehicle):
#   def __init__(self, name, manufacturer, color):
#     print("Creating a car")
#     super().__init__(name, manufacturer, color)
#     self.year = 2017
#     self.wheels = 4
# class MotorCycle(Vehicle):
#   def __init__(self, name, manufacturer, color):
#     print("Creating a MotorCycle")
#     self.name = name
#     self.manufacturer = manufacturer
#     self.color = color
#     self.year = 2017
#     self.wheels = 2
# if __name__ == "__main__":
#   c = MotorCycle("Suzuki Gixxer 150", "suzuki", "Red")
#   print(c.name, c.year, c.wheels)

import turtle
class AjobTurtle(turtle.Turtle):
  """AjobTurtle is a class for new type of turtle"""

if __name__ == "__main__":
  montu = AjobTurtle()
  print(type(montu))
  montu.left(30)
  montu.forward(200)
  turtle.done()