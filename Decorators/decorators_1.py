def func():
    s = 'this is a local'
    return locals()

s = 'this is a global variable'

print(func())
print(globals()['s'])

def hello(name='Ethan'):
    return "Hello " + name

print(hello())

greet = hello

del hello
print(greet)
print(greet())