# Sets are an unordered collection of unique elements
x = set()
x.add(1)
print(x)
x.add(2)
print(x)
x.add(1)    # No change, sets have unique elements
print(x)

l = [1,1,1,2,2,2,2,3,3,4]
print(l)
print(set(l))   # Has only unique elements

# Booleans
# Pre defined true and false
a = True
print(a)    # Show s True
print(1 > 2)    # Output is a False
print(11 > 2)   # Output is True
b = None
print(b)    # Literally nothing
b = 'a'
print(b)    # Now is string a
