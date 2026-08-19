"""Guided Practice
1. Ask the user for their name and print `"Hello, [name]!"`
2. Ask the user for their name and city, then print:
[name] lives in [city].
3. Ask the user for their favorite color and food, then print both in one sentence.
4. Ask the user for two numbers and print their sum.
(Remember to convert with `int()`)*
5. Ask the user for their birth year and print their age (assume current year is 2026).
6. Ask the user for the length and breadth of a rectangle, then print its area.
7. Ask the user for a number and print its double and its square.
8. Ask the user for their age. If it's 18 or above, print `"You are an adult."` Otherwise print `"You are a minor."`
9. Ask the user for a number. Print `"Positive"`, `"Negative"`, or `"Zero"` depending on the value.
10. Ask the user for two numbers and print which one is larger.
11. Ask the user for their name, age, and city. Print a short paragraph combining all three.
12. Ask the user for the price of an item and print the price after adding 5% tax.":"""

#1
"""username=input("Enter your name: ")
print("Hello", username)"""

#2
"""name=input("enter your name: ")
city=input("enter your city: ")
print(f"{name} lives in {city}")"""

#3
"""color=input("What is your favorite color: ")
food=input("What is your favorite food: ")
print(f"Favorite color: {color}, Favorite food: {food}")"""

#4
"""a=int(input("Enter the fist number: "))
b=int(input("Enter the second number: "))
print(a+b)"""

#5
"""birthyear=int(input("Enter your birthyear: "))
print(2026-birthyear)"""

#6
"""length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
print(length*breadth)"""

#7
"""num=int(input("Enter a number: "))
print(num+num)
print(num*num)"""

#8
"""age=int(input("Enter your age: "))
if age>=18:
    print("You are an adult.")
else:
    print("You are a minor.")"""

#9
"""number=int(input("Enter a number: "))
if number==0:
    print("Zero")
elif number>0:
    print("Positive")
else:
    print("Negative")"""

#10
"""a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    print(a)
else:
    print(b)"""

#11
"""name=input("Enter your name: ")
age=int(input("Enter your age:  "))
city=input("Enter you city: ")
print(f"{name} is {age} years old and lives in {city}.")"""

#12 
"""price=int(input("Enter the price of the item: "))
print(f"Total price of the item(including taxes)={price+5/100}")"""
