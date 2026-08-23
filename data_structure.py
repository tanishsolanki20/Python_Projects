#Lists
'''fruits=["apple", "banana", "mango"]

#Indexing
print(fruits[0])  #apple(indexing starts at 0!)
print(fruits[2])  #mango

#Updating Values
fruits.append("grape")  #adds to the end
fruits.remove("banana") #removes a specific item
fruits[0]= "pineapple"  #updates an item by position

print(len(fruits))'''

#Dictionaries
"""student={
    "name": "Kabir",
    "age": 14,
    "grade":"9th",
}

print(student["name"]) #Kabir
print(student["age"]) #14

student["age"]=15 #updates a value
student["school"]="DPS" #adds a new key-value pair

del student["grade"] #removes a key-value pair
print(student)"""


#Sets
"""unique_visitors={"Asha", "Raj", "Asha", "Meera"}
print(unique_visitors)

unique_visitors.add("Tara")
unique_visitors.remove("Raj")
print(unique_visitors)"""


#Tuples
"""days=("Monday", "Tuesday", "Wednesday")
print(days[0])"""
"""days[0]="Sunday"#ERROR- tuples cannot be modified"""

"""Q1. Make a basic list and print it 
Q2. Basic dictionary and print a value from the dictionary
Q3. Make a set 
Q4. Looping through a list with a function
Q5. Building a dictionary from scratch and looping. Starts with an empty dictionary {} and adds entries one at a time."""

#1
"""list=[1,4,2,5,6]
print(list)"""

#2
"""fruits={
    "apple": "red", "banana": "yellow", "orange": "orange"}
print(fruits["apple"])"""

#3
"""no_duplicates={1,3,3,4,2,4}
print(no_duplicates)"""

#4
"""def looping_through_a_list(names):
    for i in names:
        print(i)
looping_through_a_list(["Tanish", "Raj", "Rahul"])"""

#5
"""student={}
student["name"]="Rahul"
student["age"]=14
student["grade"]="9th"
print(student)"""

"""x={"name": ["Tanish"], "age": [13], "grade": ["8th"]}
for i in x:
    print(i)"""

"""def function_to_dictionaries(name, age, grade):
    x={"name": name, "age": age, "grade": grade}
    return x
print(function_to_dictionaries("Tanish", 13, 8))"""

"""Exercise 1:
Create a list of your 5 favorite movies. Print the first and last movie in the list using indexing.
(Hint: remember index 0 is first; what index gets the last item without counting manually? Try -1)

Exercise 2:
Create a dictionary representing a book with keys "title", "author", and "year". Print a sentence using all three values.
(Hint: access each value with book["title"] etc.)

Exercise 3:
Write a function add_student(roster, name) that takes a list called roster and a name, adds the name to the list, and returns the updated list.
(Hint: use .append() inside the function, then return roster)"""

#Exercise 1
"""fav_movies=["The Shawshank Redemption (1994)",
"The Godfather (1972)",
"The Dark Knight (2008)",
"The Lord of the Rings: The Return of the King (2003)",
"Pulp Fiction (1994)"]

print(fav_movies[0])
print(fav_movies[-1])"""

#Exercise 2
"""book={"title": "The Famous Five", "author": "Enid Blyton", "year": "2020"}
print(f"My favorite book is {book["title"]}, it is written by {book["author"]}, and the year is {book["year"]}.")"""
#Exercise 3
#roster=[]

"""def add_student(roster, name):
    roster.append(name)
    return roster
print(add_student(roster,"Tanish"))"""


"""Exercise 4:
Create a dictionary of 3 products and their prices. Loop through it and print each product with a 10% discount applied.
(Hint: loop through dictionary keys, calculate price * 0.9 for each)

Exercise 5:
Create a set of "students who submitted homework" and another set of "all students in class." Can you find which students did NOT submit? (Hint: look up the - operator between two sets, or loop and check in)"""

#4
"""products={"Milk": 20, "Vegetables": 100, "Snacks": 50}
for key,value in products.items():
    print(f"{key}:{value*0.9}")"""


#5
"""students_who_submitted_homework={"Tanish", "Rahul", "Raj", "Meera"}
all_students_in_class={"Tanish", "Pratyush", "Aditya", "Meera", "Raj", "Rahul"}
print(all_students_in_class-students_who_submitted_homework)"""

"""Easy
1. Create a list of 5 numbers. Write a loop that prints only the even ones.
2. Create a dictionary representing yourself (name, age, hobby). Print it in a nicely formatted sentence.
Medium
3. Write a function average_score(scores) that takes a list of numbers and returns the average.
4. Build a small dictionary-based "phonebook" with 4 contacts (name → phone number). Ask the user to type a name, and look up their number using .get() — print "Not found" if the name isn't in the dictionary.
Hard
5. Build a simple inventory tracker: a dictionary where keys are item names and values are quantities. Write a menu (using input + if/elif, like Phase 5's unit converter) that lets the user: (1) add an item, (2) remove an item, (3) view all items. Use a while True: loop so they can do multiple actions."""

#1
"""numbers=[1,3,2,5,6]
for number in numbers:
    if number % 2==0:
        print(number)"""

#2
"""myself={"name": "= Tanish", "age": "= 13", "hobby": "= Coding"}
for key,value in myself.items():
    print(f"My {key, value}")"""

#3
"""def average_scores(scores):
    sum=0
    for i in scores:
        sum=sum+i/len(scores)
    return sum
scores=[1,3,4,2]
print(average_scores(scores))"""

#4
"""phonebook={"Tanish": 9890392195, "Rahul": 9291032849, "Raj": 9203829392}
user_input=input("Enter the name: ")
result=phonebook.get(user_input)
if result is None:
        print("not found")
else:
    print(f"{user_input}={result}")"""

#5
"""inventory_tracker={"Golden Apple": 3, "Diamond Sword": 1, "Shield": 1, "Armor": 3}
user_command=int(input("What function do you want to perform ([1]Add an item, [2]Remove an item, [3]View all items) "))
if user_command==1:
    a=input("What do you want to add? ")
    b=int(input("enter qty: "))
    inventory_tracker[a]=b
elif user_command==2:
    c=input("What do you want to delete? ")
    del inventory_tracker[c]
elif user_command==3:
    for key,value in inventory_tracker.items():
        print(f"{key}:{value}")
else:
    print("No command executed!")"""









