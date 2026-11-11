TRIP_COST = 20

class TransportCard:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance



    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, amount:int):
        if amount <= 0:
            raise ValueError('Сумма пополнения не может быть нулевой или отрицательной!')
        self.__balance += amount
        print(f'{self.__owner} -- Сумма пополнена: {amount}')

        
    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            raise ValueError('Не хватает денег на оплату поездки!')
        self.__balance -= TRIP_COST
        print(f'{self.__owner} -- Поездка оплачена')


    def check(self):
        print(f'Владелец: {self.get_owner()}, баланс: {self.get_balance()}')

card1 = TransportCard('Tom', 0)
card2 = TransportCard('John', 0)
card1.add_money(50)
card2.add_money(20)

card1.check()
card2.check()

card1.pay_for_trip()
card2.pay_for_trip()

card1.check()
card2.check()