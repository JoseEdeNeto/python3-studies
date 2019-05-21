from math import sqrt

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'point : (%d, %d, %d)' % (self.x, self.y, self.z)

    def __add__(self, other):
        p3 = Point(self.x + other.x, self.y + other.y, self.z + other.z)
        return p3

    def distance(self, Point):
        return sqrt( (self.x-Point.x)**2 + (self.y-Point.y)**2 + (self.z-Point.z)**2 )

p1 = Point(1, 2, 3)
p2 = Point(2, 3, 4)
print(p1 + p2)