from typing import Protocol

class Withdrawable(Protocol):
    def withdraw(self, amount: int):
        pass

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
    
    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
    
class CurrentAccount:
    def __init__(self, initial_balance: int):
        self.account = BankAccount(initial_balance)
    def deposit(self, amount: int):
        self.account.deposit(amount)

    @property
    def balance(self):
        return self.account.balance

    def withdraw(self, amount: int):
        if amount > 0 and amount > self.account.balance :
            self.account.balance -= amount


class SavingAccount:
    def __init__(self, initial_balance: int):
        self.account = BankAccount(initial_balance)
    
    def is_matured(self):
        return True

    @property
    def balance(self):
        return self.account.balance

    def deposit(self, amount: int):
        self.account.deposit(amount)

    def withdraw(self, amount: int):
        if amount > 0 and amount > self.account.balance :
            self.account.balance -= amount and self.is_matured()


if __name__ == "__main__":
    current = CurrentAccount(1000)
    savings = SavingAccount(500)
    print(f"{current.balance} savings {savings.balance}")
    current.deposit(200)
    print(f"{current.balance} savings {savings.balance}")