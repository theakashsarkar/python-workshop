from typing import Protocol

class Withdrawable(Protocol):
    def withdraw(self, amount):
        pass

class CurrentAccount:
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance
    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
    
    def transfer(self, target_account: 'CurrentAccount', amount: int):
        if self.withdraw(amount):
            return target_account.deposit(amount)    
    
    def withdraw(self, amount: int):
        if amount > 0 and amount < self.balance:
            self.balance -= amount

class SavingAccount(CurrentAccount):
    def __init__(self, initial_balance = 0):
        super().__init__(initial_balance)

    def is_matured():
        return True

    def withdraw(self, amount: int):
        if amount > 0 and amount < self.balance :
            self.balance -= amount and self.is_matured()

if __name__ == "__main__":
    current = CurrentAccount(1000)
    savings = SavingAccount(500)
    print(f"{current.balance} savings {savings.balance}")
    current.deposit(200)
    print(f"{current.balance} savings {savings.balance}")