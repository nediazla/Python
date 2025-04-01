import csv
import os
from datetime import datetime

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self)::
        return f"{self.product_id}: {self.name} - ${self.price:.2f} ({self.quantity} units)"

class  RetailSystem:
    def __init__(self):
        self.products = {}
        self.load_products()

    def load_products(self):
        try:
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.products[row['product_id']] = Product(
                        row['product_id'],
                        row['name'],
                        float(row['price']),
                        int(row['quantity']))
        except FileNotFoundError:
            pass

    def save_product(self):
        with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['product_id', 'name', 'price', 'quantity'])
            for product in self.products.values():
                writer.writerow([product.produc_id, product.name, product.price, product.quantity])

    def add_product(self, product_id, name, price, quantity):
        if product_id in self.products:
            print("Product ID ya existe")
            return False
        self.products[product_id] = Product(product_id, name, price, quantity)
        self.save_product()
        return True

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
            self.save_product()
            return True
        return False

    def edit_price(self, product_id, new_price):
        if product_id in self.products:
            self.products[product_id].price = new_price
            self.save_product()
            return True
        return False

    def process_sale(self, cart):
        total = 0
        receipt_items = []
        for product_id, quantity in cart.items():
            if self.products[product_id].quantity >= quantity:
                total += self.products[product_id].price * quantity
                self.products[product_id].quantity -= quantity
                receipt_items.append((
                    self.products[product_id].name,
                    quantity,
                    self.products[product_id].price,
                    self.products[product_id].price * quantity
                ))
            else:
                print(f"no hay suficentes {self.products[product_id].name}")
                return None

        self.save_product()
        return {'total': total, 'items': receipt_items}

    def list_products(self):
        return list(self.products.values())