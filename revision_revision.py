#Exercise 1 — Answer cleaner Write a function clean(text) that strips whitespace and converts to lowercase. Test it by showing that " PARIS ", "paris", and "Paris" all become identical after cleaning.

"""def clean(text):
    x= text.strip().lower()
    return x
print(clean("paris"))
print(clean("PARIS"))
print(clean("Paris"))
"""

#Exercise 2 — Greeting formatter Write a function make_greeting(name, score) that returns a formatted string like: "Welcome back, Arjun! Your best score is 90/100 (90.0%)." Use an f-string. Make sure the name is properly title-cased even if the input isn't.

"""def make_greeting(name, score):
    percentage= "score"
    return f"Welcome back,{name.strip().title()} your best score is {score}/100."
print(make_greeting("Arjun", 90))"""

#Exercise 3 — Sentence analyser Write a function analyse(sentence) that prints: the number of words, whether it starts with a capital letter (istitle() or check sentence[0].isupper()), and how many times the letter "e" appears.

"""def analyse(sentence):
    h= sentence.split()
    d= len(h)
    c= sentence.isupper()
    e_count = sentence.lower().count("e")
    return h, d, c, e_count
print(analyse("Hello my name is Tanish."))"""

#Exercise 4 — Tag stripper Write a function strip_tags(text) that removes [EASY], [MEDIUM], or [HARD] tags from the start of a question string. For example "[EASY] What is 2+2?" becomes "What is 2+2?".

"""def strip_tags(text):
    text= text.replace("[Easy]","")
    text= text.replace("[Medium]","")    
    text= text.replace("[Hard]","")
    return text.strip()

print(strip_tags("[Easy] What is 2+2?"))
print(strip_tags("[Medium] What is the cube of 7"))
print(strip_tags("[Hard] Explain the Java script."))
    """
##Exercise 5 — Password checker Write a function is_strong_password(password) that returns True only if the password is 8+ characters, contains at least one digit (any(c.isdigit() for c in password)), and contains at least one uppercase letter (any(c.isupper() for c in password)).

#Hint: three separate conditions, all must be True.

def is_strong_password(password):
    h= len(password)>= 8
    r= password.isdigit()
    l= password.isupper()
    v= password.isalnum()
    return h, r, l, v
print(is_strong_password("Welcome2222"))

    

