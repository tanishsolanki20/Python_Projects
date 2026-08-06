"""Guided Practice

Exercise 1:
Write a for loop that prints the numbers 1 to 20.
(Hint: think about what range() arguments give you 1 through 20)

Exercise 2:
Write a while loop that prints "I love Python" exactly 4 times.
(Hint: you'll need a counter variable that starts at 0 or 1, and increases each time)

Exercise 3:
Write a program that asks the user to guess a number between 1 and 10. Use input() repeatedly inside a while loop until they guess correctly (you decide the secret number).
(Hint: similar structure to the password example)

Exercise 4:
Using a for loop and range(1, 51), print only the numbers divisible by 5.
(Hint: continue to skip the ones that aren't, or an if with %)

Exercise 5:
Write a loop from 1 to 100 that stops completely the moment it reaches a number greater than 30.
(Hint: break, not continue)

Easy
Print all even numbers from 1 to 30 using a for loop.
Use a while loop to count down from 10 to 1, then print "Liftoff!"
Medium
Write a program that adds up all numbers from 1 to 100 using a loop, and prints the total. (Hint: you'll need a variable that starts at 0 and keeps growing — this is called an "accumulator")
Ask the user to enter 5 numbers (one at a time, using a loop), and print the sum and average at the end."""

#1
"""for i in range(1,21):
    print(i)"""

#2
"""count=0
while count<=4:
    print("I love python.")
    count=count+1"""

#3
"""b=4
while True:
    a=int(input("Enter a number between 1-10: "))
    if a==b:
        print("youre right")
        break
    else:
        print("try again")"""

#4
"""for i in range(1,51):
    if i%5==0:
        print(i)
    else:
        continue"""

#5
"""for i in range(1,101):
    while True:
        if i<=30:
            print(i)
        else:
            print()
        break"""

#easy 1
"""for i in range(1,31):
    if i%2==0:
        print(i)
    else:
        continue"""

#easy2
"""count=10
while count>=1:
    print(count)
    count=count-1
print("Liftoff")"""

#medium1
"""count=0
for a in range(1,101):
    count+=a
print(count)"""

#medium2
"""x=0
for i in range(1,6):
    a=int(input("Enter a number: "))
    x+=a
print(x)"""

#Build a simple "guess the number" game: the computer picks a secret number (hardcode it for now, e.g. 7), and the user keeps guessing using a while loop. After each wrong guess, tell them "Too high" or "Too low." Use break when they guess correctly. Also count and display how many attempts it took.

"""hardcoded_number= 7
attempts=0
while True:
    a=int(input("Guess the number: "))
    attempts+=1
    if hardcoded_number==a:
        print("You guessed it!")
        break
    elif hardcoded_number>a:
        print("Too low!")
    else:
        print("Too high!")
print(attempts)"""

