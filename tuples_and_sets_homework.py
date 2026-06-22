#Write a program that stores 5 of your favorite movies in a tuple (since you won't be changing this list), then prints them out one per line using a loop.

favourite_movies= ("Spiderman", "Interstellar", "Superman", "Avengers", "Haunted House")
for i in favourite_movies:
    print(i)

#Write a program that takes two lists of numbers from the user, converts both to sets, and prints which numbers appear in both lists.
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
v={x, y}
print(f"First you entered {x} and then you entered {y}")

