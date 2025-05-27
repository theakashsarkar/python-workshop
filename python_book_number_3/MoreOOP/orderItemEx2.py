from typing import List
class OrderItem:
    def __init__(self, price: int, quantity: int):
        self.price = price
        self.quantity = quantity
    
    def orderItemPrice(self) -> int:
       return self.price * self.quantity
    
class Order:
    def __init__(self):
        self.items: List[OrderItem] = []
     
    def addItem(self, item: OrderItem):
        self.items.append(item)
    
    def calculateTotalPrice(self):
        total: int = 0
        for item in self.items:
            total += item.orderItemPrice()
        return total

order = Order()
order.addItem(OrderItem(100, 2))
order.addItem(OrderItem(50,3))
print(order.calculateTotalPrice())