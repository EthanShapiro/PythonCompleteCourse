from collections import defaultdict
# defaultdict is a dictionary like object that provides all methods from a dictionary
# it takes in a first argument
# it does not raise a key error, instead returns default value

d = {'k1': 1}
print(d['k1'])
# print(d['k2']) will return a key error because k2 is not a key
d = defaultdict(object)
print(d['one'])
for item in d:
    print(item)

d = defaultdict(lambda : 0)
print(d['one'])
print(d['two'])
