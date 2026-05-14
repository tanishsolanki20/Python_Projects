"""for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)"""


a= ["Tanish", "Solanki"]
for i, name in enumerate(a):
    print(f"Index: {i}, {name}")
    print(list(enumerate(a)))

    
b= input("Enter a number: ")
for i in range(1, int(b) + 1):
    for j in range(1, int(b) + 1):
        print(i, j)



