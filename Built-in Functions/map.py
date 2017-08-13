# map is a function that takes a function and a sequence, that applies the function to every item in the sequence

def fahrenheit(T):
    return (9/5)*T + 32

temp = [0, 22.5, 40, 100]

print(list(map(fahrenheit, temp)))
print(list(map(lambda t: (9/5)*t + 32, temp)))

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(list(map(lambda x, y, z: x + y + z, a, b, c)))

negatives = list(map(lambda x: x * -1, a))
print(negatives)
