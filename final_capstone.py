#1
# Reverse a String - Enter a string and the program will reverse it and print it out.

def reverse_string(s):
  return s[::-1]

#print(reverse_string('Example String'))


# 2

# Product Inventory Project - Create an application which manages an inventory
# of products. Create a product class which has a price, id, and quantity on hand.
#Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Products:

  def __init__(self, product, price, id, quantity):
    self.product = product
    self.price = price
    self.id = id
    self.quantity = quantity

  def __str__(self):
    return f"There are {self.quantity} {self.product} left in stock. Each costs {self.price}. ID is {self.id}."

class Inventory():

  def __init__ (self):
    self.listproducts = []





apples = Products('apples', 1.99, 1234, 40)
#print(apples.price)
#print(apples.__str__())
oranges = Products('oranges', 1.89, 2345, 60)

Inventory.add_products(apples)
Inventory.add_products(oranges)


#print(Inventory.total_value())


