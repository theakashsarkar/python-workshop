from typing import List

class OrderCalculator:
    def __init__(self):
        self.totalCost: int = 0
    
    def addCost(self, cost: int):
        self.totalCost += cost
    
    def printTotalCost(self):
        print(self.totalCost)

class OrderItem:
    def __init__(self, price: int, quantity: int):
        self.price = price
        self.quantity = quantity
    
    def calculateCost(self) -> int:
        return self.price * self.quantity
    
    def contributeCostTo(self, orderCal: OrderCalculator) -> None:
        orderCal.addCost(self.calculateCost())

class Order:
    def __init__(self):
       self.items: List[OrderItem] = []
    
    def addItem(self, item: OrderItem):
        self.items.append(item)

    def calculateTotalPrice(self):
        calculator = OrderCalculator()
        for item in self.items:
            item.contributeCostTo(calculator)
        calculator.printTotalCost()

order = Order()
order.addItem(OrderItem(100, 2))
order.addItem(OrderItem(50,3))
order.calculateTotalPrice()