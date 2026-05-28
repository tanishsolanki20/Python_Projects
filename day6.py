"""def greet():
    print ("hello")
greet()"""
"""def greet2(name, age):
    print ("hello", name, "you are", age, "years old")
greet2("Tanish", 12)
greet2("Khushi", 21)
"""
"""def wow(name, age=12):
    print("hello", name, "you are", age, "years old")
wow("Tanish")
wow("Khushi", 21)
wow(15, "Tanish")
"""
"""def abc():
    a=10
    return a

print(abc())"""

#print(a)

total=0
def add_to_total(num):
    global total
    total += num

add_to_total(5)
print(total)