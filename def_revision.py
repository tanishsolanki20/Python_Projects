#1. #A function with no parameters
#2. #A function with One parameters
#3. #A function with a return value
#4. #A function with multiple parameters and a calculation


#1
"""def my_details():
    
    z="Tanish"
    print(z)"""

#2
"""def my_details(name):
    return f"My name is {name}."
print(my_details("Tanish"))"""

#3
'''def my_details(name, age):
    return f"My name is {name} and my age is {age}"
print(my_details("Tanish", 13))'''

#4
"""def calculation(a, b):
    return a+b
print(calculation(3,1))"""

#Function example with default parameters
"""def default_parameters(name, age= 13):
    return f"My name is {name} and my age is {age}."
print(default_parameters("Tanish"))"""

#Function calling in another function
"""def cube(num):
    return num*num*num

def area(a,b):
    return cube(a) * cube(b)

print(cube(6))
print(area(13,1))"""

"""def num(number):
    number=[2,2,3,1]
    for i in number:
        if 1 in number:
            return "True"

print(num(1))"""

#1. Write a function called greet_with_time(name, time_of_day) that prints something like "Good morning, Aanya!" depending on the two arguments given.
#2. Write a function called is_adult(age) that returns True if age is 18 or above, and False otherwise. Then use it inside an if statement to print an appropriate message.
#3. Write a function called calculate_discount(price, discount_percent) that returns the final price after applying a percentage discount.
#Exercise 4:
#Write a function called count_vowels(word) that loops through a word and returns how many vowels (a, e, i, o, u) it contains.
#(Hint: you'll need a loop inside the function, and a counter that increases — combine Phase 4 ideas here)

#Exercise 5:
#Write a function called max_of_three(a, b, c) that returns the largest of three numbers, without using Python's built-in max().
#(Hint: nested if/elif comparisons, like Phase 3 — then return the answer instead of printing it)
#1
"""def greet_with_time(name, time_of_day):
    return f"Good {time_of_day}, {name}"
print(greet_with_time("Tanish", "Evening"))"""

#2
"""def is_adult(age):
    if age>=18:
        print("You are an adult.")
    else:
        print("You are NOT an adult.")
print(is_adult(3))"""

#3
"""def calculate_discount(price, discount_percent):                            
    return price* discount_percent/100
print(calculate_discount(100, 20))"""

#4
'''def count_vowels(word):
    vowels = "aeiou"
    counter = 0
    for i in word:
        if i in vowels:
            counter += 1
    return f"It contains {counter} vowels."

print(count_vowels("Tanish Solanki"))'''

#5
def max_of_three(a,b,c):
    if a>b and a>c:
        return f"{a} is the greatest."
    elif b>a and b>c:
        return f"{b} is the greatest."
    else:
        return f"{c} is the greatest."
print(max_of_three(330,1,9))