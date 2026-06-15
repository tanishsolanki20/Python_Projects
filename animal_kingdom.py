"""class Animal:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def eat(self):
        print(f"{self.name} is eating .")

    def speak(self):
        print(f"{self.name} makes a sound .")

    def __str__ (self):
        return f"{self.name} (age {self.age})"
    
class Lion(Animal):
        def __init__(self, name, age, main_colour):
            super().__init__ (name, age)
            self.main_colour = main_colour

        def speak(self):
            print(f"{self.name} roars .")

        def hunt(self):
            print(f"{self.name} hunts .")

class Parrot(Animal):
        def __init__(self, name, age, phrase):
            self.name= name
            self.age= age
            self.phrase= phrase

        def speak(self):
            print(f"{self.name} says {self.phrase} .")

        def fly(self):
            print("{self.name} is flying .")

class Elephant(Animal):
        def __init__(self, name, age, weight_KG):
            self.name= name
            self.age= age
            self.weight_KG= weight_KG

        def speak(self):
            print(f"{self.name} trumpets .")

        def memory_fact(self):
            print(f"{self.name} remembers evrything .")

lion= Lion("Leo", 7, "Orange")
parrot= Parrot("Polly", 4, " 'I like green chillies.' ")
elephant= Elephant("Dumbo", 6, "200")

zoo=[lion, parrot, elephant]
for animal in zoo:
     print(animal)
     animal.speak()
     animal.eat()
    """
