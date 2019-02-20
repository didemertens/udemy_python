import re

# Write a program that matches a string that has an a followed by one or more b's

def text_match(text):
  patterns = 'ab+?'
  if re.search(patterns, text):
    return 'Found match!'
  else:
    return 'Not matched!'

#print(text_match('ac'))
#print(text_match('abb'))

# an a followed by 2 or 3 b's

def text_match(text):
  pattern = 'ab{2,3}'
  if re.search(pattern, text):
    return 'Found match!'
  else:
    return 'Not matched!'

# print(text_match('abbb'))
# print(text_match('abb'))
# print(text_match('ab'))

# an a followed by anything ending with b

def text_match(text):
  pattern = 'a.*b$'
  if re.search(pattern, text):
    return 'Found match!'
  else:
    return 'Not matched!'

# print(text_match('abbb'))
# print(text_match('abbc'))
