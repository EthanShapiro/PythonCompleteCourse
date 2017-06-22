import math

class Line(object):
    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        return math.sqrt((self.cord2[0] - self.cord1[0])**2 + (self.cord2[1] - self.cord1[1])**2)

    def slope(self):
        x = 0
        try:
          x = self.cord2[1] - self.cord1[1] / self.cord2[0] - self.cord1[0]
        except ZeroDivisionError:
            print("Slope is undefined")
            return 0
        finally:
            return x


class Cylinder(object):
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (math.pi * self.radius**2) * self.height

    def surface_area(self):
        c = 2*(math.pi * self.radius**2)
        r = (math.pi * (2*self.radius)) * self.height
        return r + c


l = Line((0, 0), (2, 4))
print(l.distance())
print(l.slope())

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
