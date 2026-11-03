from m2l1 import Car

class ElectroCar(Car):
    def __init__(self, made, color, battery):
        super().__init__(made, color)
        self.battery = battery


if __name__ == '__main__':
    eCar_Tesla = ElectroCar('Tesla', 'White', 10)
    print(f'{eCar_Tesla.color} {eCar_Tesla.made} has {eCar_Tesla.battery}k mAm')