# class BankAccount:
#     def __init__(self, name, balance, pin):
#         self.name = name
#         self.__balance = balance
#         self._pin = pin
#     def get_balance(self):
#         return self.__balance
    
#     def withdraw(self, amount):
#         if amount >= self.__balance:
#             print('Not enough money in balance')
#         else:
#             self.__balance -= amount

#     def deposit(self, amount):
#         self.__balance += amount

# ac1 = BankAccount('tom', 100, 1234)
# print(ac1.get_balance())
# ac1.withdraw(90)
# print(ac1.get_balance())

class Example:
	def __init__(self):
		self._protected = "защищённый атрибут"
		self.__private = "приватный атрибут"

	@property
	def get_private(self):
		return self.__private


obj = Example()

# Защищённый атрибут можно прочитать напрямую, но по соглашению
# его используют только внутри класса и его наследников.
print(obj._protected)
obj.__private = 'Измененный атрибут'
# Приватный атрибут читается через публичный метод.
print(obj.get_private())
