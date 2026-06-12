class Student:
    school = "DPS Pune"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade= grade
        self.marks =[]

    #Method: add a mark to this student's list
    def add_marks(self, subject, score):
        self.marks.append({"subject": subject, "score": score})
        print (f"Added {subject}: {score} for {self.name}")

    #Method: calculate average
    def average(self):
        if not self.marks:
            return 0
        total = sum(m["score"] for m in self.marks)
        return round(total / len(self.marks), 1)

#Method: is the student passing?

    def is_passing(self, pass_mark=40):
        return self.average() >= pass_mark

#Method: print a report
    def report(self):
        print(f"\n=== {self.name} ({self.grade}) ===")
        for m in self.marks:
            print (f" {m["subject"]:12} {m["score"]}")
            print (f"   Average:    {self.average()}")
            print (f"   Status:     {"Pass"if self.is_passing()else "Fail"}")


aryan = Student("Aryan", 13, "8th")
priya = Student("Priya", 13, "8th")

aryan.add_marks("Maths", 88)
aryan.add_marks("Science", 92)
aryan.add_marks("English", 79)

priya.add_marks("Maths", 95)
priya.add_marks("Science", 87)
priya.add_marks("English", 91)

aryan.report()
priya.report()

print("\nAryan passing?", aryan.is_passing())
print("\nPriya passing?", priya.is_passing())
print("\nAryan average:", aryan.average())
print("\nAryan average:", aryan.average())

