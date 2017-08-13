# Functions within Functions

def hello(name='Ethan'):

    def greet():
        return "\tThis is inside the greet() function"

    def welcome():
        return '\tthis is inside the welcome() function'

    print(greet())
    print(welcome())
    if name == 'Ethan': # Return the functions greet and welcome
        return greet
    else:
        return welcome

x = hello()
print(x())
# cannot call welcome() or greet() because it is not defined outside of hello
