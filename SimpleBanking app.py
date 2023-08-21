# Banking app. You have different types of bank accounts such as "savings account" and "checking account". Both of
# these types of accounts share some common properties and traits/behaviour but also have specific unique features to
# each type

class Bankaccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}.New balance {self.balance}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account {self.account_number} balance:{self.balance}")


class SavingsAccount(Bankaccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.03

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def display_balance(self):
        super().display_balance()
        print(f"Interest earned:{self.calculate_interest()}")


class CheckingAccount(Bankaccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.overdraft_limit = 2000.0

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}.New balance {self.balance}")
        else:
            print("Insufficient amount")


savings_acc = SavingsAccount("EGFTSD", 1500.0)
checking_acc = CheckingAccount("GF4567", 2000.0)

savings_acc.deposit(690.0)
savings_acc.display_balance()

checking_acc.withdraw(900.0)
checking_acc.display_balance()
