class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self): # lemon, price: 5
        # print(self.dimensions)
        return f"{self.name}, price: {self.price}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        all_products = ""
        for product, count in self.products.items():
            all_products += f"\n{product.name}: {count} pcs."
        return f"User: {self.user}\nItems:{all_products}"

    # """
    # User: Ivan Ivanov
    # Items:
    # lemon: 4 pcs.
    # apple: 20 pcs.
    # """

    def get_total(self):
        all_sum = 0
        for product, count in self.products.items():
            all_sum += (product.price * count)
        return all_sum


lemon = Item('lemon', 5, "yellow", "small")
print(lemon)
# test1 = lemon.__str__()
# print(test1)
# test2 = str(lemon)
# print(test2)
apple = Item('apple', 2, "red", "middle")
# print(lemon)  # lemon, price: 5
buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov
#
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print(cart.get_total())
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
#
assert cart.get_total() == 40