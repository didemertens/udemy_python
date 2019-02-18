t = (1,2,3)

print(t[0])

# sometimes hard to remember index

from collections import namedtuple

# quickly creating a class, creating new object type
Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='lab', name='Sammy')
print(sam)
print(sam.age)
print(sam[1])


