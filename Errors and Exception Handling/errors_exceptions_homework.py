# Problem 1
# handle the exception thrown using a try and except block
try:
    for i in ['a','b','c']:
        print (i**2)
except TypeError:
    print("You cannot square that object!")

# Problem 2
# handle the exception thrown using a try and except block and then use finally to print "All done"
x = 5
y = 0
try:
    x / y
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("All done!")

# Problem 3
# write a function that asks for an integer and prints the square of it
# use a while loop, try, except, else block to check for incorrect input
def squareNum():
    while True:
        try:
            num = int(input("Please input an integer: "))
        except ValueError:
            print("That isn't an integer!")
            continue
        else:
            print("The square of {0} is {1}".format(num, num**2))
            break

squareNum()