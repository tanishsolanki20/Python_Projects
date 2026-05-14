def sum_of_numbers(n):
    sum = 0
    for s in range(0, n + 1):
        sum += s
    return sum


a= input()
b= input()
c= input()
print(str(a)*int(a) + c + str(b)*int(b))