t = (1,2,3)
print(len(t))   # Get Length of tuple
t = ('one', 2)
print(t[0])     # Indexing
print(t[-1])    # Supports slicing
print(t.index('one'))   # Return the index of an item in the tuple
t = (1,1,2,3)
print(t.count(1))   # Returns number of times something appears in the tuple

# Tuples are immutable
t = (1,2,3)
# t[1] = 4 will raise an error, because tuples do not support item assignment

# Tuples are useful when you don't want a sequence to be changed
