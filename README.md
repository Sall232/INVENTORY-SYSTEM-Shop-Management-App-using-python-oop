# INVENTORY SYSTEM (Shop Management App)

 # Overview

The INVENTORY SYSTEM (Shop Management App) is a Python-based console application built using Object-Oriented Programming (OOP) principles. It helps manage shop products by tracking stock levels, processing sales, and generating inventory reports.

This project was developed as part of a learning journey to strengthen understanding of Python OOP concepts such as classes, objects, methods, encapsulation, and modular programming.

---

# Features

# 📦 Product Management

* Create and manage products
* Store product details such as name, price, and quantity

# 📊 Stock Tracking

* Monitor product quantities in inventory
* Add and update stock levels
* Prevent selling more items than available

# 💰 Sales Processing

* Sell products from inventory
* Automatically update stock after each sale
* Return messages for successful or failed transactions

# 📈 Inventory Reporting

* Calculate total inventory value
* Display all products with current stock and price

---

## Project Structure

```text
INVENTORY_SYSTEM/
│
├── product.py        # Product class (stock, sales, value calculation)
├── inventoryApp.py   # Inventory class (manages product collection)
├── main.py           # Application entry point
└── README.md         # Project documentation
```

---

# How to Run the Project

1. Clone the repository or download the files
2. Ensure Python 3 is installed
3. Run the main file:

```bash
python main.py
```

---

# Example Usage

```python
from product import Product
from inventoryApp import Inventory

inventory = Inventory()

rice = Product("Rice", 10, 10)
sugar = Product("Sugar", 5, 10)

inventory.add_product(rice)
inventory.add_product(sugar)

rice.sell(3)

print(inventory.report())
```

---

# Example Output

```text
Sold 3 Rice(s)
Current Inventory Value: Le 85
```

---

# OOP Concepts Used

* Classes and Objects
* Encapsulation
* Methods and Attributes
* Object Interaction
* Modular Programming

---

# Future Improvements

* Product search feature
* Low stock alerts
* Sales history tracking
* Data saving using JSON or CSV
* GUI version using Tkinter
* Database integration

---

## Author

**Sallu Sidikie**

Developed as part of a Python Object-Oriented Programming learning journey.
