from collections import Counter
# Counter
# Dictionary subclass which helps count hashable objects
l = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 24, 4, 4, 4, 5, 5, 5]
print(Counter(l))   # Counts number of elements in a list

s = 'abasddsavasdnvnmsdnmfmasndfmmnsadf'
print(Counter(s))

s = 'how many times does each word show show up up how how'
words = s.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(2))

list_pairs = [('how', 3), ('banana', 5)]

print(sum(c.values()))      # total of all counts
c.clear()                   # resets all counts
print(list(c))              # list unique elements
set(c)                      # convert to a set
dict(c)                     # convert to a regular dictionary
print(c.items())            # convert to a list of (elem, cnt) pairs
Counter(dict(list_pairs))   # convert from a list of (elem, cnt) pairs
c.most_common()[:-10-1:-1]  # 10 least common elements
c += Counter()              # remove zero and negative counts
