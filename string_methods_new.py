"""email= "  Amit@Example.com  "
clean_email= email.strip().lower()
print(clean_email)"""

"""print("hello".startswith("he"))
print("hello".endswith("lo"))
print("hello".isdigit())
print("12345".isdigit())
print("hello" in "say hello there")"""

"""sentence = "the cat sat on the mat"
print(sentence.count("at"))
print(sentence.find("cat"))"""

"""sentence = "the cat sat on the mat"
words = sentence.split()
print(len(words))

rebuilt = " ".join(words)
print(words)"""

"""text= "I like Java"
text= text.replace("Java", "Python")
print(text)"""

"""name= "amit"
score= 87.456
print(f"{name}: {score:.1f}%")"""

# 1. Cleaning user input
"""raw= "PyThOn"
clean= raw.strip().lower()
print(raw)

# 2. Checking how a sentence starts
title = "Chapter 1: Introduction"
print(title.startswith("Chapter"))"""

# 3. Counting a substring
"""text= "banana"
print(text.count("an")) #2

# 4. Splitting a sentence into words and counting them
sentence= "the quick brown fox jumps over the lazy elephant"
words= sentence.split()
print(f"Word count: {len(words)}")
"""

# 5. Building a CSV line from a list of values
"""fields = ["amit",  " 15",  " 9th grade"]
line = ",".join(fields)
print(line)"""

# 6. Replacing and reformatting
"""phone = "98-765-43210"
digits_only= phone.replace("-", "")
print(digits_only)"""

# 7. Word frequency counter using split + a dictionary-free approach
"""sentence= "the cat sat on the mat the cat ran"
words = sentence.split()
unique_words = set(words)
for word in unique_words:
    print(word, words.count(word))"""

# 8. Validating a simple username
"""def is_valid_username(name):
    name= name.strip()
    return name.isalnum() and len(name) >= 3 and not name.isdigit()

print(is_valid_username("  amit99  ")) #True
print(is_valid_username("12345"))      #True
print(is_valid_username("a!"))         #False - not alphanumeric, too short"""

"""def capitalise(Sentence):
    x= Sentence.split()
    for i in x:
        print(i.capitalize())

capitalise("hello, im tanish")"""
"""
def find_vowels(word):
    word= word.lower()
    total= 0
    for letter in word:
        if letter in "aeiou":
            total += 1
    return total

print(find_vowels("Hello"))
print(find_vowels("Wow"))"""

"""def finding_palindrome(word):
    word= word.lower().replace(" ","")

    if word== word[::-1]:
        print("is palindrome")
    else:
        print("is not palindrome")
    
finding_palindrome("  malayalam   ")"""
    
"""def messy_names_structure(x):
    x=x.split(",")
    cleaned=[]
    for i in x:
        cleaned.append(i.strip())
    return cleaned

print(messy_names_structure("amit,   priya, rahul"))
"""
"""
def replacing_vowels_with_star(word):
    a=word
    for letter in "aeiou":
          a=a.replace(letter, "*")
    return a
print(replacing_vowels_with_star("aeroplanes"))"""
