#Example 1---- Temperature converter Write a function celsius_to_fahrenheit(temp) that converts a temperature. Formula: (temp × 9/5) + 32. Test it with 0°C (should give 32°F) and 100°C (should give 212°F).
"""def celsius_to_fahrenheit(temp):
    x= (temp * 9/5) + 32
    return x
print(celsius_to_fahrenheit(37))"""
#Username generator Write a function make_username(first_name, last_name, birth_year) that returns a username like "arjun_sharma_2010".
"""f_name=input("Enter your name ")
l_name=input("Enter your last name ")
year=input("Enter your birth year ")
def make_username(first_name=f_name, last_name=l_name, birth_year=year):
    return first_name + "_" + last_name + "_" + birth_year
print(make_username())"""
#Exercise 3 — Lives manager Write a function lose_life(current_lives) that returns the new life count. If lives drop to 0, also print "Game Over!".

#Hint: Two cases — lives still left, or lives = 0. What should this function return in each case?
"""def lose_life(current_lives):
    current_lives -= 1          # subtract 1 from current lives
    if current_lives == 0:
        print("Game Over!")
    return current_lives
lose_life(3)   # returns 2,  no message
lose_life(2)   # returns 1,  no message
lose_life(1)   # returns 0,  prints "Game Over!"
lose_life(0)   # returns -1, no message (already past 0)"""
#Exercise 4 — Quiz answer checker with streak Write a function check_with_streak(answer, correct, streak) that returns the new streak count. Streak goes up by 1 if correct, resets to 0 if wrong.
"""def check_with_streak(answer, correct, streak):
    if streak"""
"""def check_with_streak(answer, correct, streak):
    if answer == correct:
        streak += 1
    else:
        streak = 0
    return streak"""
"""def wow(name, age=12):
    print("Hello", name, "you are", age, "years old")
    return name, age
wow("Tanish")"""
def l(score):
 """   if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score > 100:
        return "Invalid score"
    else:
        return "F"
print(l(80))"""