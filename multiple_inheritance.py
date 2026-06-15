"""class Flyable:
    def fly(self):
        print(f"{self.name} is flying !")

    def altitude(self):
        print(f"{self.name} is at cruising altitude.")


class Swimmable:
    def swim(self):
        print(f"{self.name} can swim!")

    def dive(self):
        print(f"{self.name} dives underwater.")

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name= name

    def quack(self):
        print(f"{self.name} says: Quack!")

d= Duck("Donald")
d.fly()
d.swim()     
d.quack()
d.altitude()
d.dive()         """

#MRO
class A:
    def hello(self):
        print("Hello from A")
class B(A):
    def hello(self):
        print("Hello from B")
class C(A):
    def hello(self):
        print("Hello from  C")
        
class D(B,C):
    pass

d= D()
d.hello()
print(D.__mro__)
