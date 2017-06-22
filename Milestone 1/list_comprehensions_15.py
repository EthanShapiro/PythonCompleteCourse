l = []
for letter in "word":
    l.append(letter)

print(l)
l = []
l = [letter for letter in "word"]
print(l)

lst = [x**2 for x in range(0,11)]
print(lst)

lst = [number for number in range(11) if number % 2 == 0]
print(lst)

celsius = [0,10,20.1,34.5]
farenheit = [(temp * (9/5) + 32) for temp in celsius]
print(farenheit)

lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)
