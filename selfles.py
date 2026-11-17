class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f'Автомобиль: {self.brand} {self.model}, цена: {self.price}. А в сомах: {self.usd_to_som(self.price)}'

    @staticmethod
    def usd_to_som(amount):
        return amount * 85

    @classmethod
    def from_string(cls, data_string):
        brand, model, price = data_string.split("-")
        price = int(price)
        return cls(brand, model, price)

class Tech:
    def __init__(self, battery):
        self.battery = battery

    def show_battery(self):
        print(f'Заряд батареи: {self.battery}')

class ElectroCar(Car, Tech):
    def __init__(self, *car):
        super().__init__(*car)
    def __str__(self):
        return super().__str__() + f' Тип: Электрокар.'


carList = []

bmw1 = Car('BMW', 'X5', 1000)
carList.append(bmw1)
bmw2 = Car('BMW', 'GTR M3', 1500)
carList.append(bmw2)
tesla = ElectroCar('Tesla','urban', 900)
carList.append(tesla)

for i in carList:
    print(i)

data = 'Taycan-Porche-80000'
taycan = ElectroCar.from_string(data)
print(taycan)