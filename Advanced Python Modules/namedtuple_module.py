from collections import namedtuple
t = (1, 2, 3)
print(t[0])


Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='lab', name='Sammy')
print(sam.age)
print(sam.name)
