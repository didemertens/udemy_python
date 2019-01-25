class Dog():

  def __init__(self,name):
    self.name = name

  def speak(self):
    return self.name + ' says woof!'

class Cat():

  def __init__(self,name):
    self.name = name

  def speak(self):
    return self.name + ' says meow!'

niko = Dog('Niko')
felix = Cat('Felix')

#print(niko.speak())
#print(felix.speak())

'''
for pet in [niko,felix]:
  print(type(pet))
  print(pet.speak())
> do this with a function
'''

def pet_speak(pet):
  print(pet.speak())

#print(felix.speak())

# Common to use abstract classes, base class

class Animal():

  def __init__(self,name):
    self.name = name

  def speak(self):
    raise NotImplementedError("Subclass must implement this abstract method")

# Expecting you to inherit, use it as a base (don't need the init anymore in Dog class)
# Want the classes to share the same method name 'speak' (or for example, 'open' for files)

class Dog(Animal):

  def speak(self):
    return self.name + ' says woof!'

fido = Dog('Fido')
print(fido.speak())
