"""def check_answer(player_answer, correct_answer, current_score):
    is_correct = player_answer.lower() == correct_answer.lower()
    if is_correct:
        new_score = current_score + 10
        feedback = "Correct! +10 points"
    else:
        new_score = current_score
        feedback = "Wrong! The answer was: " + correct_answer

    return is_correct, new_score, feedback

correct, score, msg = check_answer("Paris", "paris", 20)
print(msg)    # Correct! +10 points
print(score)  # 30"""
"""def is_even(number):
    return number % 2 == 0

def describe_number(number):
    if is_even(number):           # calling another function!
        kind = "even"
    else:
        kind = "odd"
    return str(number) + " is " + kind

print(describe_number(7))    # 7 is odd
print(describe_number(12))   # 12 is even"""
"""def ask_question(question, correct_answer):
    player_answer = input(question + " ")
    if player_answer.lower() == correct_answer.lower():
        print("Correct!")
        return 1     # 1 point earned
    else:
        print("Wrong! Answer was:", correct_answer)
        return 0     # 0 points

score = 0
score += ask_question("What is the capital of France?", "Paris")
score += ask_question("What is 7 x 8?", "56")
score += ask_question("What  is the capital of India?", "New Delhi")
print("Final score:", score, "/ 3")"""
def run_quiz(questions):
    """
    questions: a list of [question, answer] pairs
    Returns the final score
    """
    score = 0
    total = len(questions)

    for i, (question, answer) in enumerate(questions):
        print(f"\nQuestion {i+1} of {total}")
        player = input(question + " ").strip()
        if player.lower() == answer.lower():
            print("Correct! +10 points")
            score += 10
        else:
            print(f"Wrong. The answer was: {answer}")

    return score

my_quiz = [
    ["What planet is closest to the sun?", "Mercury"],
    ["How many sides does a hexagon have?", "6"],
    ["What language runs on the JVM?", "Java"],
]

final = run_quiz(my_quiz)
print(f"\nGame over! You scored {final} / {len(my_quiz) * 10}")


