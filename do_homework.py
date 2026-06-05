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
    {"question": "Who wrote The Diary of a Wimpy Kid ? ", "answer": "Jeff Kinney"}
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

