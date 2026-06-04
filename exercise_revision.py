def clean_answer(raw_input):
    return raw_input.strip().lower()

#Now these all match:
print(clean_answer("Paris"))
print(clean_answer("  paris  "))
print(clean_answer("PARIS"))

correct = "paris"
guess = input("Enter the capital of France: ")
if clean_answer(guess) == correct:
    print("Correct!")
else:
    print("Wrong, try again.")
    

def format_name(raw_name):
    return raw_name.strip().title()

print(format_name("  tanish solanki  "))
print(format_name("MARY JOHNSON"))


name= "tanish"
score=70
total= 100
percentage = score/total * 100

print(f"{"="*30}")
print(f"n Player: {name}")
print(f" Score : {score} / {total}")
print(f" Percentage: {percentage:.1f}%")
print(f" Result: {'Pass' if percentage >= 40 else 'Fail'}")
print(f"{"="*30}")

def get_valid_name():
    while True:
        name= input("Enter your name: ").strip()
        if len(name)==0:
            print("Name can't be empty. Try again")
        elif not name.replace(" ", "").isalpha():
            print("Name should only contain letters. Try again")
        else:
            return name.title()
        
player_name = get_valid_name()
print(f"Welcome, {player_name}!")

def analyze_text(text):
    words= text.strip().split()
    word_count = len(words)
    char_count = len(text.replace(" ", ""))
    unique_words= len(set(words))

    return{
        "words": word_count,
        "characters": char_count,
        "unique_words": unique_words
    }
sample = "the cat sat on the mat and the cat" 
stats = analyze_text(sample)
print(f"Words: {stats["words"]}")
print(f"Characters: {stats["characters"]}")
print(f"Unique words: {stats["unique_words"]}")
