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
days=("Monday", "Tuesday", "Wednesday")
print(days[0])
"""days[0]="Sunday"#ERROR- tuples cannot be modified"""
