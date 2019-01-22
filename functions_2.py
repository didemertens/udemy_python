def dog_check(mystring):
  return 'dog' in mystring.lower()

#'dog' in mystring.lower() is already a boolean

#print(dog_check('My dog is in the garden.'))

def pig_latin(word):
  vowels = ['a', 'e', 'i', 'o', 'u']
  first_letter = word[0]
  # check if first_letter is a vowel
  if first_letter in vowels:
    pig_word = word + 'ay'
  else:
    pig_word = word[1:] + first_letter + 'ay'
  return pig_word

print(pig_latin('word'))
