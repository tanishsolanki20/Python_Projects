class Pets:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Dog(Pets):
    def bark(self):
        print(f"{self.name} barks!")

class Cat(Pets):
    def meow(self):
        print(f"{self.name} meows!")

