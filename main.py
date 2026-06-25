from product import Product
from inventoryApp import Inventory

#Create an Inventory Object
myInventory = Inventory()

#Creat product
p1 = Product("Rice", 10, 10)
p2 = Product("Sugar", 5, 10)


#Add products in inventory
myInventory.add_product(p1)
myInventory.add_product(p2)

#sell some rice
p1.sell(5)


#Generate report
final_report = myInventory.report()
print(final_report)