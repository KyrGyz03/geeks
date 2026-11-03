class Person:
    def __init__(self, name, birth_day, occupation, high_educated:bool):
        self.name = name
        self.birth_day = birth_day
        self.occupation = occupation
        self.high_educated = high_educated

    def introduce(self):
        # print(f'---\nПривет! Меня зовут {self.name}, рожден  {self.birth_day}. Работаю по профессии: {self.occupation}.')
        # if self.high_educated:
        #     print('Высшее образование имеется.\n---')
        # else:
        #     print('Высшего образования нет\n---')
        print(f'---\nПривет! Меня зовут {self.name}, рожден  {self.birth_day}. Работаю по профессии: {self.occupation}. Высшее образование имеется.' 
                if self.high_educated == True else
                f'---\nПривет! Меня зовут {self.name}, рожден  {self.birth_day}. Работаю по профессии: {self.occupation}. Высшего образования нет.')
        # Вспомнил, что можно сократить выражение внутри вывода

person1 = Person('Илья', '15 марта 1996', 'Повар', False)
person1.introduce()

person2 = Person('Вера','4 апреля 1992','Администратор', True)
person2.introduce()

person3 = Person('Канат','23 октрября 1983','Шеф повар', True)
person3.introduce()