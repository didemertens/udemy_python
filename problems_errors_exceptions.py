# Problem 1
try:
  for i in ['a', 'b', 'c']:
    print(i**2)
except TypeError:
  print('There was a type error.')

# Problem 2
try:
  x = 5
  y = 0
  z = x/y
except:
  print('Error!')
finally:
  print('All done')

# Problem 3

def ask_square():
  while True:
    try:
      number = int(input('Enter a number: '))
    except ValueError:
      print('Please enter a number, not something else.')
      continue
    else:
      square = number * number
      print(f'Thank you! Your number squared is: {square}')
      break

ask_square()
