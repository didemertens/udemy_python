s = 'hello world'

s.capitalize()
s.upper()
s.count('e')
s.find('o')

s = 'hello hello'

# check if they are all alph. characters
print(s.isalpha())

s.islower()
s.isupper()
s.isspace()
# is false because not all characters are whitespace

s.endswith('o')

s.split('e')

# Returns separator itself as well, and then everything else after it
s.partition('e')
