"""Guided Practice

Exercise 1:
Create a Car class with attributes make, model, and year. Add a method describe() that prints "2022 Toyota Corolla" style output. Create two different car objects and call describe() on each.
(Hint: __init__ takes self, make, model, year — the method just prints them together)

Exercise 2:
Create a BankAccount class with owner and _balance. Add deposit(amount), withdraw(amount), and get_balance() methods. Test it by depositing ₹500, withdrawing ₹200, and printing the final balance.
(Hint: refer to Example 4 — try writing it from memory before checking)

Exercise 3:
Create a parent class Person with name and age. Create two child classes — Teacher (adds subject) and Student (adds grade). Both should inherit describe() from Person, but each should also have its own role() method that prints something like "Teacher of Mathematics" or "Student in 9th grade".
(Hint: use super().__init__(name, age) in each child class)

Exercise 4:
Create a Library class that stores a list of books. Add methods: add_book(title), remove_book(title), and list_books(). Create a library, add 3 books, remove one, and list the remaining.
(Hint: self.books = [] in __init__ — then use .append() and .remove())"""

#1
"""class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def describe(self):
        return f"{self.make} {self.model} was made in {self.year}."

    def describe(self):
        return f"{self.make} {self.model} was made in {self.year}."

car1=Car("Mahindra", "XUV700", "2023")
car2=Car("Toyota", "Corolla", "2022")
print(car1.describe())
print(car2.describe())"""

#2
"""class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance

    def deposit(self, amount):
        if amount > 0:
            self._balance+=amount
            print("Amount deposited !", self._balance)
        else:
            print("Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("You do not have this much money!")
        else:
            self._balance-=amount
            print("Amount withdrawed !", self._balance)

    def get_balance(self):
        return self._balance


d=BankAccount("tanish",10000)
print(d.deposit(500))
print(d.withdraw(10))
print(d.get_balance())"""

#3
"""class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def describe(self):
        print(f"I am {self.name} and I am {self.age} years old.")

class Teacher(Person):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def adds_subject(self):
        print(f"{self.name} added a subject !")

class Student(Person):
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def adds_grade(self):
        print(f"{self.name} added a grade ! ")

teacher=Teacher("Khushi", 21)
student=Student("Tanish", 13)
teacher.describe()
student.describe()
teacher.adds_subject()
student.adds_grade()"""

#4
"""class Library:
    def __init__(self):
        self.books = []          # each instance gets its own list

    def add_book(self, title):
        if title in self.books:
            print(f"'{title}' is already in the library.")
        else:
            self.books.append(title)

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
        else:
            print(f"'{title}' was not found in the library.")

    def list_books(self):
        return list(self.books)  # return a copy so callers can't alter the internal list


# Usage
library = Library()
library.add_book("The Wizard of Oz")
library.add_book("Dune")
print(library.list_books())      # ['The Wizard of Oz', 'Dune']

library.remove_book("The Wizard of Oz")
print(library.list_books())      # ['Dune']

library.remove_book("Missing Book")  # prints a friendly message instead of crashing"""