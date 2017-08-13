# returns an iterator that takes elements from both iterators passed until the shortest iterator is exhausted
x = [1, 2, 3]
y = [4, 5, 6]
tple = tuple(zip(x, y))
print(tple)

a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]
for pair in zip(a, b):
    print (max(pair))

print(list(map(lambda pair: max(pair), zip(a, b))))
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]

print(tuple(zip(x,y)))
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print(tuple(zip(d1, d2)))

print(tuple(zip(d1.values(), d2)))

def switcharoo(d1,d2):
    dout = {}

    for d1key, d2val in zip(d1, d2.values()):
        dout[d1key] = d2val

    return dout

print(switcharoo(d1, d2))