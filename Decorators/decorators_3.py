# Passing functions as arguments
def hello():
    return 'Hi Ethan!'

def other(func):
    print('Other code goes here!')
    print(func())

# other(hello)

def new_decorator(func):

    def wrap_func():
        print('Code here will be executed before the func')

        func()

        print('Code here will be executed after the func')

    return wrap_func

@new_decorator  # ues the @ symbol to use decorator
def func_needs_decorator():
    print('This function needs a decorator!')

# func_needs_decorator = new_decorator(func_needs_decorator) # use = and pass the function into the wrapper

func_needs_decorator()
