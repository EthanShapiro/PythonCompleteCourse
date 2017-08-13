s = set()

s.add(1)
s.add(2)
print(s)

print(s.clear())

s = {1, 2, 3}
sc = s.copy()
print(s)
print(sc)
sc.add(1)

set1 = {1, 2, 3}
set2 = {1, 5, 6}
print(set1.difference(set2))

set1.discard(1)
print(set1)

print(set1.intersection({1, 3, 7}))

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
