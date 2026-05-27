#Q1
"""fruits=["mango","apple","lychee","waterelon","orange" ]
print (fruits[0])
print (fruits[-1])
print (len(fruits))

#Q2
players = [
    ("Virat Kohli", 45),
    ("Rohit Sharma", 72),
    ("MS Dhoni", 13),
    ("Shubman Gill", 98),
    ("Hardik Pandya", 55)
]
scores = [score for _, score in players]

print(f"\nHighest Score : {max(scores)}")
print(f"Lowest Score  : {min(scores)}")
print(f"Total Runs    : {sum(scores)}")

#Q3
subjects = []

for i in range(1, 6):
    subject = input(f"Enter subject {i}: ")
    subjects.append(subject)

print("\nYour subjects:", subjects)
print("Total subjects entered:", len(subjects))"""

#Q4
"""def greet_student(name, grade):
    print(f"Welcome, {name}! You are in Grade {grade}.")

greet_student("Rahul", 10)
greet_student("Aditya", 8)
greet_student("Pratyush", 8)

#Q5
n=int(input("Enter a number: "))
if n%2==0:
    print("The number is even.")
else:
    print("The number is odd. ")"""

#Q6
"""my_dict= {
    "name": "Tanish",
    "age": 12,
    "city": "Pune",
    "favorite_sport": "Cricket"
}
for key in my_dict:
    print(f"My {key} is {my_dict[key]}.")"""

#Q7
"""phonebook={
    "Rahul":2332989823,
    "Aditya":2234332223,
    "Vikas":9876563210,
    "Pratyush":9960561731
}
name=input("Enter a name who you have to call:")
if name in phonebook:
    print("Phone Number:",phonebook[name])
else:
    print("Contact not found.")"""

#Q8
students=[
    {"name":"Rahul", "marks": 98, "grade": 9},
    {"name":"Pratyush", "marks": 94, "grade": 8},
    {"name":"Aditya", "marks": 67, "grade": 8},
    {"name":"David", "marks": 78, "grade": 10}
]
for student in students:
    print("Name:", student["name"], "| Marks:", student["marks"])