from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name= name
        self.age= age

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass
    
    def eat(self):
        print(f"{self.name} is eating.")

    def __str__(self):
        return f"{self.name} (age{self.age})"

    #Try 1: create a bare animal - should fail
    # a = Animal("Generic", 5)

    #Try 2: child that forgets speak() - should fail
class Fish(Animal):
        def move(self):
            print(f"{self.name} swims.")
            #forgot speak() 

        
    #f = Fish("Nemo", 2)
class Dog(Animal):
        def __init__(self, name, age, breed):
            super(). __init__(name, age)
            self.breed= breed

        def speak(self):
             print(f"{self.name} barks!")

        def move(self):
             print(f"{self.name} runs on four legs.")

        def __str__(self):
             print(f"{self.name} the {self.breed} (age{self.age})")

class Bird(Animal):
     def __init__(self, name, age, can_fly):
          super(). __init__(name, age)
          self.can_fly= can_fly

     def speak(self):
        print(f"{self.name} chirps.")

     def move(self):
          if self.can_fly:
               print(f"{self.name} flies through the air.")
          else:
               print(f"{self.name} waddles along the ground.")

class Snake(Animal):
     def speak(self):
          print(f"{self.name} hisses!")

     def move(self):
        print(f"{self.name} slithers.")

d= Dog("Cookie", 3, "Shitzu")
b= Bird("Tweety", 2, True)
s= Snake("Slurpy", 4)

animals = [d, b , s]
for animal in animals:
     print(Animal)
     animal.speak()
     animal.move()
     animal.eat() #inherited, not abstract
     print()
     

