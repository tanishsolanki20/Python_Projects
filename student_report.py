class Student:
    school= "DPS Pune"
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
        self.marks= {}
    def add_marks(self, subject, score):
        if 0 <= score <= 100:
            self.marks[subject]= score
        else:
            print(f"Invalid score! {score} must be 100")

    def average(self):
        if not self.marks:
            return 0
        return round(sum(self.marks.values()) / len(self.marks), 1)
    def letter_grade(self):
        avg= self.average()
        if avg >= 90: return "A"
        elif avg >= 75: return "B"
        elif avg >= 60: return "C"
        elif avg >= 40: return "D"
        else: return "F"
    def top_subject(self):
        if not self.marks:
            return None
        return max(self.marks, key=self.marks.get)
    def report(self):
        print(f"\n{"="*40}")
        print(f"    {self.name}   |   {self.grade}    |     {self.school}  ")
        print(f"{"="*40}")
        for subject, score in self.marks.items():
            print(f"    {subject:15}    {score}")
        print(f"    {"-"*25}")
        print(f"    Average:        {self.average()}")
        print(f"    Grade:          {self.letter_grade()}")
        print(f"    Top subject:    {self.top_subject()}")

    def __str__(self):
        return f"{self.name}    | Avg: {self.average()} | Grade:{self.letter_grade()}"
        
    def __len__(self):
        return len(self.marks)
        
        #Create students
aryan = Student("Aryan", 13, "8th")
priya = Student("Priya", 13, "8th")
rahul = Student("Rahul", 14, "8th")

        #Add marks
aryan.add_marks("Maths", 100)
aryan.add_marks("Science", 92)
aryan.add_marks("English", 98)
aryan.add_marks("History", 98)

priya.add_marks("Maths", 100)
priya.add_marks("Science", 92)
priya.add_marks("English", 98)
priya.add_marks("History", 98)

rahul.add_marks("Maths", 100)
rahul.add_marks("Science", 92)
rahul.add_marks("English", 98)
rahul.add_marks("History", 98)

        #Print reports
aryan.report()
priya.report()
rahul.report()

        #use__str__
student = [aryan, priya, rahul]
print("\n--- Class Summary---")
for s in student:
    print(s)    #calls__str___

        #Find Class topper
topper = max(student, key=lambda s: s.average())
print(f"\nClass topper: {topper.name} ({topper.average()})")

