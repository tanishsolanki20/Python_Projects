"""coordinates =(10, 20)
coordinates[0]= 99"""

#Comparison between a single item in a list and a tuple.
"""list=[3]
print(list)
tuple=(3)
print(tuple)
tuple2=(3,)
print(tuple2)"""

#Sets
"""ids={101, 102, 103} 
ids.add(101)        #already there - no effect
ids.add(104)        #now {101, 102, 103, 104}
print(101 in ids)   #True - and this check is nearly instany, even with a million items

#Removing Duplicates from a set
visitors = ["amit", "priya", "amit", "rahul", "priya"]
unique_visitors = set(visitors)
print(unique_visitors)  # {'amit', 'priya', 'rahul'} - duplicates gone"""

#Real mathematical set operations:
math_students = {"amit", "priya", "rahul"}
science_students = {"priya", "neha"}

print(math_students & science_students)
print(math_students | science_students)
print(science_students - math_students)