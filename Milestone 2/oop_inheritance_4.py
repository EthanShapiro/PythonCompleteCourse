# Inheritance is a way to form new classes from classes already defined
# Newly formed classes are called derived classes, and the classes derived from are called base classes

class Animal(object):

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self);
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof")

a = Animal()
d = Dog()
d.whoAmI()  # Overrides the base classes method whoAmI
d.eat()     # can call methods in the base class
d.bark()    # Can have it's own classes
