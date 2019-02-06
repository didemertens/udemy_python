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




