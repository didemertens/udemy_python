#1
# Reverse a String - Enter a string and the program will reverse it and print it out.

def reverse_string(s):
  return s[::-1]

#print(reverse_string('Example String'))


# 2

# Product Inventory Project - Create an application which manages an inventory
# of products. Create a product class which has a price, id, and quantity on hand.
#Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Product:

  def __init__(self, product=None, price=0, id=0, quantity=0):
    self.product = product
    self.price = price
    self.id = id
    self.quantity = quantity

  def __str__(self):
    return f"There are {self.quantity} {self.product} left in stock. Each costs {self.price}. ID is {self.id}."

class Inventory():

  def __init__(self,price,quantity):
    self.products = []

  def total_value(self):
    return (product_1.quantity * product_1.price)


product_1 = Product('apples', 2, 1234, 40)
product_2 = Product('oranges', 3, 2345, 60)

inventory1 = Inventory(product_1.price, product_1.quantity)
print(inventory1.total_value())
