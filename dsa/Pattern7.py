#space
for i in range(6):
    for j in range(6-i-1):
        print(" ", end=" ")
#star
    for j in range(2*i+1):
        print("*", end=" ")
    print()