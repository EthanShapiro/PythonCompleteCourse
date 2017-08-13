from functools import reduce

# reduces a list to a single value by combining elements via a supplied function
num = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(num)

lst = [34, 75, 23, 25, 100, 2003, 2, 11]
print(max(lst))
maxFind = lambda a, b: a if a > b else b
maxNum = reduce(maxFind, lst)
print(maxNum)
