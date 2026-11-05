TRIP_COST = 20

class TransportCard:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        return self.__owner

    def get_balanec(self):
        return self.__balance

    def add_money(self, amount):
        try:
            self.__balance += amount
            if amount <= 0:
                raise ValueError(f'Сумма пополнения не может быть нулевой или отрицательной!')
            print(f'{self.__owner} -- Сумма пополнена: {amount}')
        except ValueError as e:
            if str(e):
                print(f'Ошибка: {e}')
            else:
                print('Ошибка: требуется ввести число')
        
    def pay_for_trip(self):
        try:
            self.__balance -= TRIP_COST
            if self.__balance <= TRIP_COST:
                raise ValueError(f'Не хватает денег на оплату поездки!')
            print(f'{self.__owner} -- Поездка оплачена')
        except ValueError as e:
            if str(e):
                print(f'Ошибка: {e}')
            else:
                print('Ошибка: требуется ввести число')

    def check(self):
        print(f'Владелец: {self.get_owner()}, баланс: {self.get_balanec()}')

card1 = TransportCard('Tom', 0)
card2 = TransportCard('John', 0)
card1.add_money(50)
card2.add_money(100)
card1.check()
card2.check()

card2.pay_for_trip()
card1.check()
card2.check()