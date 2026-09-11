"""Exercise 1:
Write a program that asks the user for their favourite colour and saves it to a file called "colour.txt". Then read the file and print the contents with a message like "Your favourite colour is: blue".
(Hint: write mode first, then read mode — two separate with blocks)

Exercise 2:
Write a program that uses try/except to safely divide two numbers entered by the user. Handle both ValueError (non-numeric input) and ZeroDivisionError (dividing by zero) with separate, clear messages.
(Hint: two except blocks, like Example 3 from the teaching notes)

Exercise 3:
Write a "visitor log" program that appends the user's name to "log.txt" every time it runs, then reads and prints all previous visitors.
(Hint: append mode first to add the name, then read mode to display all)"""

#Exercise 1
"""fav_colours=input("Enter your favourite colour: ")
with open("colour.txt", "w") as file:            
    file.write(fav_colours)
with open("colour.txt", "r") as file:
            content=file.read()
            print(content)"""

#Exercise 2
"""try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(num1/num2)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Please enter a digit other than 0. ")"""

#Exercise 3
"""user_input=input("Enter your name: ")
with open("log.txt", "a") as file:
    file.write(user_input + "\n")

with open("log.txt", "r") as file:
    content=file.read()
    print(content)"""

"""Exercise 4:
Using the random module, write a function generate_password(length) that returns a random string of letters and digits. Use import string to get string.ascii_letters and string.digits, and random.choice() to pick each character.
(Hint: build the password using a loop, appending one random character at a time)

Exercise 5:
Write a function safe_open(filename) that tries to open and return the contents of a file. If the file doesn't exist, it should create the file with the content "New file created.\n" and return that string instead of crashing.
(Hint: except FileNotFoundError — inside the except block, open the file in write mode to create it)"""

#4
"""import random
import string
def generate_password(length):
    password=string.ascii_letters + string.digits
    password_length="".join(random.choice(password) for _ in range(length))
    return password_length
print(generate_password(12))"""

#5
"""try:
    with open("safe_open_file.txt", "w") as file:
        message=file.write("File created!\n")
        print(message)
except FileNotFoundError:
    print("File not found!")"""
