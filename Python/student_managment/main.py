from student import (
    add_student,
    view_students,
    update_student,
    delete_student
)

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        course = input("Enter Course: ")
        add_student(name, email, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = input("Enter Student ID: ")
        name = input("Enter New Name: ")
        email = input("Enter New Email: ")
        course = input("Enter New Course: ")
        update_student(student_id, name, email, course)

    elif choice == "4":
        student_id = input("Enter Student ID: ")
        delete_student(student_id)

    elif choice == "5":
        print("👋 Exiting program. Thank you!")
        break

    else:
        print("❌ Invalid choice. Try again.")
