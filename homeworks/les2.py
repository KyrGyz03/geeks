class Person:
    def __init__(self, name, b_day, job):
        self.name = name
        self.b_day = b_day
        self.job = job

    def introduce(self):
        print(f'--- Привет, меня зовут {self.name}, родился {self.b_day}, моя работа - {self.job}. ', end='')
        

class Classmate(Person):
    def __init__(self, group, *person):
        super().__init__(*person)
        self.group = group

    def introduce(self):
        super().introduce()
        print(f'Я учусь вместе с Байэлем в группе {self.group}')
        
        
class Friend (Person):
    def __init__(self, hobby, *person):
            super().__init__(*person)
            self.hobby = hobby

    def introduce(self):
        super().introduce()
        print(f'Нас с Байэлем связало общее хобби -  {self.hobby}')

class Bestfriend(Friend):
    def __init__(self, memory, *person):
        super().__init__(*person)
        self.memory = memory

    def introduce(self,):
        super().introduce()
        print(f'Мы стали близки с Байэлем после того, как {self.memory}')

mates = []
person = Person('Tom', '29.01.1990', 'строитель')
mates.append(person)

classmate1 = Classmate('72-1','Никита',' 18.05.2005', 'повар')
mates.append(classmate1)

classmate2 = Classmate('72-1','Карина',' 28.04.2004', 'риелтор')
mates.append(classmate2)

friend1 = Friend('Музыкальная игра, началось все с гитары','Петр','27.12.2002', 'строитель' )
mates.append(friend1)

friend2 = Friend('Готовка и хороший отдых', 'Игорь', '4.05.1989','повар')
mates.append(friend2)

bf1_memory = 'впервые поговорили по душам, нас ничто не отвлакало'
b_friend1 = Bestfriend(bf1_memory,'Философия и мировозрение','Georg',' 30.06.2004', 'таксист')
mates.append(b_friend1)

for prs in mates:
    prs.introduce()
    if prs == mates[0]:
        print()