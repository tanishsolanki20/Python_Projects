"""def add_score(scores, player, points):
    scores[player] = points
    return scores

def get_winner(scores):
    winner = ""
    top_score = 0
    for player in scores:
        if scores[player] > top_score:
            top_score = scores[player]
            winner = player
    return winner

scores = {}
scores = add_score(scores, "Aisha", 95)
scores = add_score(scores, "Raj", 87)
scores = add_score(scores, "Meera", 91)

winner = get_winner(scores)
print(f"The winner is {winner}!")"""




"""Build a quiz game that stores questions in a dictionary, asks each question, checks the answer, and prints the final score. Requirements:

Questions stored as a dictionary: {question: correct_answer}
A function ask_question(question, correct_answer) that prints the question, gets input, and returns True or False
A function run_quiz(questions) that loops through and calls ask_question for each one, tracks score, and returns total correct
Print the final score and a message based on performance

Sample Output:

--- Python Quiz ---
Q: What keyword defines a function? a
Incorrect! The answer was: def

Q: What does % give you? remainder
Correct!

Q: What type does input() return? str
Correct!

You scored 2 out of 3.
Good effort — keep practising!

Bonus challenges:

Add a dictionary that stores the player's answer alongside the correct answer for each question, and print a full review at the end
Add a scoring system where harder questions are worth more points (store each question's difficulty alongside the answer)"""
questions_with_answers={"Q: What keyword defines a function?(Easy)":"def", "Q: What does % give you?(Medium)" :"remainder", "Q: What type does input() return?(Hard)": "str"}
                        
def ask_question(question, correct_answer):
    user_answer = input("Q: " + question + " ")
    if user_answer.strip().lower() == correct_answer.strip().lower():
        print("Correct!")
        return True
        
    else:
        print("Incorrect! The answer was: " + correct_answer)
        return False

def run_quiz(questions_with_answers):
    score   = 0
    total   = len(questions_with_answers)
    results = {}

    for question in questions_with_answers:
        correct_answer        = questions_with_answers[question]
        is_correct            = ask_question(question, correct_answer)
        results[question]     = is_correct

        if is_correct:
            score += 1
        print()

    return score, total, results

score,total,results=run_quiz(questions_with_answers)
print(f"Your final score is {score} out of 3!")
if score==1:
    print("Not bad!")
elif score==2:
    print("Good try!")
elif score==0:
    print("Keep practicing!")
else:
    print("Excellent you got every question right !")