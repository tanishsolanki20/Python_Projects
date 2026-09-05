#File Handling Basic Structure-
"""with open("filename.txt", "mode") as file:"""

#Writing to a File
"""with open("notes.txt", "w") as file:
    file.write("Hello, file! \n")
    file.write("This is the second line \n")"""

#Reading from a file:
"""with open("notes.txt", "r") as file:
    content=file.read()
    print(content)"""

#Reading line by line:
"""with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())"""

#Appending to a file:
"""with open("notes.txt", "a") as file:
    file.write("New line added!\n")
"""

#Error Handling-try/except, Basic Structure:
"""try:
    #code that might go wrong
except Errortype:
    #what to do if that error happens."""

#Multiple except blocks:
"""try:
    number=int(input("Enter a number: "))
    result=10/number
except ValueError:
    print("That wasn't a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")"""

#The else and finally clauses
"""try:
    number=int(input("Enter a number."))
except ValueError:
    print("Invalid Input.")
else:
    print("Success! You entered: ", number)
finally:
    print("This always runs, error or not.")"""

#Catching any error:
"""try: 
    risky_code()
except Exception as e:
    print("Something went wrong", e)"""







