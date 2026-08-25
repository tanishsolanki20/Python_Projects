#Error Code---(TypeError)
"""age=14
print("I am" + age + "years old")"""

#Correct Code---(No Error)
"""age=14
print("I am "  +  str( age )  +  " years old. ")"""


# BROKEN
"""student = {"name": "Aisha", "age": 14}
print(student["grade"])"""

"""student = {"name": "Aisha", "age": 14}
print(student.get("grade"))"""

# BROKEN
"""def greet(name):
    print("Hello, " + Name)

greet("Raj")"""

"""def greet(name):
    print("Hello, " + name)

greet("Raj")"""

"""def calculate_average(scores):
    print("DEBUG scores:", scores, type(scores))   # debug print
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    return average

result = calculate_average([80, 90, 70])
print("Average:", result)"""

"""Decomposition into functions

Problem: Ask for a student name and 3 scores, calculate average, print pass/fail"""

"""def get_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)

def is_passing(average):
    return average >= 50

def print_result(name, average):
    status = "PASS" if is_passing(average) else "FAIL"
    print(name + " — Average: " + str(average) + " — " + status)

name   = input("Enter student name: ")
scores = []
for i in range(3):
    score = int(input("Enter score " + str(i + 1) + ": "))
    scores.append(score)

average = get_average(scores)
print_result(name, average)"""

"""Each function has exactly one job. If the average calculation has a bug, you know to look in get_average. If the pass/fail logic is wrong, you look in is_passing. The problem is decomposed."""


"""Clean vs messy code comparison
"""
# MESSY — hard to read, cryptic names, no structure
"""def f(d):
    r = []
    for k in d:
        if d[k]["g"] == "9th":
            r.append(k)
    return r

# CLEAN — same logic, easy to read
def find_students_in_grade(students, target_grade):
    matching_students = []
    for name in students:
        if students[name]["grade"] == target_grade:
            matching_students.append(name)
    return matching_students"""















"""Exercise 1 — Fix the bug:

python
score = input("Enter your score: ")
if score >= 50:
    print("Pass")
else:
    print("Fail")

The program crashes when you run it. What's the error type? What's the fix?
(Hint: what type does input() always return?)

Exercise 2 — Fix the bug:

python
students = {"Aisha": 88, "Raj": 72}
print("Meera scored " + str(students["Meera"]))

This crashes. What type of error? Rewrite it so it prints a friendly message instead of crashing.
(Hint: .get() with a default value)

Exercise 3 — Decompose before coding:
On paper, break this problem into at least 4 steps, then write a function for each step:
"Ask the user for 5 numbers. Find the largest one. Print whether the largest number is odd or even."
(Hint: don't write code first — write the steps in English first)

Exercise 4 — Rename for clarity:
Rewrite this function with meaningful variable names and a comment explaining the logic:

python
def f(x, y):
    z = x * y / 100
    return x - z

Exercise 5 — Dictionary debugging:

python
inventory = {
    "apples": 10,
    "bananas": 5
}

inventory["oranges"] = inventory["oranges"] + 3
print(inventory)

This crashes on line 6. What's the error? Fix it so adding a quantity to a non-existent item creates it with that quantity, and adding to an existing item increases it.
(Hint: check if the key exists first)"""

#1
"""score = int(input("Enter your score: "))
if score >= 50:
    print("Pass")
else:
    print("Fail")"""

#2
"""students = {"Aisha": 88, "Raj": 72}
print("Meera scored",students.get("Meera"))"""

#3
"""user_input1=int(input("Enetr the first number: "))
user_input2=int(input("Enetr the second number: "))
user_input3=int(input("Enetr the third number: "))
user_input4=int(input("Enetr the fourth number: "))
user_input5=int(input("Enetr the fifth number: "))
biggest_number=max(user_input1, user_input2, user_input3, user_input4, user_input5)
print(biggest_number)
if biggest_number%2==0:
    print("Even")
else:
    print("Odd")"""

#4
"""def finding_percentage(num1, num2):
    percentage= num1 * num2 / 100 #Percentage formula variables(or parameters) defined as num1 and num2
    return percentage
print(finding_percentage(3,5))
"""

#5
"""inventory = {
    "apples": 10,
    "bananas": 5
}

finding=inventory.get("oranges")
print(finding)"""

