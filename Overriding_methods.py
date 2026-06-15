class Animal:
    def __init__(self, name, age, color):  # ← THIS WAS MISSING
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

class Fish(Animal):
    pass

animals = [Dog("Rex", 3, ""), Cat("Luna", 2, True), Fish("Nemo", 1,"blue")]
for a in animals:
    a.speak()