"""Write a function is_long(word) that returns True if the word has more than 5 characters, False
otherwise. Then call it and print the result."""
"""def is_long(word):
    return len(word) > 5


# Calling the function and printing the result
print(is_long("python"))     # 6 characters
print(is_long("hello"))      # 5 characters
print(is_long("elephant"))   # 8 characters"""

"""Build a dictionary called student with keys: name, age, grade, city. Then: (3 marks)
• Print each value using its key
• Update the grade to A+
• Use .get() to safely try to print a key called &#39;school&#39; (it doesn&#39;t exist — show the fallback)"""
"""student={"name":"Tanish", "age":13, "grade":"B", "city":"Pune"}"""

#Part 1
"""print(student["name"])
print(student["age"])
print(student["grade"])
print(student["city"])"""

#Part 2
"""student["grade"]="A+"
print(student)"""

#Part 3
"""if "school" in student:
    print(student)
else:
    print("Not found !")"""
