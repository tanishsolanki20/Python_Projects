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
    
#Write a function is_palindrome(text) that returns True if the given text reads the same
#forwards and backwards, ignoring case and spaces. For example,
#is_palindrome(" Nurses ") should return True.

"""def is_palindrome(text):
    y= text.strip().lower()
    if y==y[::-1]:
        return True
print(is_palindrome("wow"))"""
    
#Write a function word_lengths(sentence) that takes a sentence and returns a dictionary
#mapping each unique word to the number of letters it has.

"""def word_length(sentence):
    x={}
    l= sentence.split()
    for i in l:
        x[i] = x[i.len()]

print(word_length("I am Tanish"))"""

#Write a function merge_inventories(inv1, inv2) that combines two dictionaries of item-quantity pairs, adding quantities together when the same item appears in both. Your function must not modify the original dictionaries passed in.

def merge_inventories(inv1, inv2):
    merged= dict(inv1)
    for item, quantity in inv2.items():
        merged[item]= merged.get(item, 0) + quantity

    return merged 
inv = {"Apple": 10, "Banana": 23, "Mango": 12, "Lychee": 8}
i = {"Apple": 3, "Banana": 23, "Mango": 32, "Lychee": 8}

print(merge_inventories(inv, i))
