class Sample(object):
    pass


class Dog(object):

    # Class Object Attributes
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

x = Sample()    # x is an instance of the Sample class or an object
print(type(x))

kona = Dog("Snauzcher", "Kona")
print(kona.breed)   # breed is an attribute, so you don't put parentheses
print(kona.species) # species is a class object attribute, so every dog instance is a mammal
