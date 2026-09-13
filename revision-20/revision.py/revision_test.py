"""import math 
print(math.sqrt(16))"""

"""try:
    print(int("42"))
    print(int("hello"))
except ValueError:
    print("Caught!")
print("Done.")"""

"""try:
    result = 100 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Always runs.")"""

"""import random
random.seed()
choices = ["rock", "paper", "scissors"]
print(random.choice(choices))
"""
"""lines = ["Aisha\n", "Raj\n", "Meera\n"]
for line in lines:
    print(line.strip())"""

"""try:
    f = open("missing_file.txt", "r")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Other error:", e)
finally:
    print("Finished.")"""

"""Write a program that writes the numbers 1 to 5 to a file called "numbers.txt" (one number per line), then reads it back and prints each line."""

"""with open("numbers.txt", "w") as file:
    for i in range(1,6):
        file.write(str(i)+"\n")
    
with open("numbers.txt", "r") as file:
    for line in file:
        print(line.strip())"""

"""Write a program that asks the user for their name and appends it to "visitors.txt" every time it runs. Then read and print all names in the file. What should the file contain after two separate runs with different names?""" 

"""with open("visitors.txt", "w") as file:
    name=input("Enter your name:    ")
    file.write(f"Name: {name}")
with open("visitors.txt", "r") as file:
    file.read()"""

""". Write a try/except block that:
    • Asks the user for a number
    • Converts it with int()
    • Divides 100 by that number
    • Handles ValueError and ZeroDivisionError separately
    • Prints the result if no error occurred (use the else block)
"""

"""try:
    num=int(input("Enter a number:  "))
    print(100/num)
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
"""

"""Using import math and import random: generate 4 random numbers between 1 and 50. Print each number and its square root rounded to 2 decimal places."""

"""import math
import random
random_num=random.randint(1,50)

print(random_num)
print(math.sqrt(random_num))"""

"""Write two functions: save_scores(scores, filename) that writes each {name: score} entry as name,score on its own line, and load_scores(filename) that reads it back and returns a dictionary. Test both with {"Aisha": 88, "Raj": 72}."""

user_input=input("Enter a name: ")
with open("scores.txt", "w") as file:
    file.write(f"{user_input} -> 90")
with open("scores.txt", "r") as file:
    file.read()


