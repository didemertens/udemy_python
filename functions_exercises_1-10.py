def myfunc():
    print('Hello World')

def myfunc(Name):
    print('Hello {}'.format(Name))

def myfunc(s):
    if s == True:
        return 'Hello'
    if s == False:
        return 'Goodbye'

def myfunc(x, y, z):
    if z == True:
        return x
    if z == False:
        return y

def myfunc(a, b):
    return a+b

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def is_greater(a, b):
    if a > b:
        return True
    else:
        return False

"""
def myfunc(*args):
  return sum(args) > no limit to input, arbitrary number of arguments
  doesn't have to be 'args', it's about the asterix but convention is args

**kwargs = keyword arguments. kwargs returns a dictionary
def myfunc(**kwargs):
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs[fruit]))
  else:
    print('No fruit.')
myfunc(fruit='apple', veggie='lettuce')

def myfunc(*args, **kwargs):
  print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc(10,20,30,fruit='orange', food='eggs', animal='dog')
"""

def myfunc(*args):
    return sum(args)

def myfunc(*args):
    my_list = []
    for n in args:
        if n % 2 == 0:
            my_list.append(n)
    return my_list

def myfunc(string):
    new_string = ''
    index = 0
    for letter in string:
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        index += 1
    return new_string


