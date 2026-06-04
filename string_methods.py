"""answer= "paris"
guess= input("Enter the capital of France: ")

if guess.lower() == answer:
    print("Correct!")
else:
    print("Wrong, try again.")"""
"""name= "     tanish solanki      "
print(name)
#full_name= name.split()
print(name.lstrip().rstrip())
# print(full_name)
# print(full_name[0])
# print(full_name[1])
first_name= "tanish"
last_name= "solanki"
print(name)
print(name.upper())
print(name.capitalize())

print(first_name.capitalize()+" "+last_name.capitalize())

print(name.title())

x= "I like cats"
print(x.replace("cats", "dogs"))

l= "red,green,blue".split()
print (l)
v= "red,green,blue".split(",")
print(v)

words=["hello", "world"]
result= "".join(words)
print(result)
result= " ".join(words)
print(result)
result= ", ".join(words)
print(result)

q= "***hello***"
print(q)
print(q.strip("*"))

will="hello123".isalpha()
print(will)
will= "hello123".isalnum()
print(will)
will= "hello123".isspace()
print(will) 
will= "123".isdigit()
print(will)
will= "Hello World".istitle()
print(will)
"""
# f string methods
name= "Arjun"
score= 90
total= 100

#Old Way (ugly)
print("Player"+ name +  " scored " + str(score) + " out of " + str(total))

#f-String (clean and modern)
print(f"Player {name} scored {score} out of {total}")

#You can put expressions inside{}
print(f"Percentage: {score/total*100:.1f}%")  # Percentage: 90.0%
print(f"{"Pass" if score >= 40 else "Fail"}")  # Pass
