# Counter
from collections import Counter

l = [1,2,2,1,1,1,1,3,4,4,4,4,3,3,3]
print(Counter(l))
s = 'aaassssssaaaavvvvv'
print(Counter(s))

s = 'How many times does each word show up in this sentence word word show up up'

words = s.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(2))
# Shows 2 most common words

print(list(c))
# Show only the unique elements



