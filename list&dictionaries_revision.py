"""planets= ["Mercury", "Venus", "Earth", "Mars",]
print(planets[0])
print(planets[2])
print(planets[-1])
planets[1]= "Venus"
planets.append("Jupiter")
planets.insert(1, "Mars")
print(planets)
planets.remove("Mars")
print(planets)
planets.pop(0)
print(planets)"""
#LIST SLICING
"""numbers= [10, 20, 30, 40, 50]
print(numbers[1:4])  #20,30,40
print(numbers[:3])  #10,20,30
print(numbers[2:])  #30,40,50"""
#DICTIONARIES
"""player= {
    "name": "Arjun",
    "score": 0,
    "lives": 3
}
print(player["name"])
print(player["score"])
print(player["lives"])
player["score"]= 10
player["level"]= 1
print(player)
del player["lives"]
print(player)
#CHECKING IF A KEY EXISTS
if "name" in player:
    print("Player found!")
    #LOOPING THROUGH A DICTIONARY
for key in player:
    print(key, ":", player[key])"""
"""question= [
    {"question": "Capital of France?", "answer": "Paris"},
    {"question": "Sides of a hexagon?", "answer": "6"},
    {"question": "How many planets are in our solar system?", "answer": "8"}


]
print(question[0]["question"])
print(question[0]["answer"])
for q in question:
    print(q["question"])
    user_answer= input("Your answer: ")
    if user_answer.lower()== q["answer"].lower():
        print("Correct!")
    else:
        print("Wrong! The answer was:", q["answer"])"""
"""questions=["Capital of France?", "Sides of a hexagon?", "How many planets are in our solar system?"]

for i in range(len(questions)):
    print(f"Question {i+1}: {questions[i]}")"""
scores=[]
scores.append(10)
scores.append(20)   
print(scores)

print("All scores:" , scores)
print("Total:", sum(scores))
print("Average:", round(sum(scores)/len(scores)))

