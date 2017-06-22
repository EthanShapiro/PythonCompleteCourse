def square(num):
    result = num**2
    return result

def square1(num):
    return num**2

print(square(2))
print(square1(4))
square2 = lambda x: x**2
print(square2(3))

even = lambda num: num % 2 == 0
print(even(16))

first = lambda s: s[0]

print(first("Hello"))

rev = lambda s: s[::-1]
print(rev("hello"))

adder = lambda x,y: x+y
adder(30,30)

# Lambdas are very good in conjunction with these functions:
map()
filter()

# Usefull lambda tutorial https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/
