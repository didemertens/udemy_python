def add_numbers(n1,n2):
  return n1+n2

number1 = 10
#number2 = input('Enter a number: ')

# Nothing after an error is going to run, so add try block

try:
  # Attempt this code, may have an error
  result = 10 + 10
except:
  print('You are not adding correctly')
else:
  print('Add went well!')
  print(result)

# Regardless of an error, code always run: finally



