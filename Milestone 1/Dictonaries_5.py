# Dictionaries are data structures that are not ordered, and use key value pairs
# To define a dictionary see below.
myDict = {"Key1": "Value1"}

# Access A value by using a key
print(myDict["Key1"])

# Values don't have to be the same type
myDict = {"k1": 123, "k2": 2.4, "k3": "string"}
print(myDict["k1"] - 120)   # doesn't effect value permanently
myDict["k1"] = myDict["k1"] - 120   # Changes the value of k1

print(myDict["k1"])
myDict["k1"] = 123

myDict["k1"] -= 120     # Same thing as myDict["k1"] = myDict["k1"] - 120
# NOTE you can do -= += /= and *=

d = dict()  # Another way to create a dictionary
d['animal'] = "dog"     # Add new key and value
d['answer'] = 42
print(d)

# You can create nested dictionaries
d = {"k1": {"nestkey": {"subnestkey": "value"}}}
print(d)
print(d["k1"]["nestkey"]['subnestkey']) # will print 'value'
# NOTE you don't want to have too many nested dictionaries because you can forgot where things are

d = {}
d["k1"] = 1
d["k2"] = 2
d["k3"] = 3

print(d.keys())  # Returns all keys unordered
print(d.values())    # Returns all values unordered
print(d.items())    # Returns a tuple of all keys and values
