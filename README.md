class Item:  # Клас Item для визначення товару

    def __init__(self, name, price, description, dimensions):  # Ініціалізатор для класу Item
        self.price = price  # Задати ціну товару
        self.description = description  # Задати опис товару
        self.dimensions = dimensions  # Задати розміри товару
        self.name = name  # Задати ім'я товару

    def __str__(self): # lemon, price: 5  # Метод для перетворення об'єктів в рядок
        # print(self.dimensions)  # Закоментовано, але може використовуватися для виведення розмірів
        return f"{self.name}, price: {self.price}"  # Повернення рядка з ім'ям товару і ціною

class User:  # Клас User для визначення користувача

    def __init__(self, name, surname, numberphone):  # Ініціалізатор для класу User
        self.name = name  # Задати ім'я користувача
        self.surname = surname  # Задати прізвище користувача
        self.numberphone = numberphone  # Задати номер телефону користувача

    def __str__(self):  # Метод для перетворення об'єктів в рядок
        return f"{self.name.title()} {self.surname.title()}"  # Повернення рядка з ім'ям та прізвищем користувача

class Purchase:  # Клас Purchase для визначення покупки
    def __init__(self, user):  # Ініціалізатор для класу Purchase
        self.products = {}  # Задати порожній словник для продуктів
        self.user = user  # Задати користувача для покупки
        self.total = 0  # Задати початкову вартість покупки

    def add_item(self, item, cnt):  # Метод для додавання товару до покупки
        self.products[item] = cnt  # Додати товар і його кількість до словника продуктів

    def __str__(self):  # Метод для перетворення об'єктів в рядок
        all_products = ""  # Ініціалізація порожнього рядка для всіх продуктів
        for product, count in self.products.items():  # Перебирати всі товари та їх кількість
            all_products += f"
{product.name}: {count} pcs."  # Додати товар і його кількість до рядка
        return f"User: {self.user}
Items:{all_products}"  # Повернення рядка з користувачем і всіма товарами

    # """
    # User: Ivan Ivanov
    # Items:
    # lemon: 4 pcs.
    # apple: 20 pcs.
    # """

    def get_total(self):  # Метод для отримання загальної вартості покупки
        all_sum = 0  # Ініціалізація змінної для підрахунку загальної суми
        for product, count in self.products.items():  # Перебирати всі товари та їх кількість
            all_sum += (product.price * count)  # Додати вартість товару до загальної суми
        return all_sum  # Повернення загальної суми

lemon = Item('lemon', 5, "yellow", "small")  # Створення екземпляра класу Item
print(lemon)  # Виведення інформації про лимон
# test1 = lemon.__str__()  # Закоментовано тестовий рядок для виклику методу __str__
# print(test1)  # Закоментовано виведення результату методу __str__
# test2 = str(lemon)  # Закоментовано тестовий рядок для виклику функції str
# print(test2)  # Закоментовано виведення результату функції str
apple = Item('apple', 2, "red", "middle")  # Створення екземпляра класу Item
# print(lemon)  # lemon, price: 5  # Закоментовано виведення інформації про лимон
buyer = User("Ivan", "Ivanov", "02628162")  # Створення екземпляра класу User
print(buyer)  # Ivan Ivanov  # Виведення інформації про користувача
#
cart = Purchase(buyer)  # Створення екземпляра класу Purchase
cart.add_item(lemon, 4)  # Додавання лимонів до покупок
cart.add_item(apple, 20)  # Додавання яблук до покупок
print(cart)  # Виведення інформації про покупку
print(cart.get_total())  # Виведення загальної вартості покупок
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'  # Перевірка, що користувач є екземпляром класу User
assert cart.get_total() == 60, "Всього 60"  # Перевірка загальної вартості покупок
assert cart.get_total() == 60, 'Повинно залишатися 60!'  # Перевірка загальної вартості покупок
cart.add_item(apple, 10)  # Додавання яблук до покупок
print(cart)  # Виведення інформації про покупку
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
#
assert cart.get_total() == 40  # Перевірка загальної вартості покупок
