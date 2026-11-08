class Conctact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return True if len(phone_number) == 10 and phone_number.isdigit() else False

class ContactList():
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Conctact.validate_phone_number(phone_number):
            new_contact = Conctact(name, phone_number)
            cls.all_contacts.append(new_contact)
            print(f'Контакт {name} добавлен')
        else:
            raise ValueError(f'Неправильный номер телефона')


print(ContactList.all_contacts) # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

# так как all_contacts является списком, можно пройти по нему циклом
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)
    # Вася Пупкин 0700100200
    # Виктор Цой 0500123456

ContactList.add_contact("John Doe", "5551234") 
# получаем ValueError потому что количество цифр не подходит


class Library:
    def __init__(self, city, books=None):
        self.city = city
        self.books = books

    def __str__(self):
        return f'{self.city}: {len(self.books)}'

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        return item in self.books

    def __bool__(self):
        return len(self.books) >5


lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])
print(lib)
print(len(lib))
print("1984" in lib)
print("Гарри Поттер" in lib)
if lib:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")