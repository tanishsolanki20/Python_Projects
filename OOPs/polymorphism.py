class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14159*self.radius**2

shapes=[Rectangle(4,5),Circle(3), Rectangle(2,8)]

for shape in shapes:
    print(shape.area())
    
