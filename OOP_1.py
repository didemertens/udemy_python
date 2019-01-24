class Dog():

  # Class object attribute
  # Same for any instance of the class (so don't use self)
  species = 'mammal'

  def __init__(self,breed,name,spots):
    self.breed = breed
    self.name = name
    # Expect a boolean
    self.spots = spots

  def bark(self,number):
    print('Woof! My name is {} and I am {} years old.'.format(self.name, number))
    #print(f'My name is ' + self.name)

my_dog = Dog(breed='dalmation', name='Timmie', spots=True)

#print(type(my_dog))
#print(my_dog.breed) > call back info of the instance
#print(my_dog.species)
my_dog.bark(2)
