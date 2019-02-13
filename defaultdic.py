from collections import defaultdict

# Never raises a key value, returns default

d = defaultdict(object)
print(d['one'])

for item in d:
  print(item)
  # prints 'one'

d = defaultdict(lambda : 0)
# Always returns zero

print(d['one'])
d['two']
print(d)

# Prints: {'one': 0, 'two': 0})
