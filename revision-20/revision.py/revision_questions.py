#Ask the user for their name and age. Print a message saying how old they will be in 10 years.
"""name= input("Enter your name: ")
age=int(input("Enter your age: "))
x= age + 10
print(f"Hello {name}, you will be {x} years old in 10 years.")"""

#Ask the user for two numbers. Print their sum, difference, product, and remainder.
"""number1= int(input("Enter the first number: "))
number2= int(input("Enter the second number: "))
sum_result= number1 + number2
difference= number1 - number2
product= number1 * number2
remainder= number1 % number2
print(f"Addition gives: {sum_result}")
print(f"Subtraction gives: {difference}")
print(f"Multiplication gives: {product}")
print(f"Remainder gives: {remainder}")"""

#A shopkeeper sells pens at ₹5 each. Ask the user how many pens they want and print the total cost.
# A shopkeeper sells pens at ₹5 each. 
# Ask the user how many pens they want and print the total cost.
"""price_per_pen = 5
num_pens = int(input("How many pens do you want? "))
total_cost = num_pens * price_per_pen
print("Total cost: ₹", total_cost)"""

#Ask the user for a number. Print whether it is positive, negative, or zero.
"""number= int(input("Enter a number: "))
if number > 0:
    print("positive")
elif number == 0:
    print("0")
else:
    print("negative")"""

#Ask the user for three numbers. Print the largest of the three without using max().
# Ask the user for three numbers. Print the largest of the three without using max().

"""num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)
#A cinema charges ₹150 for adults, ₹80 for children under 12, and ₹100 for seniors over 60. Ask for the person's age and print the ticket price.
"""
"""print("Hello, welcome to the cinema.")
age= int(input("Please enter your age: "))
if age < 12:
    print("Ticket price: Rupees 80")
elif age < 60:
    print("Ticket price: Rupees 150")
else:
    print("Ticket price: Rupees 100")"""

#Write a program that checks if a year is a leap year. 
"""year= int(input("Enter an year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")"""

# Print all numbers from 1 to 50 that are divisible by 3 but not by 9.

"""for num in range(1, 51):
    if num % 3 == 0 and num % 9 != 0:
        print(num)"""

#Write a program that keeps asking the user to guess a number between 1 and 10 until they get it right. Print how many guesses it took.
"""number= 5
guess= int(input("Guess ther number: "))
if number == guess:
    print("You guessed the number !")
else:
    print("Try again.")"""

#Print the following pattern:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 

# Print the following pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#rows = 5

"""for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()"""