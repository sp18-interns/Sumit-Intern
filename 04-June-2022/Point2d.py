"""
Example of the Point2d class from Lectures 18 and 19.  It is important for Lab 9.
"""

import math

class Point2d(object):
    def __init__( self, x0=0, y0=0):
        self.x = x0
        self.y = y0

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dist(self, o):
        return math.sqrt( (self.x-o.x)**2 + (self.y-o.y)**2 )

    def __str__(self):
        s = "(%d,%d)" %(self.x,self.y)   # This assumes x and y are ints, and converts to ints if they are not
        return s

    def scale(self,n):
        self.x = self.x * n
        self.y *= n                      

    def __add__(self,o):
        new_x = self.x + o.x
        new_y = self.y + o.y
        return Point2d(new_x,new_y)   # created a new Point2d object

    def __sub__(self,o):
        return Point2d(self.x-o.x, self.y-o.y)

    def __mul__(self,s):
        return Point2d(self.x*s, self.y*s)

    def __eq__(self,o):
        return self.x == o.x and self.y == o.y

if __name__ == '__main__':
    p = Point2d(15,13)   
    d = p.magnitude()
    print ('Distance = %.2f' %d)
    q = Point2d(25)
    d = q.magnitude()
    print ('Distance = %.2f' %d)
    print "Distance between the points is %.2f" %p.dist(q)

    #  In the following, Python automatically converts str(p) to the method call p.__str__()
    print "As a string", str(p)
    p.scale(5)
    print "p is now", str(p)

    #  In the following line of code, Python automatically converts
    #     r = p+q
    #  to the method call
    #     r = p.__add__(q)
    r = p+q

    print "r = p+q yields r as", str(r)   # We could just use r.  Python figures it out automatically
    print "p-q =", p-q                    # Automatically calls __str__ on the Point2d object that results from p-q
    print "p*3 =", p*3

    z = Point2d(25,0)
    print "z == q", z==q                  #  The call z==q becomes z.__eq__(q)
    print "z == p", z==p                  #  The call z==p becomes z.__eq__(p)
