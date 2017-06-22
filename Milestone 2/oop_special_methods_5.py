class Book(object):

    def __init__(self, title, author, numPages):
        print("A book has been created")
        self.title = title
        self.author = author
        self.numPages = numPages

    def __str__(self):
        return "Title: {0}, Author {1}, Pages: {2}".format(self.title, self.author, self.numPages)

    def __len__(self):
        return self.numPages

    def __del__(self):
        print("A book is gone!")

b = Book("python", "Ethan", 100)
print(b)
print(len(b))
del b
