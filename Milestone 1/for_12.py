l = [1,2,3,4,5,6,7,8]
t = [1, "Banana", 6.12]
d = {"one": 1, "two": 2, "three": 3}
s = "this is a string"

for item in l:
    if item % 2 == 0:
        print("{0} is an even number".format(item))
    else:
        print("{0} is an odd number".format(item))

for item in t:
    print(item)

for v,k in d.items():
    print(v,k)

for char in s:
    print(char)