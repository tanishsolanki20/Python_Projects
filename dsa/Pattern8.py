for i in range(6):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2*6-2*i-1):
        print("*", end=" ")
    print()