# Strings are usually used to record text in a string
# Use "" or '' to specify a string
'Hello' # String
"Hello" # Still a string
# Double quotes should be used if you have a single quote in you string
# 'I'm  Will raise an error because python thinks you are trying to close the single quote

# Strings are a sequence it thinks of each character as an individual unit
# Output strings using print statements
print('String as a single thing')
print("String as a double thing")
print("This uses a new line\nTo break the print to multiple lines")
print("This is a tab \t here")

# get string length using len() function
print(len("Four"))

# you can use indexes to access certain parts of a string
s = "Hello World"
print(s)
# Indexing starts at 0
print(s[0]) # Returns the first element
# Slicing grabs everything from one point to another
print(s[1:4])

# Gets values 6-9 (up to 10)
print(s[6:10:2])

# go backwards
print(s[::-1])

# Get last letter
print(s[-1])

# everything but last index
print(s[:-1])

# Strings are IMMUTABLE
#   Immutability means that you can't change the value
#   That means you can't do s[0] = '0'

# You can add stuff to the end of a string
s = s + " I added this!"
print(s)

# You can also use arithmetic symbols on strings
letter = 'z'
letter = letter*10
print(letter)

# Use upper to change all letters to upper and lower
s = 'heLLo'
print(s.lower())
print(s.upper())

# Split a string
s = "Hello i am a string"
print(s.split()) # Splits by spaces
print(s.split('i')) # splits by specified value

# Strip a string
print(s.strip()) # strips all spaces at beginning and end
print(s.strip('H')) # strips all specified from beginning and end