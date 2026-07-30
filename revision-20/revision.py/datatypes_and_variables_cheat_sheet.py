#Python Variables & Data Types — Complete Guide
"""1. Quick Revision
What is a Variable?

A variable is a name that points to a value stored in memory. Think of it as a labeled box where you keep something.

python
age = 25
name = "Alice"

Here, age and name are variables. Python figures out the data type automatically — you never declare types like in C or Java. This is called dynamic typing.

python
x = 10        # x is an int
x = "hello"   # now x is a str — totally legal in Python
Basic Data Types

int — whole numbers, positive or negative, no decimal point.

python
age = 25
temperature = -10

float — numbers with a decimal point.

python
price = 99.99
pi = 3.14159

str — text, wrapped in single or double quotes.

python
name = "Alice"
greeting = 'Hello!'

bool — only two values: True or False (capitalized, no quotes).

python
is_active = True
is_done = False

NoneType — represents "nothing" or "no value assigned". There's only one value: None.

python
result = None
Type Conversion

You can convert between types using built-in functions:

python
int("5")       # '5' (str) -> 5 (int)
float("3.14")  # '3.14' (str) -> 3.14 (float)
str(100)       # 100 (int) -> '100' (str)
bool(0)        # 0 -> False
bool(1)        # 1 -> True

Examples:

python
age_str = "20"
age_num = int(age_str)     # 20
print(age_num + 5)         # 25

x = str(42)                 # "42"
print(x + " apples")        # "42 apples"

⚠️ Not everything converts cleanly:

python
int("hello")   # ❌ ValueError — "hello" isn't a number
Checking a Variable's Type

Use type():

python
x = 10
print(type(x))       # <class 'int'>

y = "hi"
print(type(y))       # <class 'str'>

z = None
print(type(z))       # <class 'NoneType'>
2. Cheat Sheet
Variable Naming Rules
Rule	Valid	Invalid
Must start with a letter or _	_age, age1	1age
Can contain letters, digits, underscores	my_var2	my-var
No spaces	first_name	first name
Case-sensitive	Age ≠ age	—
Can't be a Python keyword	total	for, if, class
No special characters	user_name	user@name
Data Types Summary
Type	Example	Description
int	5, -10	Whole numbers
float	3.14, -0.5	Decimal numbers
str	"hi", 'yo'	Text
bool	True, False	Logical value
NoneType	None	No value
Type Conversion Functions
Function	Converts to	Example
int(x)	integer	int("5") → 5
float(x)	float	float("2.5") → 2.5
str(x)	string	str(10) → "10"
bool(x)	boolean	bool(0) → False
Useful Functions
Function	Purpose
type(x)	Check data type
isinstance(x, int)	Check if x is a specific type
id(x)	Memory address of x
len(x)	Length of a string/list
input()	Take input (always returns str)
print()	Display output
Important Syntax
python
x = 5                  # assignment
x, y = 1, 2            # multiple assignment
x = y = z = 0           # chained assignment
a, b = b, a              # swap values
x += 1                  # shorthand for x = x + 1
Beginner Tips
input() always returns a string — convert it if you need a number.
= assigns a value; == compares two values.
Falsy values in Python: 0, 0.0, "", None, False, [], {} — everything else is truthy.
Use snake_case for variable names (Python convention).
f-strings are the cleanest way to format text: f"My name is {name}".
3. Common Mistakes

1. Using quotes incorrectly

python
name = "Alice'   # ❌ mismatched quotes

Fix: use matching quotes — both '...' or both "...".

2. Mixing strings and numbers

python
age = 25
print("Age: " + age)   # ❌ TypeError

Why: Python won't auto-convert int to str in concatenation.
Fix: print("Age: " + str(age)) or use f-strings: print(f"Age: {age}").

3. Forgetting to convert input()

python
num = input("Enter a number: ")
print(num + 5)   # ❌ TypeError — num is a string

Fix: num = int(input("Enter a number: "))

4. Invalid variable names

python
1st_place = "Gold"   # ❌ starts with digit
my-var = 5             # ❌ hyphen not allowed

Fix: first_place = "Gold", my_var = 5

5. Case sensitivity

python
Name = "Bob"
print(name)   # ❌ NameError — 'name' was never defined

Why: Python treats Name and name as completely different variables.

6. Confusing = with ==

python
if x = 5:   # ❌ SyntaxError

Fix: if x == 5: — = assigns, == compares.

7. Using Python keywords as variable names

python
class = "Math"   # ❌ SyntaxError — 'class' is reserved

Fix: use class_name = "Math".

8. Assuming bool works like numbers everywhere

python
print(True + True)   # 2 — this is valid but confusing!

Why: bool is technically a subtype of int (True == 1, False == 0). Beginners often don't expect this.

9. Forgetting None isn't 0 or False

python
x = None
if x == 0:   # False — None is not equal to 0
    print("zero")

Fix: use if x is None: to check for None specifically.

10. Overwriting built-in function names

python
str = "hello"   # ❌ now str() the function is broken!
print(str(5))   # TypeError

Fix: avoid naming variables str, list, int, type, etc."""