students = {}
def calculate_result(marks):
    total = sum(marks.values())
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    subjects = int(input("Enter Number of Subjects: "))
    marks = {}

    for i in range(subjects):
        subject = input(f"Enter Subject {i+1} Name: ")
        score = float(input(f"Enter Marks in {subject}: "))
        marks[subject] = score

    total, percentage, grade = calculate_result(marks)

    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    print("Student Record Added Successfully!")


def display_all():
    if not students:
        print("No records found!")
        return

    for roll, data in students.items():
        print("\n----------------------------")
        print("Roll Number :", roll)
        print("Name        :", data["name"])
        print("Marks       :", data["marks"])
        print("Total       :", data["total"])
        print("Percentage  :", round(data["percentage"], 2), "%")
        print("Grade       :", data["grade"])
        print("----------------------------")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        data = students[roll]
        print("\nStudent Found")
        print("Name        :", data["name"])
        print("Marks       :", data["marks"])
        print("Total       :", data["total"])
        print("Percentage  :", round(data["percentage"], 2), "%")
        print("Grade       :", data["grade"])
    else:
        print("Student not found!")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    if roll not in students:
        print("Student not found!")
        return

    print("Enter New Details")

    name = input("Enter Student Name: ")
    subjects = int(input("Enter Number of Subjects: "))
    marks = {}

    for i in range(subjects):
        subject = input(f"Enter Subject {i+1} Name: ")
        score = float(input(f"Enter Marks in {subject}: "))
        marks[subject] = score

    total, percentage, grade = calculate_result(marks)

    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    print("Record Updated Successfully!")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("Record Deleted Successfully!")
    else:
        print("Student not found!")

while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try Again.")

