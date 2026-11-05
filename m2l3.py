class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self._pin = pin
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount >= self.__balance:
            print('Not enough money in balance')
        else:
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

ac1 = BankAccount('tom', 100, 1234)
print(ac1.get_balance())
ac1.withdraw(90)
print(ac1.get_balance())
