"""def greet_bad(name):
    print("Hello,"+ name) #output goes to screen, vanishes

def greet_good(name):
    return "Hello,"+ name #output becomes a value you can store

result_bad= greet_bad("Arjun") #result_bad = None !
result_good= greet_good("Arjun") #result_good = "Hello, Arjun"

#Default Parameters
def greet(name, greeting="Hello"):
    return greeting +"," +name +"!"

print (greet("Arjun")) #Hello, Arjun
print (greet("Arjun", "Namaste")) #Namaste, Arjun
#The parameter greeting="Hello" means: "if nobody tells me what greeting to use, use Hello."
def get_score_info(score):
    passed = score >=40
    grade = "A" if score >=90 else "B" if score >=70 else "C"if score >=50 else"F" 
    return passed, grade #return TWO things at once

passed, grade = get_score_info(75)
print(passed) #True
print(grade) #B"""
"""def greet_player(name):
    return "Welcome, "+ name +"! Ready to play?"

print(greet_player("Arjun"))
print (greet_player("Maya"))"""
"""def double (number, times=1):
    return number * (2**times)

print(double(5))
print(double(5,3))
"""
def get_grade(score):
    if score >=90:
        return "S"
    elif score >= 70:
        return "A"
    elif score>= 50:
        return "B"
    else:
        return "F"
    
print(get_grade(85)) #A
print(get_grade(45)) #F
