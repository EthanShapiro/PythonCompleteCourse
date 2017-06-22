import string
import math
from functools import reduce

def vol(rad):
    return (4/3) * math.pi * (rad**3)

print(vol(3))


def ranBool(num, low, high):
    return num in range(low, high+1)

print("the number is", ranBool(2, 0, 4))


sampleString = "Hello Mr. Rogers, how are you this fine Tuesday?"

def upLow(s):
    numUp = 0
    numLow = 0

    for c in s:
        if c in string.ascii_lowercase:
            numLow += 1
        elif c in string.ascii_uppercase:
            numUp += 1

    print(numUp)
    print(numLow)

upLow(sampleString)


l = [1,1,1,1,2,2,3,3,3,3,4,5]

def uniqList(l):
    return list(set(l))

print(uniqList(l))

def multiply(nums):
    return reduce(lambda x, y: x * y, nums)

print(multiply([1,2,3,4]))


def isPalindrome(s):
    return s.lower() == s.lower()[::-1]

print(isPalindrome("Helleh"))
print(isPalindrome("merk"))

panagram = "The quick brown fox jumps over the lazy dog"
def isPanagram(s):
    return "".join(sorted(set("".join(s.split()).lower()))) == string.ascii_lowercase

print(isPanagram(panagram))
print(isPanagram("this is not a pangaramasf"))
