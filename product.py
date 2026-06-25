'''
This  app manage products in a shop:
Stock tracking
sales
Inventory report


sign---Sallu Sidikie
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity-=amount
        else:
            return "Not enough stock"
        
    def total_value(self):
        return self.price * self.quantity
    
    def is_low_stock(self):
        return self.quantity < 5

