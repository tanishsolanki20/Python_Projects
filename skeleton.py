#FUNCTION SKELETON
def name(param1, param2):  #def + name + params + colon 
    result= param1 + param2  #body = 4 spaces indented
    return result  #return sends value back

outpuut=name(5,10)  #call it and catch the result

#FOR LOOP PATTERNS
for i in range(5):  #01234
for i in range(1, 6):  #12345
for i in range(5, 0, -1):  #54321 (countdown)
for item in my_list:  #each item in a list

#WHILE LOOP
count= 0
while count < 5:
    print(count)
    count += 1  #NEVER forget this line or you will have an infinite loop

#COMMON MISTAKES
def greet(name)  #WRONG- missing colon
def greet(name):  #Correct

def f():
return #WRONG  missing indentation
    return 5 #correct 

result = greet  #WRONG - forgot()
result = greet()  #Correct
