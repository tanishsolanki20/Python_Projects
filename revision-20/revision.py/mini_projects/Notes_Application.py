"""Mini Project — Notes Application

Objective: Build a persistent notes app that saves, loads, and manages notes across multiple program runs — so notes survive even after the program closes.

Requirements:

Store notes in a file called "notes.txt"
On startup, load any existing notes from the file into a list
Menu with four options:
Add note — user types a note, it's added to the list and immediately saved to the file
View all notes — prints each note numbered
Delete note — user picks a number, that note is removed, file is updated
Exit
All file operations wrapped in try/except for safe handling
Use at least two separate functions: one to load notes from the file, one to save notes to the file."""

def add_note():
    note = input("Enter the note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added.")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
        print(content if content else "No notes yet.")
    except FileNotFoundError:
        print("No notes yet.")

def delete_note():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        print("No notes yet.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"{i}: {note.strip()}")

    choice = input("Which note number do you want to delete: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(notes)):
        print("Invalid note number.")
        return

    del notes[int(choice) - 1]
    with open("notes.txt", "w") as file:
        file.writelines(notes)
    print("Note deleted.")

while True:
    user_action = input(
        "What action do you want to perform (add note|view all notes|delete note|exit): "
    ).strip().lower()

    if user_action == "add note":
        add_note()
    elif user_action == "view all notes":
        view_notes()
    elif user_action == "delete note":
        delete_note()
    elif user_action == "exit":
        print("File exited.")
        break
    else:
        print("Command not found.")