from database.sqlite_db import init_db
from business import logic

def main():
    init_db()
    print("Welcome to Student Course Management System")
    
    while True:
        print("\nOptions:\n1. Add Student\n2. Add Course\n3. Enroll Student\n4. View Enrollments\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            logic.register_student(name, email)
        elif choice == '2':
            name = input("Enter course name: ")
            description = input("Enter course description: ")
            logic.create_course(name, description)
        elif choice == '3':
            student_name = input("Enter student name: ")
            course_name = input("Enter course name: ")
            logic.enroll(student_name, course_name)
        elif choice == '4':
            enrollments = logic.view_enrollments()
            for student_name, course_name in enrollments:
                print(f"{student_name} enrolled in {course_name}")
        elif choice == '5':
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
