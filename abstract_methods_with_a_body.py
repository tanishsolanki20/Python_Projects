from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self,colour):
        self.colour= colour

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def describe(self):
        print(f"I am a {self.colour} shape.")

class Circle(Shape):
    def __init__ (self, colour, radius):
        super(). __init__(colour)
        self.radius = radius

    def area(self):
        import math
        return round(math.pi* self.radius ** 2, 2)
    
    def describe(self):
        super().describe()

        print(f"I am a circle with radius {self.radius} and area {self.area()}")

c = Circle("red", 5)
c.describe()