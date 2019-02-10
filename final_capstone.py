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

  def __init__(self, product_list=[]):
    self.products = product_list

  def add_product(self, product):
    self.products.append(product)

  def total_value(self):
    total_value = 0
    for product in self.products:
      total_value += (product.quantity * product.price)
    return total_value


product_1 = Product('apples', 2, 1234, 5)
product_2 = Product('oranges', 2, 2345, 5)

inventory1 = Inventory([product_1,product_2])
# inventory1.add_product(product_1)
# inventory1.add_product(product_2)
print(inventory1.total_value())
