def vol(rad):
    pass

def ran_check(num,low,high):
  if num in range(low,high+1):
    print(f'{num} is in the range between {low} and {high}')
  else:
    print(f'{num} is not in the range between {low} and {high}')

#ran_check(5,2,7)

def ran_bool(num,low,high):
  return num in range(low,high+1)

#print(ran_bool(14,1,10))

def up_low(s):
  total_upper = 0
  total_lower = 0
  for letter in s:
    if letter.isupper():
      total_upper += 1
    elif letter.islower():
      total_lower += 1
    else:
      pass
  print(f'No. of upper case characters: {total_upper}')
  print(f'No. of lower case characters: {total_lower}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
#up_low(s)

def unique_list(lst):
  unique = []
  for number in lst:
    if number not in unique:
      unique.append(number)
  return unique

#print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(numbers):
  mlt = 1
  for number in numbers:
    mlt = mlt * number
  return mlt

#print(multiply([1,2,3,-4]))

def palindrome(s):
  space_string = s.replace(" ", "")
  return space_string == space_string[::-1]

print(palindrome('madam'))

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str_spaces = str1.replace(" ", "")
    unique_letters = []
    for letter in list(str_spaces):
      if letter not in unique_letters:
        unique_letters.append(letter.lower())
    return sorted(unique_letters) == list(string.ascii_lowercase)

#print(ispangram("The quick brown fox jumps over the lazy dog"))

def ispangram_b(str1, alphabet=string.ascii_lowercase):
  alphaset = set(alphabet)
  return alphabet <= set(str1.lower())
