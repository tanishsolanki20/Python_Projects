#Build a "tag deduplicator" — given a list of hashtags someone used across multiple posts (with repeats and inconsistent casing like "Python" vs "python"), normalize the casing and return only the unique tags as a set.
"""x=["Python", "python", "AI", "ai"]
def duplicate(tags):
    t=set()
    for tag in tags:
        y= tag.lower()
        t.add(y)
    return t

print(duplicate(x))"""

#Build a simple contact book where each contact is stored as a tuple (name, phone, email) inside a list, then write a search function that finds and returns the full tuple for a given name.
"""contact=[("Alice", "9834345213", "xyz"), ("Vikram", "9201345026", "abc"), ("Lily", "3099232345", "pqr")]
def find_contact(name):
    for t in contact:
        if t[0].lower()== name.lower():
            return t
        else:
            None
print(find_contact("Alice"))"""

#Build a "friend recommendation" mini-system: given a dictionary where each person maps to a set of their friends, write a function that suggests new friends for a person — defined as friends-of-friends who aren't already their friend (and isn't the person themselves). This mirrors a real feature in social apps and requires combining set operations with iteration.

def recommend_friends(friends, person):
    """
    Suggest new friends for `person`: friends-of-friends who aren't
    already their friend and aren't the person themselves.
    """
    direct_friends = friends.get(person, set())
    
    fof = set()
    for friend in direct_friends:
        fof = fof.union(friends.get(friend, set()))
    
    recommendations = fof - {person} - direct_friends
    
    return recommendations


# Example usage
friends = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}

print(recommend_friends(friends, "A"))  # Output: {'D'}
