#Basic function format
"""def greet():
    print("Hello, welcome to the programme.")
greet()"""

#Giving Arguments
"""def greet(name):
    print("Hello," + name + "!")
greet("Aanya")
greet("Rohan")

#Multiple Parameters
def intoduce(name, age):
    print( str (name) + " is " + str (age) + " years old. " )

intoduce(14, "Maya")

#Default Parameter values:

def greet(name= "friend"):
    print("Hello," + name + " ! " )
greet()
greet("Tanish")"""

#Key_distinction ----- print v/s return

def add_print(a,b):
    print(a+b)          #displays the result, but gives nothing back

def add_return(a,b):
    return a+b

x=add_print(3,4)
y=add_return(3,4)


