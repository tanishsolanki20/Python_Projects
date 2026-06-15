class Animal():
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def __str__(self):
        return f"{self.name} (age {self.name})"

"""class Dog(Animal):
    def __init__(self, name, age , breed):
        super() . __init__ (name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof !")

    def __str__(self):
        return f"{self.name} the {self.breed} (age {self.age})"
    

class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def meow(self):
        location = "indoor" if self.indoor else "outdoor"
        print(f"{self.name} ({location}) says: Meow !")

a = Animal("Generic Animal", 5)
d = Dog("Bruno", 3, "Golden Retriever")
c = Cat("Whiskers", 2, True)

d.eat()
d.sleep()
d.bark()

c.eat()
c.meow()

print(d)
print(c)

print (isinstance(d, Dog))
print (isinstance(d, Animal))
print (isinstance(c, Dog))"""

#WITHOUT super() -- repetitive and fragile
"""class Dog(Animal):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed"""

#WITH super() -- clean and correct
class Dog(Animal):
    def __init__(self, name, age, breed):
        super(). __init__(name, age)
        self.breed = breed