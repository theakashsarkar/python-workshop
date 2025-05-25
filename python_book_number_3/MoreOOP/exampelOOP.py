# array = []

# while(True):
#     input1 = input("Enter a number")
#     number = int(input1)
#     array.append(number)
#     if len(array) >= 5:
#         print(array) 
#         array = []

# class AlphabetStore:

#     def __init__(self):
#         self.array = []

#     def take_input(self):
#         input1 = int(input("Enater a number"))
#         self.add_to_array(input1)

#     def add_to_array(self, input):
#         self.array.append(input)
#         if len(self.array) >= 5:
#             self.print_and_flush()

#     def print_and_flush(self):
#         print(self.array)
#         self.array = []

# #  generate a object from blueprint

# if __name__ == "__main__":
#     alphabetStore = AlphabetStore()
#     while True:
#         alphabetStore.take_input()

from dataclasses import dataclass
from typing import List, Dict, Tuple
from abc import ABC, abstractmethod


@dataclass
class TicketPricingStrategy(ABC):

    @abstractmethod
    def calculate_ticket_price(self):
        pass

@dataclass 
class TicketPriceInterCity(TicketPricingStrategy):
    service_charge: int = 10
    per_kilometer: int  = 2.5
    distance: float = 0.0

    def calculate_ticket_price(self):
        return self.service_charge + (self.per_kilometer * self.distance)

class BusTicketPriceCalculationBrta:
    def __init__(self):
        self.price_matrix: Dict[Tuple[str, str], TicketPricingStrategy] = {
            ('Dhaka', 'Sylhet'): TicketPriceInterCity(
                distance = 250
            ),
            ('Dhaka', 'Chittagong'): TicketPriceInterCity(
                distance=300.0
            ), 
            ('Gulistan', 'Muktarpur'): TicketPriceInterCity(
                distance=45
            )
        }
    
    def get_price(self, from_city: str, to_city: str):
        route = (from_city, to_city)
        if route in self.price_matrix:
            return self.price_matrix[route].calculate_ticket_price()
        
class BusTicket:
    
    def __init__(self):
        self.brta_ticket_price = BusTicketPriceCalculationBrta()
    
    def get_bus_seat_price(self, from_city: str, to_city: str):
        price = self.brta_ticket_price.get_price(from_city, to_city)
        return price

    def get_bus_ticket(self, amount):
        try:
            
            return 'A5'
        except ValueError as e:
            print(e)    
    # def get_ticket_check_helper(self):
    #     self.get_bus_ticket()

def demonstrate():
    ticket_service = BusTicket()
    price = ticket_service.get_bus_seat_price('Gulistan', 'Muktarpur')
    if price:
        print(f"Ticket price: {price}")

if __name__ == "__main__":
    demonstrate()


