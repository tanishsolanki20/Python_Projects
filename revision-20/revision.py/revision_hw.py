"""Take-Home Assignment

1. Write a program that asks for a number and prints "Even" or "Odd."
2. Ask the user for the temperature. If above 30, suggest they drink water. If below 10, suggest they wear a coat. Otherwise say "Nice weather!"

3. Build a simple login system — ask for a username and password, compare against stored values, and respond with success or failure messages.
4. Ask a user for their monthly income. Calculate and display which income tax bracket they fall into (you can make up 3 simple brackets).₹0-4 lakh nil, ₹4-8 lakh at 5%, ₹8-12 lakh at 10%

5. Build a "smart thermostat" program. Ask for the current temperature and whether it's daytime or nighttime ("day" or "night"). If it's day and above 28 degrees, say "Turning on AC." If it's night and below 18 degrees, say "Turning on heater." Handle all other combinations with appropriate messages. (Hint: nested conditions or logical operators)"""

#1
"""num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")"""

#2
"""temp=int(input("Enter the temperature in you area: "))
if temp>=30:
    print("Drink water!")
elif temp<=10:
    print("Wear a coat!")
else:
    print("Nice weather!")"""

#3
"""username="Stany"
password=13564
x=input("Enter the username: ")
y=int(input("Enter the password: "))
if x==username and y==password:
    print("successfully logged in!")
else:
    print("Incorrect username or password. Try again!")
"""

#4
"""monthly_income = int(input("Enter your monthly income: "))
annual_income = monthly_income * 12

if annual_income <= 400000:
    tax_percent = 0
elif annual_income <= 800000:
    tax_percent = 5
elif annual_income <= 1200000:
    tax_percent = 10
elif annual_income <= 1600000:
    tax_percent = 15
elif annual_income <= 2000000:
    tax_percent = 20
elif annual_income <= 2400000:
    tax_percent = 25
else:
    tax_percent = 30

print(f"Your annual income is ₹{annual_income}. Tax bracket: {tax_percent}%")"""
    
"""
temp=int(input("Enter the temperature: "))
time=input("Enter the time of the day(day|night): ")
if temp>=28 and time=="day".strip().lower():
    print("Turning on AC.")
elif temp<=18 and time=="night".strip().lower():
    print("Turning on heater.")
elif temp>=28 and time=="night".strip().lower():
    print("Do you want to turn on AC?")
elif temp<=18 and time=="day".strip().lower():
    print("Do you want to turn on heater?")
else:
    print("Invalid temperature details.")"""