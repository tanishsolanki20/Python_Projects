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
"""math_students = {"amit", "priya", "rahul"}
science_students = {"priya", "neha"}

print(math_students & science_students)
print(math_students | science_students)
print(science_students - math_students)"""

"""point = (3, 7)
x, y = point
print(f"x={x}, y={y}")"""

"""scores = [85, 90, 85, 78, 90, 92]
unique_scores = set(scores)
print(unique_scores)"""

"""allowed_users = {"amit", "priya", "rahul"}
name = "amit"
print(name in allowed_users)"""

"""def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = get_stats([4, 8, 15, 16, 23])
print(f"low={low}, high={high}, avg={avg:.1f}")"""

"""team_a = {"amit", "priya", "rahul", "neha"}
team_b = {"priya", "neha", "vikram"}

print("In both teams:", team_a & team_b)
print("Only in team A:", team_a - team_b)
print("Everyone combined:", team_a | team_b):"""

"""distances = {}
distances[(0, 0)] = 0
distances[(1, 1)] = 1.41
print(distances[(1, 1)])"""

"""def unique_in_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(unique_in_order([3, 1, 3, 2, 1, 4]))   # [3, 1, 2, 4]"""

"""visits = [("amit", "Monday"), ("priya", "Monday"), ("amit", "Monday"), ("rahul", "Tuesday")]
unique_visits = set(visits)
monday_count = sum(1 for person, day in unique_visits if day == "Monday")
print(monday_count)"""

#Write a function that takes a list of (name, age) tuples and returns the name of the oldest person. Hint: you can unpack each tuple inside a loop, or sort using a key function.

"""def oldest_person(people):
    oldest_name = None
    oldest_age = -1  # start lower than any real age

    for name, age in people:
        if age > oldest_age:
            oldest_age = age
            oldest_name = name

    return oldest_name

people = [("Pratyuh", 14), ("Bob", 45), ("Charlie", 22)]
print(oldest_person(people))  # Bob"""

#Given two sets of hobbies for two friends, find hobbies they don't share with each other (in either direction). Hint: think about which set operation gives you "everything except what's common."

friend_1= {"cricket", "painting", "singing"}
friend_2= {"cricket", "gaming", "studying"}
common= friend_1 & friend_2   
print(f"In both friends {common} is common.")
v= friend_1-friend_2
print(v)
n=friend_2-friend_1
print(n)
difference= v|n
print(difference)

