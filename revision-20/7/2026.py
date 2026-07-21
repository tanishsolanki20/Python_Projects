"""coordinates=(342, 564)
rgb=(255, 0, 0)
print(coordinates[0])
for i in rgb:
    print(i)

x,y= coordinates
print(x, y)"""

"""def values(numbers):
    return min(numbers), max(numbers)
print(values([1, 2, 3, 4, 5]))
low, high = values([1, 2, 3, 4, 5])
print(low, high)"""

"""student_ids={3454627, 3454628, 3454629}
student_ids.add(3454630)
student_ids.add(3454627)
print(student_ids)
print(3454627 in student_ids)"""
"""
x= [96, 100, 88]
set_x= set(x)
print(set_x)"""
"""
maths_class= {"John", "Mary", "Peter"}
science_class= {"Mary", "rahul", "David"}
print(maths_class.intersection(science_class))
print(maths_class.union(science_class))
print(maths_class.difference(science_class))"""
"""
x= "                Tanish"
print(x.upper())
email= x.strip().lower()
print(email)"""

"""x= "t3nish"
x= alphanumeric= x.isalnum()
print(x)
print("hello".startswith("t"))
print("hello".endswith("o"))
print("hello".isdigit())"""

print("cat" in "the cat sat on the mat")

text= "the cat sat on the mat"
print(text.count("at"))
print(text.find("cat"))
sentence= "the cat sat on the mat"
words= sentence.split()
print(len(words))
