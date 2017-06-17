def myAdditionFunc(arg1, arg2):
    print(arg1 + arg2)

def addNum(num1, num2):
    return num1 + num2

def sayHello():
    print("Hello")

def greeting(name):
    print("Hello " + name)

def isPrime(num):
    """
    INPUT: A number
    OUTPUT: A print statement whether or not the a number is prime.
    """
    for n in range(2, num):
        if num % n == 0:
            print("Not prime")
            break
        else:
            print("The number is prime!")

myAdditionFunc(1, 2)
sayHello()
greeting("Jeff")
x = addNum(2, 5)
print(x)
