class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        
        return None
    
    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]

    def report(self):
        total = 0
        for p in self.products:
            total += p.total_value()

        return f"The total value of all products in inventory is Le {total}"
    