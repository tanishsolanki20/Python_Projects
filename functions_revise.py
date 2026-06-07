"""def wow(variable= "3"):
    x= input("Enter a random number ")
    if x== variable:
        print("You guessed the number")
    else:
        print("The answer is incorrect")

wow()
"""
"""print("*")
print("**")
print("****")
print("******")
print("********")"""

# rows = 5

# for i in range(1, rows + 1):
#     # Loop to print leading spaces
#     for j in range(rows - i):
#         print(" ", end="")
        
#     # Loop to print the stars
#     for k in range(2 * i - 1):
#         print("*", end="")
        
#     # Move to the next line after completing the row
#     print()
rows = 5
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

rows = 5
for i in range(rows, 0, -1):
    # Leading spaces
    for j in range(rows - i):
        print(" ", end="")
    # Stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()
