class Engine:
    def start(self):
        return "engine start"

class Wheels:
    def rotae(self):
        return "Wheel rotatin"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()
    
    def move(self):
        return f"{self.engine.start()}, {self.wheels.rotae()} "

car = Car()
print(car.move())