import random
print (random.randint(1, 100))
print (random.random())

team=["Aryan", "Priya", "Rohit", "Sonia", "Vikram"]
print (random.choice(team))
random.shuffle(team)
print (team)
print(random.sample(team, 3))


l=random.randint(1, 10)
while True:
 n= int(input("Enter a number:"))
 if n==l:
    print("Congratulations! You guessed the number.")
    break
 elif n<l:
    print(" Too low! Try again.")
else:
    print("Too high! Try again.")
