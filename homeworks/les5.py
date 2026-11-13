class Distance:
    UNIT_TO_METERS = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
    }

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f'{self.value}{self.unit}'

    def convert(self, unit: str):
        if self.unit not in self.UNIT_TO_METERS:
            raise ValueError(f'Неизвестная единица измерения: {self.unit}')
        if unit not in self.UNIT_TO_METERS:
            raise ValueError(f'Неизвестная единица измерения: {unit}')
        
        return self.value * self.UNIT_TO_METERS[self.unit] / self.UNIT_TO_METERS[unit]
                

    def __add__(self, other):
        if not isinstance(other, Distance):
            return ValueError
        return Distance(self.value + other.convert(self.unit), self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
             return ValueError
        return Distance(self.value - other.convert(self.unit), self.unit)
    
    def __eq__(self, other):
        if not isinstance(other, Distance):
                    return ValueError
        if self.value > other.convert(self.unit):
            return f'{self.value}{self.unit} is bigger than {other.value}{other.unit}'
        elif self.value == other.convert(self.unit):
            return 'Equal'
        else:
            return f'{other.convert(self.unit)} is bigger than {self.value}'

obj1 = Distance(3, 'km')
obj2 = Distance(4, 'cm')

print(obj1, obj2)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 == obj2)