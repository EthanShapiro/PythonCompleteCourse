try:    # Executes code that can potentially have an error
    2 + 's'
except TypeError:   # If a specific error occurred
    print("There was a type error")
except: # If any exception occurred
    print("There was an exception!")
finally:
    print("Finally this was printed")

try:
    f = open("testfile1232", 'r')
    f.write("write this")
except:
    print("Error writing to the file!")
else:
    print("File write was a success")
finally:
    print("always execute finally code blocks")

def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except ValueError:
            print("That was not an integer!")
            continue
        else:
            print("Correct input was inputted!")
            break
        finally:
            print("We got here finally!")
    print(val)

askint()