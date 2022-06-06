from math import sqrt


class Point2d:
    pass


p = Point2d()
p.x = 8
p.y = 8
dist_from_origin = sqrt(p.x**2 + p.y**2)
print(dist_from_origin)