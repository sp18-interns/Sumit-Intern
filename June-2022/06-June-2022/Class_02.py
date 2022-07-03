import math

class Point2d(object):
    def __init__( self, x0, y0 ):
        self.x = x0
        self.y = y0

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dist(self, o):
        return math.sqrt( (self.x-o.x)**2 + (self.y-o.y)**2 )

p = Point2d(0,4)
q = Point2d(5,10)
leng = q.magnitude()
print("Magnitude {:.2f}".format( leng ))
print("Distance is {:.2f}".format( p.dist(q)))