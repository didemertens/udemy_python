s = set()
s.add(1)
s.add(2)
#sets don't take duplicate items

s.clear()

s = {1,2,3}
sc = s.copy()
s.add(4)

s.difference(sc)
# shows the difference between s and sc

s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)
# returns the first set without the element that isn't in set2

# if it isn't in the set, does nothing otherwise removes it
s1.discard(12)

s1 = {1,2,3}
s2 = {1,2,4}

s1.intersection(s2)
# common in both of the sets

s1.intersection_update(s2)
# first set with just the common elements

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

s1.isdisjoint(s2)
# they do have something in common so it's False
s1.isdisjoint(s3)
# is true, have a null intersection

s1.issubset(s2)
# is it a part of set2 and other way around:
s2.issuperset(s1)



