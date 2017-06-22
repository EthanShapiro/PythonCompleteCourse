print("This is a string")
s = 'String'
print("Place my variable here: %s" %(s))
x = 123
print("Place my variable here: %s" %(x))

print("Floating point number: %1.2f" %(13.145))
print("Floating point number %10.2f" %(13.1423))

print("Convert to string %s" %(123)) # uses str()
print("Convert to string %r" %(123)) # Uses repr()

print("First %s, Second %s, Third %s" %("Hi", 'two', 1234))
print("First: {x}, Second: {x}".format(x=1))
print("First: {x}, Second: {y}, Third: {x}".format(x=1, y="two!"))
