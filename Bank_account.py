class BankAccount(object):
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_amount):
        BankAccount.__init__(self)
        self.minimum_amount = minimum_amount

    def withdraw(self, amount):
        if self.balance - amount > self.minimum_amount:
            self.balance -= amount
            return self.balance
        else:
            print("Balance too low to withdraw, please deposit more money in your account")
            return self.balance


account1 = BankAccount()
account2 = MinimumBalanceAccount(10)

account1.deposit(20)
account2.deposit(30)

account1.withdraw(15)
account2.withdraw(21)


