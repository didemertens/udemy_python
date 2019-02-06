'''
def func():
  return 1

def hello():
  return "Hello!"

greet = hello
print(greet())
# even if you delete the name hello afterwards, still points to that function

def hello(name="Roan"):
  print('Hello() function executed')

  def greet():
    return "\t This is  the greet() func inside hello!"

  def welcome():
    return "\t This is the welcome() inside hello"
  print(greet())
  print(welcome())
  print("This is the end of the hello function")

hello()
'''

# To access the greet/welcome outside of the hello function:


def hello(name="Roan"):
  print('Hello() function executed')

  def greet():
    return "\t This is  the greet() func inside hello!"

  def welcome():
    return "\t This is the welcome() inside hello"
  if name == 'Roan':
    return greet
  else:
    return welcome

#my_new_func = hello('Roan')
#print(my_new_func())

def hello():
  return 'Hi Roan!'

def other(some_def_func):
  print('Other code runs here!')
  print(some_def_func())
# Pass the raw function into the other function
#other(hello)


def new_decorator(original_func):
# Extra functionality in the function before original
# Decorator, because you wrap the function
  def wrap_func():
    print("Some extra code before original")

    original_func()

    print("Some extra code after original")

  return wrap_func

def func_needs_decorator():
  print("I want to be decorated!")

#decorated_func = new_decorator(func_needs_decorator)
#decorated_func()


# Special syntax for line 71

# TO CREATE NEW DECORATOR:

@new_decorator
def func_needs_decorator():
  print("I want to be decorated!")

func_needs_decorator()





