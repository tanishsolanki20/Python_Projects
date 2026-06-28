"""prices={"Apple": 50, "Banana": 20, "Mango": 80}
for fruit, price in prices.items():
    print(f"{fruit} costs Rs{price}.")"""

"""inventory = {"Pen": 50, "Notebook": 30}
item= "Pen"
if item in inventory:
    print(inventory[item])
else:
    print("Out of stock.")"""

"""names = ["amit", "priya", "rahul"]
scores = [85, 92, 78]
gradebook = dict(zip(names, scores))
print(gradebook)"""

"""def map_word(sentence):
    x= {}
    l= sentence.split()
    for word in l:
        x[word]= len(word)
    return x
print(map_word("Mary had a little lamb"))"""

"""def merge_inventories(inv1, inv2):
    
    merged= dict(inv1)
    for item, quantity in inv2.items():
        merged [item]= merged.get(item,0)+ quantity
        return merged

fruit1 = {"Lychee": 30, "Mango": 20, "Watermelon": 18}
fruit2 = {"Banana": 29, "Mango": 31, "Apple": 10}
print(merge_inventories(fruit1,fruit2))"""

