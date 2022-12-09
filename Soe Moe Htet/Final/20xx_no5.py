class EWallet:
    def __init__(self, owner, maxMoney):
        self.owner = owner
        self.maxMoney = maxMoney
        self.balance = 0
    
    def deposit(self, amount):
        if self.balance + amount <= self.maxMoney:
            self.balance += amount
            return (f"Deposited {amount}. Current balance: {self.balance}")
        else:
            return ("You have reached maximum amount of money for your account!")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return (f"Withdrawn {amount}. Current balance: {self.balance}")
        else:
            return ("You don't have enough money to withdraw!'")
    
    def getBalance(self):
        print(f"Current balance: {self.balance} THB")


class SmartEWallet(EWallet):

    def __init__(self, owner, maxMoney):
        super().__init__(owner, maxMoney)

        self.transaction_history = []


    def deposit(self, amount):
        self.transaction_history.append(super().deposit(amount))

    def withdraw(self, amount):
        self.transaction_history.append(super().withdraw(amount)) 


    def get_history(self):
        return self.transaction_history

s = SmartEWallet("Stephen", 20000)
s.deposit(10000)
s.withdraw(1999)
s.getBalance()

print(s.get_history())

    