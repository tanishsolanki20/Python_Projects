def light(correct_answer="paris"):
    x=input("What is the capital of France? ")
    if x.strip().lower() == correct_answer.strip().lower():
        print("Correct")
    else:
        print("Incorrect")

light()