"""Easy
1. Write a function cube(number) that returns the number multiplied by itself three times.
2. Write a function print_separator() that prints a line of 20 dashes (--------------------). Call it between two other print statements to see it in use.

Medium
3. Write a function convert_celsius_to_fahrenheit(celsius) that returns the Fahrenheit equivalent (F = C * 9/5 + 32).
4. Write a function is_prime(number) that returns True or False depending on whether the number is prime. (Hint: a number is prime if nothing between 2 and itself-minus-1 divides evenly into it — use a loop and the % operator)

Hard
5 . Build a simple "unit converter" tool using three separate functions: km_to_miles(km), kg_to_pounds(kg), and celsius_to_fahrenheit(c). Then write a small menu using input() and if/elif that asks the user which conversion they want, takes a number, calls the right function, and prints the result."""

#1
"""def cube(number):
    return number*number*number
print(cube(3))"""

#2
"""def print_separator(a):
    return a
print(print_separator("--------------------"))
print("HI")
print(print_separator("--------------------"))"""

#3
"""def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
print(celsius_to_fahrenheit(32))"""

#4
"""def is_prime(number):
    if number < 2:
        return False
    
    
    for i in range(2, number):
        if number % i == 0:
            return False  
    
    return True  
print(is_prime(45))
print(is_prime(23))"""

#5
def km_to_miles(km):
    return km * 0.621371

def kg_to_pounds(kg):
    return kg * 2.2046

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

z = input("Enter the conversion (km to miles|kg to pounds|celsius to fahrenheit): ")

if z == "km to miles":
    value = float(input("Enter km: "))
    print(km_to_miles(value))
elif z == "kg to pounds":
    value = float(input("Enter kg: "))
    print(kg_to_pounds(value))
elif z == "celsius to fahrenheit":
    value = float(input("Enter celsius: "))
    print(celsius_to_fahrenheit(value))
else:
    print("Invalid option")