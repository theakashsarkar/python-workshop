class DeliveryMan:
    def __init__(self, name):
        self.name = name
    
    def deliver(self, package):
        print(f"{self.name} is delivering the package: {package}")
    
class Courier:
    def __init__(self, package):
        self.package = package

    def request_dalivery(self, daliveryMan: DeliveryMan):
        print("Courier: Please deliver this package.")
        daliveryMan.deliver(self.package)

