#Easy Examples
#Example 1
"""with open("greeting.txt", "w")as file:
    file.write("Hello world! \n")
    file.write("This was written by python. \n")

print("File written successfully!")
"""

#Example 2
"""with open("greeting.txt", "r")as file:
    content=file.read
print(content)"""

#Example 3
"""try:
    age=int(input("Enter your age: "))
    print("You are", age, "years old.")
except ValueError:
    print("Please enter a valid number, not text.")"""

#Medium Examples
#Example 4
"""with open("greeting.txt", "r") as file:
    for line in file:
        cleaned=line.strip()
        print("Line: ", cleaned)"""

#Example 5
"""name=input("Enter your name: ")
with open("visitors.txt", "a")as file:
    file.write(name + "\n")

print("Welcome! Recorded!")
with open("visitors.txt", "r") as file:
    print("\n All visitors so far: ")
    for line in file:
        print("-", line.strip())
"""

