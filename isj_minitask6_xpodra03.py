# minitask 6
class Point():
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __sub__(point1, point2):
        return Point(point1.x - point2.x, point1.y - point2.y)
        
    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)        
        
p0 = Point()
p1 = Point(3, 4)
print(p0-p1)
p2 = Point(1, 2)
result = p1-p2
print(result)
print(p1 == p2)