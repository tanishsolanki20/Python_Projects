"""name=input("Please enter your name: ")
print(f"Hello {name}!")
age=int(input("Enter your age: "))
showtime=input("At what time is your show(morning|evening|night): ")
if age <= 12 :
    category="Child"
    price=100
    print("Ticket price: Rupees 100.")
elif age >=12 and age<=20:
    category="Teens"
    price=150
    print("Ticket price: Rupees 150.")
elif age >=20:
    category="Adult"
    price=200
    print("Ticket price: Rupees 200.")
elif age >= 60:
    category="Senior"
    price=120
    print("Ticket price: Rupees 120.")
else:
    print("Invalid age.")

if showtime== "morning":
    print("You got a 20 percent discount")
    price= price-(price*20/100)
    price_note=f"{price}"

    print("Your final price is", price_note)
elif showtime== "evening" or "night":
    price=price
    price_note=f"{price}"
    print("Full price")
else:
    print("Invalid time")   

print("----TICKET SUMMARY----")
print(f"Name:   {name}")
print(f"Age:    {age}")
print(f"Category:   {category}")
print(f"Showtime:   {showtime}")
print(f"Price:  {price_note}")"""
