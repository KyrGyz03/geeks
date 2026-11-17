# """Простые примеры сложности алгоритмов Big O и декораторов."""


# # Big O показывает, как растёт количество работы при увеличении входных данных.
# def get_first(items):
#     """Получить первый элемент: O(1), размер списка почти не влияет на работу."""
#     return items[0]


# def contains_value(items, value):
#     """Поиск в списке: O(n) в худшем случае, где n — длина списка."""
#     for item in items:
#         if item == value:
#             return True
#     return False


# def count_pairs(items):
#     """Два вложенных цикла: O(n²), проверяем каждую пару элементов."""
#     pairs = 0
#     for _ in items:
#         for _ in items:
#             pairs += 1
#     return pairs


# # Декоратор принимает функцию и возвращает новую функцию-обёртку.
# def announce(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызывается функция {func.__name__}")
#         result = func(*args, **kwargs)
#         print("Функция завершилась")
#         return result

#     return wrapper


# # @announce — короткая запись для greet = announce(greet).
# @announce
# def greet(name):
#     return f"Привет, {name}!"


# if __name__ == "__main__":
#     numbers = [10, 20, 30, 40]

#     print("Первый элемент:", get_first(numbers))
#     print("Число найдено:", contains_value(numbers, 30))
#     print("Количество пар:", count_pairs(numbers))

#     print(greet("Алия"))