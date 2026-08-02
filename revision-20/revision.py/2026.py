"""coordinates=(342, 564)
rgb=(255, 0, 0)
print(coordinates[0])
for i in rgb:
    print(i)

x,y= coordinates
print(x, y)"""

"""def values(numbers):
    return min(numbers), max(numbers)
print(values([1, 2, 3, 4, 5]))
low, high = values([1, 2, 3, 4, 5])
print(low, high)"""

"""student_ids={3454627, 3454628, 3454629}
student_ids.add(3454630)
student_ids.add(3454627)
print(student_ids)
print(3454627 in student_ids)"""
"""
x= [96, 100, 88]
set_x= set(x)
print(set_x)"""
"""
maths_class= {"John", "Mary", "Peter"}
science_class= {"Mary", "rahul", "David"}
print(maths_class.intersection(science_class))
print(maths_class.union(science_class))
print(maths_class.difference(science_class))"""
"""
x= "                Tanish"
print(x.upper())
email= x.strip().lower()
print(email)"""

"""x= "t3nish"
x= alphanumeric= x.isalnum()
print(x)
print("hello".startswith("t"))
print("hello".endswith("o"))
print("hello".isdigit())"""

"""print("cat" in "the cat sat on the mat")

text= "the cat sat on the mat"
print(text.count("at"))
print(text.find("cat"))
sentence= "the cat sat on the mat"
words= sentence.split()
print(len(words))"""

#Write a class rectangle with attributes width and height and methods area() and peimeter().
"""class Rectangle:
    def __init__ (self,width,height):
        self.width= width
        self.height= height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)

rec1= Rectangle(3,5)

print(rec1.area())
print(rec1.perimeter())"""

#Write a class "Student" attributes name and marks where marks is a list. Add a method "Average" that returns the average marks a method "Highest" that returns the highest marks.
"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def highest(self):
        return max(self.marks)


# Example usage
s = Student("Alice", [85, 90, 78, 92])
print(f"Average: {s.average()}")
print(f"Highest: {s.highest()}")"""

"""class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Amount deposited: {amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Amount withdrawn: {amount}"

    def get_balance(self):
        return f"Balance: {self.balance}


obj1 = BankAccount()

print(f"deposit: {obj1.deposit(1232341)}")
print(f"withdraw: {obj1.withdraw(344)}")
print(f"balance: {obj1.get_balance()}")"""

#Write a function tht takes a list of numbers and returns a new list containing only even numbers.
"""even_numbers=[]
def return_even_numbers(numbers):
    for i in numbers:
        if i%2==0:
            even_numbers.append(i)
    return even_numbers
print(return_even_numbers([3,7,56,33]))"""

