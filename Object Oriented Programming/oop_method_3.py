class Circle(object):

    # Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.perimeter = Circle.pi * (radius * 2)

    def area(self):
        # pi multiplied by radius**2
        return Circle.pi * (self.radius**2)

    def setRadius(self, newRadius):
        """
        This method takes in a radius, and sets the current radius of the Circle
        :param newRadius:
        :return:
        """
        self.radius = newRadius

    def getRadius(self):
        return self.radius

    def getPerimeter(self):
        """
        Returns the perimeter of the current Circle
        :return:
        """
        return Circle.pi * (self.radius * 2)

c = Circle(20)
print(c.area())
c.setRadius(4)
print(c.getRadius())
