#Personal Information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_subject = input("Enter your favorite subject: ")
likes_coding = input("Do you like coding? (True/False): ")

print(name)
print(age)
print(favorite_subject)
print(likes_coding)




#smart calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error! Cannot divide by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operation!"

print("Result:", result)


