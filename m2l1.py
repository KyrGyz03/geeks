class Car:
    def __init__(self, made, color):
        self.made = made
        self.color = color
    def driving(self, dest):
        print(f'"{self.color} {self.made}" going to {dest}')




class Character:
    def __init__(self, name, role, is_evil, dmg):
        self.name = name
        self.role = role
        self.is_evil = is_evil
        self.dmg = dmg

    def print_character(self):
        print(f'---\n{self.name} is {self.role}, {self.is_evil}, deals {self.dmg} damage\n---')


if __name__ == "__main__":
    tank = Character('Sion', 'tank', 'not evil', '100')
    tank.print_character()