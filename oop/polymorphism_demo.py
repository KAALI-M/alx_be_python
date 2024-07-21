import math
class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width=width

    def area(self): 
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius =radius
    def area(self):
        return math.pi*(self.radius** 2)
    
rec=Rectangle(100,100)
cir=Circle(100)
print (f" rectangle {rec.area()}, circle {cir.area()}")
