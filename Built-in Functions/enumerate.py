# enumerate allows you to keep a count as you iterate through an object
# it does this by returning a tuple in the form (count, element)
l = ['a', 'b', 'c']
count = 0
for item in l:
    print(count)
    print(item)
    count += 1

for count, item in enumerate(l):
    if count >= 2:
        break
    else:
        print(item)
