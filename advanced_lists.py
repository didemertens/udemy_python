l = [1,2,3]

l.append(4)

l.count(2)

x = [1,2,3]
x.append([4,5])
# appends the entire element to the list, list in a list
# if you want to add to the list, use extend
x.extend([4,5])

l.index(2)

# two arguments: index, object
l.insert(2,'inserted')

ele = l.pop()
# pop always last element, but can add index

l.remove('inserted')
# removes only the first occurance of a value

l.reverse()
l.sort()
