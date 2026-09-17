class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed=breed

    def describe(self):
        print(self.name+" is a " + self.breed)

d=Dog("Cookie", 2, "Shitzu")
d.describe()
print(d.age)