#Build a "tag deduplicator" — given a list of hashtags someone used across multiple posts (with repeats and inconsistent casing like "Python" vs "python"), normalize the casing and return only the unique tags as a set.
x=["Python", "python", "AI", "ai"]
def w(tags):
    t=set()
    for tag in tags.lower():
        