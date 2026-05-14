a= {"name": "Tanish", "age": 12, "city": "pune"}
a["school"]= "Vikhe patil Memorial School"
print(a)
del a["school"]
print(a)    
#rint(a["school"])
print(a.get("school"))
for key in a:
    print(key)

for key, value in a.items():
    print(key, ":", value)

students= {"Aryan" : {"age": 12, "score": 92, "city": "pune"},
           "Aditya" : {"age": 13, "score": 88, "city": "mumbai"},
           "Pratyush" : {"age": 12, "score": 95, "city": "delhi"}}
print (students["Aditya"]["score"])
print (students["Pratyush"]["city"])
for name, info in students.items():
    print(name, "scored", info["score"])