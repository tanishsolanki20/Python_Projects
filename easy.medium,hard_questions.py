"""Easy
Write a program that saves three lines of text to a file, then reads them back and prints each line numbered: 1. Hello, 2. World, etc.
Use import datetime to get today's date (datetime.datetime.now()) and save it to a file called "last_run.txt". Each time the program runs, it should append the current date — so the file builds up a history of every run.
Medium
Build a simple "to-do list" that saves tasks to "tasks.txt". The user can type "add" to add a task (appended to the file) or "show" to display all current tasks. Use a while True: loop and "quit" to exit.
Write a function safe_divide(a, b) that handles ZeroDivisionError using try/except and returns None if division is impossible, or the result if it's fine. Then write a second function that uses safe_divide and prints either the answer or "Cannot divide by zero".
Hard
Build a "contact book" that saves to and loads from a file. Each contact is stored as name,phone on its own line. The program should have a menu (while True loop) with options to: add a contact (appends to file), search for a contact by name (reads file and searches), and list all contacts (reads and displays all). All file errors should be handled gracefully."""

#1
"""with open("save_three_lines_of_text", "w") as file:
        file.write("Hi my name is tanish\n")
        file.write("i am in 8th grade\n")

with open("save_three_lines_of_text", "r") as file:
        for i in file:
                print(i)

print(f"1.{i}")
print(f"2.{i}")"""

#2
"""import datetime
date=(datetime.datetime.now())
print(date)
with open("last_run.txt", "a") as file:
    file.write(f"date and time={date}\n")
with open("last_run.txt", "r") as file:
    file.read()"""

#3
"""user_action=input("What action do you want to do (add|show|quit)?       ")
if user_action=="add":
    with open("tasks.txt", "a") as file:
        file.write("Mopping the floor.")
elif user_action=="show":
    with open("tasks.txt", "r") as file:
        file.read()
elif user_action=="quit":
    with open("tasks.txt", "w") as file:
        file.write("                                                                       ")"""

#4
"""try:
        def safe_divide(a,b):
                return a/b
        print(safe_divide(4,2))
except ZeroDivisionError:
        print("Cannot divide by 0!")"""

#5
"""try:
        user_input=input("Which action do you want to perform (add a contact|search for a contact|lists all contacts)?  ")
        if user_input=="add a contact":
                with open("contact_book.txt", "a") as file:
                        file.write("Rahul-9293010193")
        elif user_input=="search for a contact" or "list all contacts":
                with open("contact_book.txt", "r") as file:
                        for i in file:
                                print(i)
except NameError:
        print("Name not found!")
finally:
        print("Programme Done!")"""

