myList = [1,2,3] # List of integers
print(myList)

myList = ['string', 23, 1.2, 'a'] # Tuple
print(myList)

print(len(myList)) # Can get the length of a list

myList = ["one", 'two', "three", 4, 5]
print(myList[0])

print(myList[1:]) # get everything after element 1
print(myList[:4]) # Everything up to element 4
print(myList[::-1]) # print backwards
print(myList[:-1]) # Get Last item

myList = myList + ["this is new", "Also new"] # add lists together
print(myList)

print(myList * 2) # Duplicate elements in list

l = [1, 2 ,3]
print(l)
l.append(4) # adds element to the end
print(l)
x = l.pop() # removes and returns element at the end
print(x)
# l[99] will result in an 'index out of range' error because there is no item at index 99

newList =  ['a', 'h', 'x', 'd', 'e']
print(newList.reverse())
print(newList.sort())

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
matrix = [list1,list2,list3] # create nested lists (list of lists)
print(matrix)
print(matrix[0]) # Returns first item in matrix
print(matrix[1][0]) # Returns first element in the second list in the matrix

firstCol = [row[0] for row in matrix] # flat for loop to go through each element
print(firstCol) # Gets the first element in each matrix list