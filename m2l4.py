from abc import ABC, abstractmethod


class Notifications():
    def __init__(self, name):
         self.name = name

    def sendNot(self,type, message):
        if type == "Telegram":
            print(f"Отправка Telegram-уведомления: {message}")
        elif type == "Email":
              print(f"Отправка Email-уведомления: {message}")
        elif type == "SMS":
              print(f"Отправка SMS-уведомления: {message}")
        elif type == "VK":
              print(f"Отправка VK-уведомления: {message}")

class EmailNots(Notifications):
	def send(self, message: str) -> None:
		print(f"Отправка email-уведомления: {message}")

class SMSNots(Notifications):
    def send(self, message: str) -> None:
        print(f"Отправка SMS-уведомления: {message}")

class TelegramNots(Notifications):
    def send(self, message: str) -> None:
        print(f"Отправка сообщения в Telegram: {message}")

class vkNots(Notifications):
     def send(self, message):
          return super().send(message)

# Функция-клиент. Она знает только про абстрактный класс Notifications
def notify_user(notification_service: Notifications, text: str):
    # Мы вызываем метод send, не зная деталей его внутренней реализации
    notification_service.send(text)

if __name__ == "__main__":
    # Создаем список различных систем уведомлений (все они наследники Notifications)
    services = [
        EmailNots(),
        SMSNots(),
        TelegramNots()
    ]
    
    # Рассылаем одно и то же сообщение через разные каналы
    print("--- Демонстрация работы абстракции ---")
    for service in services:
        notify_user(service, "Ваш заказ отправлен")
