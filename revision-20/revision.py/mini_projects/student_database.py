"""Mini Project — Student Database

Objective: Build a simple student record system using a dictionary of dictionaries, combined with functions.

Requirements:

Create a dictionary called students where each key is a student's name, and each value is another dictionary holding their age and grade
Write a function add_student(students, name, age, grade) that adds a new student to the database and returns the updated dictionary
Write a function print_all_students(students) that loops through and neatly prints every student's details
Write a function find_student(students, name) that returns that student's info, or "Not found" if the name doesn't exist (use .get())

Sample Output:

=== Student Database ===
Aisha: Age 14, Grade 9th
Raj: Age 15, Grade 10th
Meera: Age 14, Grade 9th

Searching for 'Raj'...
Found: Age 15, Grade 10th

Searching for 'Zara'...
Not found

Bonus challenges:

Add a function students_in_grade(students, grade) that returns a list of names of all students in a given grade
Add a while True: menu so a user can repeatedly add, search, or list students without restarting the program
Track a set of all unique grades that exist in the database, and print it at the end"""







students = {
    "Aisha": {"age": 14, "grade": "9th"},
    "Raj":   {"age": 15, "grade": "10th"},
    "Meera": {"age": 14, "grade": "9th"},
}


def add_student(students, name, age, grade):
    students[name] = {"age": age, "grade": grade}
    return students


def print_all_students(students):
    if len(students) == 0:
        print("No students in the database.")
        return
    print("\n=== Student Database ===")
    for name in students:
        age   = students[name]["age"]
        grade = students[name]["grade"]
        print(name + ": Age " + str(age) + ", Grade " + grade)


def find_student(students, name):
    result = students.get(name)
    if result is None:
        return "Not found"
    return result


def students_in_grade(students, grade):
    matches = []
    for name in students:
        if students[name]["grade"] == grade:
            matches.append(name)
    return matches


def get_all_grades(students):
    grades = set()
    for name in students:
        grades.add(students[name]["grade"])
    return grades


# --- Main menu ---

while True:
    print("\n--- Student Database Menu ---")
    print("1. View all students")
    print("2. Add a student")
    print("3. Search for a student")
    print("4. Find students by grade")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print_all_students(students)

    elif choice == "2":
        name  = input("Enter student name: ")
        age   = int(input("Enter age: "))
        grade = input("Enter grade (e.g. 9th): ")
        students = add_student(students, name, age, grade)
        print(name + " added successfully.")

    elif choice == "3":
        name   = input("Enter student name to search: ")
        result = find_student(students, name)
        if result == "Not found":
            print("Student not found.")
        else:
            print(name + ": Age " + str(result["age"]) + ", Grade " + result["grade"])

    elif choice == "4":
        grade   = input("Enter grade to search (e.g. 9th): ")
        matches = students_in_grade(students, grade)
        if len(matches) == 0:
            print("No students found in grade " + grade)
        else:
            print("Students in grade " + grade + ": " + ", ".join(matches))

    elif choice == "5":
        all_grades = get_all_grades(students)
        print("\nGrades represented in this database: " + str(all_grades))
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")