import os
print(os.getcwd())
print(os.listdir())
print(os.path.exists("datetime_module.py"))

#From x import y
from math import sqrt, pi, floor
print(sqrt(144))
print(pi)
print(floor(pi))

try:
    num= int(input("Enter a number: "))
    print(10/num)
#except ValueError:
 #   print("Error: Please enter a valid number")
#except ZeroDivisionError:
 #   print("Error: Cannot divide by zero")"""
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: Please enter a valid number. {e}")
a= 10
print(a)

def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Error: Please enter a valid number.")

age= get_number("Enter your age: ")
print("In 10 years you'll be", age + 10)