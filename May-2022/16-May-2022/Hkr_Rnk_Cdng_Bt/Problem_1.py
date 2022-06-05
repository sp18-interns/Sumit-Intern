'''You are given four points A, B, c and D in a 3-dimensional Cartesian coordinate system. You are required to print the
angle between the plane made by the points A, B, C and B, C, D in degrees(not radians). Let the angle be PHI.
Cos(PHI) = (X*Y) / |X| |Y| where X = ABxBC and Y = BC x CD.
Input Format

One line of input containing the space separated floating number values of the  and  coordinates of a point.

Output Format x,y,z

Output the angle correct up to two decimal places.'''

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):

    def dot(self, no):

    def cross(self, no):

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':

