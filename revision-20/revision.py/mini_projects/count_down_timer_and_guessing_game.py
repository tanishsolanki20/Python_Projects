"""Mini Project — Countdown Timer & Guessing Game (Combined)

Objective: Build a two-part console program — a countdown timer followed by a number guessing game.

Requirements:

Part 1 — Countdown Timer:

Ask the user to enter a starting number (e.g. 10)
Use a while loop to count down to 0, printing each number
When it reaches 0, print "🚀 Liftoff!"

Part 2 — Guessing Game:

The computer "thinks of" a secret number (you can hardcode it, e.g. 42)
Use a while True: loop to keep asking the user to guess
Give hints: "Too high" or "Too low"
Use break when correct
Count the number of attempts and display it at the end

Sample Output:

Enter starting number: 5
5
4
3
2
1
🚀 Liftoff!

--- Guessing Game ---
Guess the number (1-100): 50
Too high!
Guess the number (1-100): 25
Too low!
Guess the number (1-100): 42
🎉 Correct! It took you 3 attempts."""

#Part-1
"""a=int(input("Enter a number to start the countdown: "))
while a>=1:
    print(a)
    a=a-1
print("Liftoff")"""

"""hard_coded_number=23
attempts=0
while True:
    a=int(input("Guess the number(1-100):   "))
    attempts+=1
    if attempts==7:
        break
    if a==hard_coded_number:
        print("You guessed it!")
        break
    elif a>hard_coded_number:
        print("Too high!")
    else:
        print("Too low!")

    # Bonus: congratulations banner using a for loop
    if a==hard_coded_number:
        for i in range(5):
            print("*" * (i + 1) * 4)
        else:
            print(f"Game Over! The correct number was {hard_coded_number}. ")


print(f"You took {attempts} attempts to guess.")"""

"""Bonus challenges:

Limit the guessing game to 7 attempts maximum — if they run out, reveal the number and say "Game over"
Add a for loop that prints a small congratulations banner made of * characters after winning
Track and print the worst guess (the one farthest from the correct answer)"""

"""import random

# ============================================
# PART 1: Countdown Timer
# ============================================
start = int(input("Enter starting number: "))

while start >= 0:
    print(start)
    start -= 1
print("Liftoff!")

# ============================================
# PART 2: Guessing Game
# ============================================
print("\n--- Guessing Game ---")

secret_number = 42
attempts = 0
max_attempts = 7
guesses = []  # to track worst guess later
won = False

while attempts < max_attempts:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    guesses.append(guess)

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct!")
        won = True
        break

if won:
    print(f"It took you {attempts} attempts.")

    # Bonus: congratulations banner using a for loop
    for i in range(5):
        print("*" * (i + 1) * 4)
else:
    print(f"Game over! The number was {secret_number}.")

# ============================================
# Bonus: Track the worst guess (farthest from answer)
# ============================================
if guesses:
    worst_guess = max(guesses, key=lambda g: abs(g - secret_number))
    print(f"Your worst guess was {worst_guess} (off by {abs(worst_guess - secret_number)}).")

    font = {
    'A': [" * ", "* *", "***", "* *", "* *"],
    'C': ["***", "*  ", "*  ", "*  ", "***"],
    'G': ["***", "*  ", "* *", "* *", "***"],
    'I': ["***", " * ", " * ", " * ", "***"],
    'L': ["*  ", "*  ", "*  ", "*  ", "***"],
    'N': ["* *", "***", "***", "* *", "* *"],
    'O': ["***", "* *", "* *", "* *", "***"],
    'R': ["***", "* *", "***", "**  ", "* *"],
    'S': ["***", "*  ", "***", "  *", "***"],
    'T': ["***", " * ", " * ", " * ", " * "],
    'U': ["* *", "* *", "* *", "* *", "***"],
    ' ': ["   ", "   ", "   ", "   ", "   "],
}

word = "CONGRATULATIONS"

# Print row by row (5 rows total, since each letter is 5 rows tall)
for row in range(5):
    line = ""
    for letter in word:
        line += font[letter][row] + "  "  # space between letters
    print(line)"""

