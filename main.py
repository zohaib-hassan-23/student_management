from student import insert_student, get_all_students, delete_student
from course import insert_course, get_all_courses, delete_course
from enrollment import enroll_student, get_enrollments
from grade import assign_grade, get_all_grades
from attendance import mark_attendance, get_all_attendance

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Add Course")
        print("5. View Courses")
        print("6. Delete Course")
        print("7. Enroll Student")
        print("8. View Enrollments")
        print("9. Assign Grade")
        print("10. View Grades")
        print("11. Mark Attendance")
        print("12. View Attendance")
        print("13. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            address = input("Enter address: ")
            insert_student(name, email, dob, address)
            print("\n Add Student Successfully \n")

        elif choice == "2":
            print("\n List of Students \n")
            for s in get_all_students():
                print(dict(s))

        elif choice == "3":
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
            print("\n Student Delete Successfully \n")

        elif choice == "4":
            cname = input("Enter course name: ")
            credits = input("Enter credit hours: ")
            insert_course(cname, credits)
            print("\n Add Course Successfully \n")

        elif choice == "5":
            print("\n List of add Courses \n")
            for c in get_all_courses():
                print(dict(c))

        elif choice == "6":
            course_id = input("Enter course ID to delete: ")
            delete_course(course_id)
            print(" \n Courses Delete Successfully \n ")

        elif choice == "7":
            sid = input("Enter student ID: ")
            cid = input("Enter course ID: ")
            enroll_student(sid, cid)
            print("\n Enroll Student Successfully \n" )

        elif choice == "8":
            print("\n List of enrolled Students \n")
            for e in get_enrollments():
                print(dict(e))

        elif choice == "9":
            sid = input("Enter student ID: ")
            cid = input("Enter course ID: ")
            grade = input("Enter grade: ")
            assign_grade(sid, cid, grade)
            print("\n Assign Grade Successfully \n")

        elif choice == "10":
            print("\n List of Assign Graded Students \n")
            for g in get_all_grades():
                print(dict(g))

        elif choice == "11":
            sid = input("Enter student ID: ")
            cid = input("Enter course ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter status (Present/Absent/Late): ")
            mark_attendance(sid, cid, date, status)
            print("/n Mark Attendence Successfully")

        elif choice == "12":
            print("\n List of Attendance marked Students \n")
            for a in get_all_attendance():
                print(dict(a))

        elif choice == "13":
            print("Exiting...")
            print("\n Thank you \n")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
