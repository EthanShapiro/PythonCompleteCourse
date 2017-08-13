from functools import reduce
# Problem 1
# Use map to get the length of each word in the sentence
sentence = "How long are the words in this phrase"
print(list(map(len, sentence.split())))

# Problem 2
# Use reduce to take a list of digits and return the number they correspond to
digits = [3, 4, 3, 2, 1]

def digitsToNum(digits):
    return reduce(lambda x, y: x*10 + y, digits)
print(digitsToNum(digits))

# Problem 3
# Use filter to return the words from a list of words which start with a letter
l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']

def filterWords(wordList, letter):
    return list(filter(lambda x: x[0] == letter, wordList))
print(filterWords(l, 'h'))


# Problem 4
# Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2
# concatenated together with connector between them. Look at the example output below:
def concatenate(L1, L2, connector):
    return [word1 + connector + word2 for (word1, word2) in zip(L1, L2)]
print(concatenate(['A', 'B'], ['a', 'b'], '-'))

# Problem 5
# enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value
# You may assume that a value will only appear once in the given list.

def dList(L):
    return {key: value for value, key in enumerate(L)}

print(dList(['a', 'b', 'c']))

# Problem 6
# enumerate and other skills from above to return the count of the number of items in the list value equals its index
def countMatchIndex(L):
    return len([num for count, num in enumerate(L) if num == count])

print(countMatchIndex([0, 2, 2, 1, 5, 5, 6, 10]))