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

