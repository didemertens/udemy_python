class Animal():

  def __init__(self):
    print('Animal created')

  def who_am_i(self):
    print('I am an animal')

  def eat(self):
    print('I am eating')

#myanimal = Animal()
#print(myanimal.eat())

class Dog(Animal):
  #Derived class

  def __init__(self):
    Animal.__init__(self)
    print('Dog created')

  def who_am_i(self):
    print('I am a dog')

  def bark(self):
    print('Woof!')

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()
