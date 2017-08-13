# takes in a function that returns true or false and returns items that return true in a iterable

def evenCheck(num):
    return num % 2 == 0

evenNums = list(filter(evenCheck, [1, 2, 3, 4, 5, 6]))
print(evenNums)

evenNums = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(evenNums)