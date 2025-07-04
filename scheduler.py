
import os

existingExams = []

def displayMenu():
# Shows the menu to guide the user and add some ASCII art 
    print("\n" + "="*40)
    print(r"""
░█▀▀░█▄█░█▀▄░▀█▀░░░█▀▀░█▀▀░█░█░█▀▀░█▀▄
░▀▀█░█░█░█▀▄░░█░░░░▀▀█░█░░░█▀█░█▀▀░█░█
░▀▀▀░▀░▀░▀░▀░░▀░░░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀░
""")
    print("1. Add New Exam")
    print("2. View All Exams")
    print("3. Edit an Exam")
    print("4. Delete an Exam")
    print("5. Clear Terminal")
    print("6. Exit")

def addExam():
    examName = input("Enter Exam Name: ")
    # Check for duplicate exam name
    for exam in existingExams:
        if exam['name'].lower() == examName.lower():
            print("⚠️ Exam with that name already exists. Please use a different name.")
            return

    examDate = input("Enter Date (YYYY-MM-DD): ")
    examTime = input("Enter Time (HH:MM): ")
    examRoom = input("Enter Room: ")

    # Check for conflicting schedule (same date & time, and room)
    for exam in existingExams:
        if (exam['date'] == examDate and 
            exam['time'] == examTime and 
            exam['room'].lower() == examRoom.lower()):
            print("⛔ Conflict detected! Another exam is already scheduled in that room at that time.")
            return

    existingExams.append({
        "name": examName,
        "date": examDate,
        "time": examTime,
        "room": examRoom
    })
    # Notify the user that the exam has been added
    print("✅ Exam added successfully.")

def viewExams():
    if not existingExams:
    # check if there are no exams and will notify the user
        print("⚠️ No exams scheduled.")
        return
    #Loop to print the exams 
    print("\n📅 Exam Schedule:")
    #used enumerate so I can use the 2 vars using a 1 liner
    for i, exam in enumerate(existingExams):
        print(f"{i + 1}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")

def editExam():
#fist show the existing exams then ask for the exam number to modify
    viewExams()
    try:
        #try block for validation and error handling
        index = int(input("Enter the exam number to edit: ")) - 1
        #minus 1 to get the index
        if 0 <= index < len(existingExams):
        #shorthand without using "and", if true print and get modifications from user
            existingExams[index]["name"] = input("New Exam Name: ")
            existingExams[index]["date"] = input("New Date (YYYY-MM-DD): ")
            existingExams[index]["time"] = input("New Time (HH:MM): ")
            existingExams[index]["room"] = input("New Room: ")
            print("✏️ Exam updated successfully.")
        else:
            print("❌ Invalid exam number.")
    except ValueError:
        #ValueError to catch invalid input when converting user input to an integer.
        print("❌ Invalid input.")
    
def deleteExam():
#delete exams from the list using pop
    viewExams()
    try:
        index = int(input("Enter the exam number to delete: ")) - 1
        if 0 <= index < len(existingExams):
            removed = existingExams.pop(index)
            print(f"🗑️ Removed: {removed['name']}")
        else:
            print("❌ Invalid exam number.")
    except ValueError:
        print("❌ Invalid input.")
        
#helper function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
        
# Main loop
while True:
    displayMenu()
    choice = input("Choose an option (1–6): ")
    if choice == '1':
        addExam()
    elif choice == '2':
        viewExams()
    elif choice == '3':
        editExam()
    elif choice == '4':
        deleteExam()
    elif choice == '5':
        clear_terminal()
    elif choice == '6':
        print("👋 Exiting Smart Scheduler. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")



