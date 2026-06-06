#Exercise 1 — Fruit basket Create a list of 5 fruits. Print the first, print the last using a negative index, add a new fruit, remove one, then print the final list and how many items it has.

#Hint: append(), remove(), len() — check the cheat sheet.

"""fruits= ["Apple", "Banana", "Lychee", "Grapes", "Strawberry"]
print(fruits[0])
print(fruits[-1])
fruits.append("Watermelon")
print(fruits)
fruits.remove("Watermelon")
print(fruits)
print(len(fruits))"""

#Exercise 2 — Student record Create a dictionary for a student with keys: "name", "age", "grade". Print a sentence using all three values. Then add a "favourite_subject" key and print the updated dictionary.

#Hint: Access values with dict["key"]. Add new keys the same way you'd update one.

"""student={
    "name":"Tanish",
    "age": 12,
    "grade":8
}
for f in student:
    print(student)

student["favoutite_subject"]= "maths"
print(student)"""

#Exercise 3 — Quiz question bank Create a list of 3 dictionaries. Each dictionary should have a "question" and "answer" key. Loop through the list, print each question, and ask for input. Print whether each answer was correct.

#Hint: for q in questions: then q["question"] and q["answer"].

"""questions=[
    {"question": "What is the capital of france ? ", "answer": "paris"},
    {"question": "What is 2+2 ? ", "answer": "4"},
    {"question": "Who wrote The Diary of a Wimpy Kid ? ", "answer": "jeff kinney"}
]

score= 0

for q in questions:
    user_answer = input(q["question"] + " ")     #Code NOT WORKING

    if user_answer.strip().lower()== q["answer"]:
        print("Correct !")
        score +=1
    else:
        print(f" Wrong! The correct answer is: {q["answer"]}\n")

print(f"Your final score: {score} out of 3")"""

#Exercise 4 — High score tracker Create an empty list called scores. Write a function add_score(scores, new_score) that appends the score to the list. Write another function get_best(scores) that returns the highest score using max(). Test with at least 4 scores.

#Hint: max(my_list) returns the largest value in a list.

"""scores=[]
def add_score(scores, new_score):
    scores.append(new_score)
    return scores

print(add_score(scores,10))
print(add_score(scores,20))
def get_best(scores):
    return max(scores)
print(get_best(scores))"""

#Exercise 5 — Inventory manager Create an empty dictionary called inventory. Write a pick_up(inventory, item) function that adds 1 to the item's count (or creates it at 1 if it doesn't exist yet). Use .get(). Test by picking up the same item twice and a different item once.

#Hint: inventory.get("sword", 0) returns the current count or 0 if it doesn't exist.
    
"""inventory={}
def pick_up(inventory, item):
        inventory[item] = inventory.get(item, 0) + 1
        return inventory
print(pick_up(inventory, "apple"))
print(pick_up(inventory, "apple"))
print(pick_up(inventory, "orange"))"""

#Take Home Assignment
#Easy
#Create a list of your 5 favourite games. Write a for loop that prints each one with its position number, like: "1. Minecraft". Hint: use enumerate() or range(len(...)).

"""games= ["Rivals", "Steal a Brainrot", "Escape Tsunami for Brainrots", "Brookhaven", "Dead Rails"]
for i in range(len(games)):
    print(f"{i+1}. {games[i]}")"""

#Create a dictionary representing a game character with at least 5 keys (name, hp, attack, level, weapon). Write a function describe_character(character) that prints a neat summary of all their stats.

"""game_character= {
    "Name": "Alex",
    "HP": 90,
    "Attack": "Stealth",
    "Level": "33",
    "Weapon": "Sniper"
} 

def describe_character(character):
    print(f"  Name: {character['Name']}")
    print(f"  HP: {character['HP']}")
    print(f"  Attack: {character['Attack']}")
    print(f"  Weapon: {character['Weapon']}")
describe_character(game_character)"""


    

