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


# END class BankAccount


class User:
    def __init__(
        self,
        first_name,
        last_name,
        email,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account = BankAccount(interest_rate=0.01, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        print(f"Deposit: {amount}")
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        print(f"Withdrawal: {amount}")
        return self

    def display_user_balance(self):
        print("Balance:", self.account.balance)
        return self


# END class User


user01 = User("John", "Malkovic", "jmalkov@gmail.com")
user01.make_deposit(1_250)
user01.display_user_balance()
user01.make_withdrawal(550)
user01.display_user_balance()

# # This is an object instance. Specify class "User"
# user_001 = User("John", "Schiller", "schiller@google.com", 28, "USA")
# user_002 = User("Njemanja", "Djokovic", "djokovic@gmail.com", 35, "Serbia")
# print("========")
# user_001.greeting()
# user_001.verify_age_country()
# user_002.greeting()
# user_002.verify_age_country()
# print("========")

# account01 = BankAccount(0.01, 500)
# account02 = BankAccount(0.01, 100)
# print("----")
# account01.display_account_info()
# account02.display_account_info()
# print("----")
# account01.deposit(10).deposit(43).deposit(57).withdraw(
#     100
# ).yield_interest().display_account_info()
# print("----")
# account02.deposit(950).deposit(550).withdraw(1200).withdraw(
#     375
# ).yield_interest().display_account_info()
# print("----")
