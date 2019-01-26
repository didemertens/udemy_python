# magic/dunder methods = special methods with __X__ (like init)

class Book():

  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return f"{self.title} by {self.author}"

  def __len__(self):
    return self.pages

  def __del__(self):
    print('A book object has been deleted.')

b = Book('Python rocks', 'Jose', 20)

print(b)
print(str(b))
print(len(b))
del b
#print(b) > get an error, not defined, without the method

"""
Dunder methods let you emulate the behavior of built-in types.
For example, to get the length of a string you can call len('string').
But an empty class definition doesn’t support this behavior out of the box.
To fix this, you can add a __len__ dunder method to your class.

__str__: The “informal” or nicely printable string representation of an object.
This is for the enduser.
"""
