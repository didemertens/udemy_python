def lesser_of_two_evens(a,b):
  if (a % 2 == 0) and (b % 2 == 0):
    return min(a,b)
  else:
    return max(a,b)

#print(lesser_of_two_evens(2,5))

def animal_crackers(text):
  words = text.split()
  letter_1 = words[0][0]
  letter_2 = words[1][0]
  return letter_1 == letter_2

#print(animal_crackers('Levelheaded Llama'))

def makes_twenty(n1, n2):
  return (n1+n2 == 20) or (n1 == 20 or n2 == 20)

#print(makes_twenty(2,3))

def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

#print(old_macdonald('macdonald'))

def master_yoda(text):
  words = text.split()
  words.reverse()
  new_text = " ".join(words)
  return new_text

#print(master_yoda('I am home'))

def almost_there(n):
  return n in range(90,111) or n in range(190, 211)

#print(almost_there(209))

def has_33(nums):
  for index, number in enumerate(nums):
    if number == 3 and nums[index+1] == 3:
      return True
  return False

#print(has_33([3, 4, 3, 4, 2, 3, 3]))

def paper_doll(text):
  new_text = ''
  for letter in text:
    new_text += letter * 3
  return new_text

#print(paper_doll('Hello'))

def blackjack(a,b,c):
  if sum((a,b,c)) <= 21:
    return sum((a,b,c))
  elif sum((a,b,c)) < 31 and 11 in (a,b,c):
    return (sum((a,b,c)) - 10)
  else:
    return 'BUST'

#print(blackjack(9,9,2))

def summer_69(arr):
  total_sum = 0
  skipping = False
  for number in arr:
    if number == 6:
      skipping = True
    if skipping == False:
      total_sum += number
    if skipping == True and number == 9:
      skipping = False
  return total_sum


#print(summer_69([4,5,6,7,8,9]))
#print(summer_69([2, 1, 6, 9, 11]))

def spy_game(nums):
  for index, number in enumerate(nums):
    if number == 0 and nums[index+1] == 0 and nums[index+2] ==7:
      return True
  return False

#print(spy_game([1,2,4,0,0,3,7,8,5]))

def count_primes(num):
  total_prime = 0
  x = 3
  while x <= num:
    for number in range(3,x):
      if x % number == 0:
        x += 1
        break
    else:
      total_prime += 1
      x += 1
  return total_prime

#print(count_primes(100))


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',
    7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A' : [1,2,4,3,3], 'B': [5,3,5,3,5]}
    for pattern in alphabet[letter.upper()]:
      print(patterns[pattern])

#print(print_big('b'))



