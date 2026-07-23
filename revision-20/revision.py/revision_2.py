"""x = 10
y = 3
print(x//y)
print(x%y)"""

"""name = "amit"
age = 15
print(f"My name is {name} and I am {age} years old.")"""
"""
type("hello")
print(type("hello"))"""

"""x = 15
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
"""

"""score = 72
grade = "A" if score >= 80 else "B" if score >= 60 else "C"
print(grade)"""

"""total= 0
for i in range(1,6):
    total += i
print(total)"""

""""x=10
while x > 0:
    x -= 3
print(x)"""

"""for i in range(5):
    if i == 3:
        break
    print(i)"""

"""def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print(greet("Alice"))
print(greet("Bob", "Hi"))"""

"""def mystery(n):
    if n == 0:
        return 0
    return n + mystery(n -1)

print(mystery(4))"""

"""def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))
print(is_prime(4))"""

"""def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))
print(count_vowels("Gym"))"""

"""def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))"""

"""t= (1, 2, 3, 4, 5)
print(t[1:4])
print(t[::-1])"""

"""def min_max(nums):
    return (min(nums), max(nums))

low, high = min_max([3, 1, 9, 4])
print(low, high)"""

"""def x(name, score):
    return f"{name} scored {score} points."
y=[x("Alice", 85), x("Bob", 92), x("Charlie", 78)]
print(y)
highest_score = max([85, 92, 78])
print(f"The highest score is: {highest_score}.")"""

"""a={1,2,3,4}
b={3,4,5,6}
print(a & b)
print(a | b)
print(a - b)
print(a ^ b)"""

"""words = ["apple", "banana", "apple", "cherry", "banana"]
print(len(set(words)))"""

"""def common_friends(a_friends, b_friends):
    return a_friends & b_friends
a={"Alice", "Bob", "Charlie"}
b={"Bob", "David", "Eve"}
print(common_friends(a, b))"""

"""def has_duplicates(lst):
    return len(lst) != len(set(lst))
print(has_duplicates([1, 2, 3, 4, 5]))  # False
print(has_duplicates([1, 2, 3, 4, 5, 3]))  # True"""

"""def double(n):
    print(n * 2)
result = double(5)
print(result)"""
"""items = ["apple", "banana", "cherry"]
print(items[-1])"""
"""a = 10
b = 3
print(a % b)
print(a ** 2)"""
"""for i in range(5):
    if i % 2 == 0:
        print(i)"""



"""count = 0
while count < 4:
    count = count + 1
    if count == 3:
        continue
    print(count)"""

"""def mystery(a, b):
    return a * b + 1
print(mystery(3, 4))
print(mystery(mystery(2, 2), 3))"""

"""def greet(name="friend"):
    return "Hello, " + name
msg = greet()
print(msg)
print(greet("Aisha"))"""

"""fruits = ["mango", "banana", "apple"]
fruits.append("grape")
fruits.remove("banana")
print(fruits[1])
"""

"""student = {"name": "Raj", "age": 15}
student["age"] = 16
student["grade"] = "10th"
print(student.get("grade", "unknown"))
print(student.get("email", "not set"))"""

"""scores = {"Aisha": 88, "Meera": 72, "Kabir": 91}
total = 0
for name in scores:
    total = total + scores[name]
print(total)"""
"""
tags = {"python", "python", "code", "code", "learn"}
print(len(tags))"""
"""student = {"name": "Aisha", "grade": "9th"}
print(student["age"])"""

"""def multiply(a, b):
    result = a * b
    return result

answer = multiply(4, 5)
print(answer)"""

"""total = 0
for i in range(1, 6):
    total = total + i
print(total)"""

"""price = 200
discount = price * 0.10
final = price - discount
print(final)"""

#Write a for loop that prints the multiplication table for 6, from 6×1 to 6×10. Each line should look like: 6 x 1 = 6


"""for i in range(1, 11):
    print(f"6 x {i} = {6 * i}")"""

#Write a function called is_passing(score) that returns True if the score is 50 or above, andFalse otherwise. Then call it with the value 47 and print a suitable message based on theresult.


"""def is_passing(score):
    return score >= 50

result = is_passing(47)
if result:
    print("The student is passing.")
else:
    print("The student is not passing.")"""

#Create a dictionary of 4 students and their scores. Loop through it and print only the names of students who scored 80 or above.

"""students = {"Alice": 85, "Bob": 72, "Charlie": 91, "David": 78}
for name, score in students.items():
    if score >= 80:
        print(name)"""



#Write a function called count_vowels(word) that takes a string and returns the number of
#vowels (a, e, i, o, u) in it. Make sure it works for both uppercase and lowercase letters. Call it with the word Programming& and print the result.

"""def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Programming"))"""