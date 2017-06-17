# Scope can be described by 3 general rules
#   Name assignments will create or change local names by default.
#   Name references search (at most) four scopes, these are(LEGB):
#       local
#       enclosing functions
#       global
#       built-in
#   Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.

# Global variables are not affected within a function using its' own local variable of the same nam
x = 25
def printer():
    x = 50
    print(x)

print(x)    # Will return 25
printer()   # Will return 50

# hello procedure can access the variable name because it is enclosed in greet
name = "this is a global name"

def greet():
    name = "Ethan"

    def hello():
        print("Hello " + name)

greet()

# Global variables can be edited in a function or procedure using the keyword global

x = 50

def proc():
    global x
    print("Global x is currently {0}".format(x))
    x = 2
    print("Changed global x to {0}".format(x))

proc()
print("Now global x is {0}".format(x))

# Built in functions are non overwritable

print(len)
