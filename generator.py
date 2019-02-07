def create_cubes(n):
  for x in range(n):
    yield x**3

'''
for x in create_cubes(10):
  print(x)
print(list(create_cubes(10)))
'''

def simple_gen():
  for x in range(3):
    yield x

for number in simple_gen():
  print(number)

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

s = 'hello'
iter_s = iter(s)
print(next(iter_s))

