sentence = "Print only the words that start with an s in this sentence"
st = "Print every word in this sentence that has an even number of letters"
print([word for word in sentence.split() if word[0] == 's'])

print([x for x in range(11) if x % 2 == 0])

print([x for x in range(51) if x % 3 == 0])

print([word for word in st.split() if len(word) % 2 == 0])

stuff = []
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        stuff.append("FizzBuzz")
    elif x % 3 == 0:
        stuff.append("Fizz")
    elif x % 3 == 0:
        stuff.append("Buzz")
    else:
        stuff.append(x)
print(stuff)

st = "Create a list of the first letters of every word in this string"
print([letter[0] for letter in st.split()])