#Write a program that asks the user for their full name and prints it with proper capitalization, with leading/trailing spaces removed.

"""x= input("Enter your name: ")
x=x.strip().upper()
print(x)"""

#Write a program that takes a sentence and tells the user how many words and how many characters (excluding spaces) it contains.

"""sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)

char_count = len(sentence.replace(" ", ""))

print(f"Word count: {word_count}")
print(f"Character count (excluding spaces): {char_count}")"""

#Build a simple "username availability checker" — take a list of taken usernames and a username the user wants, normalize both for case and whitespace, and tell them if it's available.

"""taken_usernames=["Rahul_20", "##Gamer43##", "SSGamers_19"]
x= input("What should we call you ?")
for i in taken_usernames:
    if x==i:
        print("Username taken ! Please pick another username.")
        break
    else:
        print(f"hi {x}")
        break"""

#Build a "word reverser" that takes a sentence and reverses the order of the words (not the letters) — e.g. "I love Python" becomes "Python love I".

"""x = input("Enter a sentence: ")
y = x.split()
print(y)
z=y[::-1]
c=" ".join(z)
print(c)"""

#Build a basic "text anonymizer" — given a paragraph and a list of names to hide, replace every occurrence of each name (case-insensitive) with "[REDACTED]", and report how many replacements were made in total. This mirrors real-world data privacy tools.

"""import string

def anonymize_text_v2(paragraph, names):
    names_lower = set(name.lower() for name in names)
    total_replacements = 0
    
    words = paragraph.split()
    new_words = []
    
    for word in words:
        # strip punctuation to compare the "core" word, but keep it for reattaching
        stripped = word.strip(string.punctuation)
        prefix_len = len(word) - len(word.lstrip(string.punctuation))
        suffix_len = len(word) - len(word.rstrip(string.punctuation))
        
        prefix = word[:prefix_len]
        suffix = word[len(word)-suffix_len:] if suffix_len else ''
        
        if stripped.lower() in names_lower:
            new_words.append(prefix + '****' + suffix)
            total_replacements += 1
        else:
            new_words.append(word)
    
    return ' '.join(new_words), total_replacements


text = "John met Sarah at the cafe. JOHN was late, but sarah didn't mind."
names_to_hide = ["John", "Sarah"]

anonymized, count = anonymize_text_v2(text, names_to_hide)
print(anonymized)
print(f"Total replacements: {count}")"""


