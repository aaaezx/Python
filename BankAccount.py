class BankAccount:
    def __init__(self):
        self.money = 0
    def __init__(self, money):
        self.money=money
    def withdraw(self, minus):
        self.money = self.money-minus
    def deposit(self, plus):
        self.money = self.money+plus
    def balance(self):
        return self.money

x = BankAccount(700)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(7)
print(x.balance())
