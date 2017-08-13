import random

def gensquares(N):
    for x in range(N):
        yield x**2

for x in gensquares(10):
    print(x)


def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)

for x in rand_num(1, 10, 10):
    print(x)


s = 'hello'
print(iter(s))

# Generators a are used when you are dealing with a lot of data, they don't store values, they generate them on the fly
