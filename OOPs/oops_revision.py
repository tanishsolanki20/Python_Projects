"""class Rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return f"Area: {self.length*self.breadth}"

area_of_rectangle=Rectangle(8,6)
print(area_of_rectangle.area())     """

"""class BankAccount:
    def __init__(self, balance):
        self._balance=balance

    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
            print(str(amount))
        else:
            ("Please enter a positive value!")

    def withdraw(self,amount):
        if amount>self._balance:
            print("You do not have that much money to withdraw!")
        else:
            self._balance-=amount
            print(amount)

    def get(self):
        return self._balance

account1=BankAccount(2000)
print(account1.deposit(10))
print(account1.get())
"""

"""class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

d=Dog("Cookie", 3)
c=Cat("Whiskers", 2)
d.describe()
c.describe()"""

class Car:
    def __init__(self, company, model):
        self.company=company
        self.model=model

    def describe(self):
        print(f"company: {self.company}, model: {self.model}")

class Electric_car:
    def __init__(self, battery_range):
        self.battery_range=battery_range
        print(f"battery_range: {battery_range}")



    
