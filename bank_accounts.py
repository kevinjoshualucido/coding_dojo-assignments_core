class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Balance: {self.balance}")
            return self
        else:
            print("--Insufficient funds: Charging a $5 fee")
            print(f"Balance: {self.balance - 5}")
            return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        self.balance += self.interest_rate * self.balance
        print("Balance:", self.balance)
        return self


account01 = BankAccount(0.01, 500)
account02 = BankAccount(0.01, 0)
print("----")
print("Balance:", account01.display_account_info())
print("Balance:", account02.display_account_info())
print("----")
account01.deposit(10).deposit(43).deposit(57).withdraw(100).yield_interest().display_account_info()
print("----")
account02.deposit(950).deposit(550).withdraw(1200).withdraw(375).yield_interest().display_account_info()
print("----")
