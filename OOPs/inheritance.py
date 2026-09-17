class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def describe(self):
        print(self.name+"is"+str( self.age ) + " years old.")

class Dog(Animal):
    def speak(self):
        print(self.name+"says:Woof!")

class Cat(Animal):
    def speak(self):
        print(self.name+"says:Meow!")

dog=Dog("Cookie", 2)
cat=Cat("Whiskers", 3)
dog.describe()
cat.describe()
