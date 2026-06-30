"""t = (1, 2, 3)
print(t[1:])"""

"""s = {1, 2, 3}
s.add(2)
s.add(4)
print(len(s))"""

#name = "amit"
# print(name.upper().startswith("AM"))
"""
d = {"x": 10}
print(d.get("y", 99))"""

"""counts = {}
for letter in "aabbbc":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)"""

"""Write a function unique_hobbies(friend_a, friend_b) that takes two sets of hobbies and
returns a single set containing only the hobbies that are NOT shared between the two
friends (hobbies unique to one friend or the other, not both)."""

"""def unique_hobbies(friend_a, friend_b):
    x= friend_a-friend_b
    y= friend_b-friend_a
    z= friend_a | friend_b
l={"painting", "hiking", "swimming"}
a={"dancing", "singing", "painting"}
print(unique_hobbies(l,a))"""

#Write a function has_duplicates(lst) that takes a list and returns True if it contains any
#repeated values, and False otherwise. You must use a set in your solution.

"""def has_duplicates(lst):
    y=set()
    for i in lst:
        if i in y:
            return True
        y.add(i)
    return False
a=["apple", "banana", "watermelon"]
print(has_duplicates(a))"""
    

    