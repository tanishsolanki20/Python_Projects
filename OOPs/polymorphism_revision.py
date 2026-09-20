class Shape:
    def __init__(self, colour):
        self.colour=colour

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(self.colour)
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(self.colour)
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

class Triangle(Shape):
    def __init__(self, height, base):
        super().__init__(self.colour)
        self.height=height
        self.base=base
    def area(self):
        return 0.5*self.height*self.base

shapes=[Rectangle(4,2), Circle(5), Triangle(7, 5)]

for shape in shapes:
    shape.describe()


