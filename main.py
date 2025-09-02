from db_init import init_db

from student import (
    insert_student, get_all_students, find_student_by_email,
    update_student, update_all_students,
    delete_student, delete_all_students
)
from course import (
    insert_course, get_all_courses, find_course_by_name,
    update_course, update_all_courses,
    delete_course, delete_all_courses
)
from enrollment import (
    insert_enrollment, get_all_enrollments, find_enrollments_by_student,
    update_enrollment, update_all_enrollments,
    delete_enrollment, delete_all_enrollments
)

from grade import (
    insert_grade, get_all_grades, find_grades_by_student,
    update_grade, update_all_grades,
    delete_grade, delete_all_grades
)
from attendance import (
    insert_attendance, get_all_attendance, find_attendance_by_student,
    update_attendance, update_all_attendance,
    delete_attendance, delete_all_attendance
)

def pause():
    input("\nPress Enter to continue...")

def print_rows(rows, title="Records"):
    print(f"\n-- {title} --")
    if not rows:
        print("(no rows)")
        return
    for r in rows:
        try:
            print(dict(r))
        except Exception:
            print(r)

def students_menu():
    while True:
        print("\n--- Students Menu ---")
        print("1) Add student")
        print("2) View all students")
        print("3) Search student by email")
        print("4) Update single student")
        print("5) Bulk update students")
        print("6) Delete single student")
        print("7) Delete ALL students")
        print("0) Back")
        ch = input("Choose: ").strip()

        if ch == "1":
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address (optional): ") or None
            dob = input("DOB YYYY-MM-DD (optional): ") or None
            print("Inserted." if insert_student(name, email, address, dob) else "Insert failed.")
            pause()

        elif ch == "2":
            print_rows(get_all_students(), "Students")
            pause()

        elif ch == "3":
            email = input("Email: ")
            row = find_student_by_email(email)
            print_rows([row] if row else [], "Search result")
            pause()

        elif ch == "4":
            sid = int(input("Student ID: "))
            name = input("New name (Enter to skip): ") or None
            email = input("New email (Enter to skip): ") or None
            address = input("New address (Enter to skip): ") or None
            dob = input("New DOB YYYY-MM-DD (Enter to skip): ") or None
            print("Updated." if update_student(sid, name, email, address, dob) else "Update failed.")
            pause()

        elif ch == "5":
            address = input("Set address for ALL (Enter to skip): ") or None
            dob = input("Set DOB YYYY-MM-DD for ALL (Enter to skip): ") or None
            print("Bulk updated." if update_all_students(address, dob) else "Bulk update failed.")
            pause()

        elif ch == "6":
            sid = int(input("Student ID: "))
            print("Deleted." if delete_student(sid) else "Delete failed.")
            pause()

        elif ch == "7":
            if input("Type 'YES' to delete ALL: ") == "YES":
                print("All deleted." if delete_all_students() else "Delete failed.")
            pause()

        elif ch == "0":
            return
        else:
            print("Invalid choice.")

def courses_menu():
    while True:
        print("\n--- Courses Menu ---")
        print("1) Add course")
        print("2) View all courses")
        print("3) Search course by name")
        print("4) Update single course")
        print("5) Bulk update courses")
        print("6) Delete single course")
        print("7) Delete ALL courses")
        print("0) Back")
        ch = input("Choose: ").strip()

        if ch == "1":
            name = input("Course name: ")
            chours = int(input("Credit hours: "))
            print("Inserted." if insert_course(name, chours) else "Insert failed.")
            pause()

        elif ch == "2":
            print_rows(get_all_courses(), "Courses")
            pause()

        elif ch == "3":
            q = input("Name contains: ")
            print_rows(find_course_by_name(q), "Search result")
            pause()

        elif ch == "4":
            cid = int(input("Course ID: "))
            name = input("New name (Enter to skip): ") or None
            chours = input("New credit hours (Enter to skip): ")
            chours = int(chours) if chours else None
            print("Updated." if update_course(cid, name, chours) else "Update failed.")
            pause()

        elif ch == "5":
            chours = input("Set credit hours for ALL (Enter to skip): ")
            chours = int(chours) if chours else None
            print("Bulk updated." if update_all_courses(chours) else "Bulk update failed.")
            pause()

        elif ch == "6":
            cid = int(input("Course ID: "))
            print("Deleted." if delete_course(cid) else "Delete failed.")
            pause()

        elif ch == "7":
            if input("Type 'YES' to delete ALL: ") == "YES":
                print("All deleted." if delete_all_courses() else "Delete failed.")
            pause()

        elif ch == "0":
            return
        else:
            print("Invalid choice.")

def enrollments_menu():
    while True:
        print("\n--- Enrollments Menu ---")
        print("1) Add enrollment")
        print("2) View all enrollments")
        print("3) Search enrollments by student_id")
        print("4) Update single enrollment")
        print("5) Bulk update enrollments")
        print("6) Delete single enrollment")
        print("7) Delete ALL enrollments")
        print("0) Back")
        ch = input("Choose: ").strip()

        if ch == "1":
            sid = int(input("Student ID: "))
            cid = int(input("Course ID: "))
            print(" Inserted." if insert_enrollment(sid, cid) else " Insert failed.")
            pause()

        elif ch == "2":
            print_rows(get_all_enrollments(), "Enrollments")
            pause()

        elif ch == "3":
            sid = int(input("Student ID: "))
            print_rows(find_enrollments_by_student(sid), "Search result")
            pause()

        elif ch == "4":
            eid = int(input("Enrollment ID: "))
            sid = input("New student_id (Enter to skip): ")
            cid = input("New course_id (Enter to skip): ")
            sid = int(sid) if sid else None
            cid = int(cid) if cid else None
            print("Updated." if update_enrollment(eid, sid, cid) else "Update failed.")
            pause()

        elif ch == "5":
            cid = input("Set course_id for ALL (Enter to skip): ")
            cid = int(cid) if cid else None
            print("Bulk updated." if update_all_enrollments(cid) else "Bulk update failed.")
            pause()

        elif ch == "6":
            eid = int(input("Enrollment ID: "))
            print("Deleted." if delete_enrollment(eid) else "Delete failed.")
            pause()

        elif ch == "7":
            if input("Type 'YES' to delete ALL: ") == "YES":
                print("All deleted." if delete_all_enrollments() else "Delete failed.")
            pause()

        elif ch == "0":
            return
        else:
            print("Invalid choice.")

def grades_menu():
    while True:
        print("\n--- Grades Menu ---")
        print("1) Add grade")
        print("2) View all grades")
        print("3) Search grades by student_id")
        print("4) Update single grade")
        print("5) Bulk update grades")
        print("6) Delete single grade")
        print("7) Delete ALL grades")
        print("0) Back")
        ch = input("Choose: ").strip()

        if ch == "1":
            sid = int(input("Student ID: "))
            cid = int(input("Course ID: "))
            g = input("Grade (e.g., A, B+): ")
            print("Inserted." if insert_grade(sid, cid, g) else "Insert failed.")
            pause()

        elif ch == "2":
            print_rows(get_all_grades(), "Grades")
            pause()

        elif ch == "3":
            sid = int(input("Student ID: "))
            print_rows(find_grades_by_student(sid), "Search result")
            pause()

        elif ch == "4":
            gid = int(input("Grade ID: "))
            g = input("New grade: ") or None
            print("Updated." if update_grade(gid, g) else "Update failed.")
            pause()

        elif ch == "5":
            g = input("Set grade for ALL: ") or None
            print("Bulk updated." if update_all_grades(g) else "Bulk update failed.")
            pause()

        elif ch == "6":
            gid = int(input("Grade ID: "))
            print("Deleted." if delete_grade(gid) else "Delete failed.")
            pause()

        elif ch == "7":
            if input("Type 'YES' to delete ALL: ") == "YES":
                print("All deleted." if delete_all_grades() else "Delete failed.")
            pause()

        elif ch == "0":
            return
        else:
            print("Invalid choice.")

def attendance_menu():
    while True:
        print("\n--- Attendance Menu ---")
        print("1) Add attendance")
        print("2) View all attendance")
        print("3) Search attendance by student_id")
        print("4) Update single attendance")
        print("5) Bulk update attendance")
        print("6) Delete single attendance")
        print("7) Delete ALL attendance")
        print("0) Back")
        ch = input("Choose: ").strip()

        if ch == "1":
            sid = int(input("Student ID: "))
            cid = int(input("Course ID: "))
            date = input("Date (YYYY-MM-DD): ")
            status = input("Status (Present/Absent/Late): ")
            print("Inserted." if insert_attendance(sid, cid, date, status) else "Insert failed.")
            pause()

        elif ch == "2":
            print_rows(get_all_attendance(), "Attendance")
            pause()

        elif ch == "3":
            sid = int(input("Student ID: "))
            print_rows(find_attendance_by_student(sid), "Search result")
            pause()

        elif ch == "4":
            aid = int(input("Attendance ID: "))
            status = input("New status (Present/Absent/Late, Enter to skip): ") or None
            date = input("New date YYYY-MM-DD (Enter to skip): ") or None
            print("Updated." if update_attendance(aid, status, date) else "Update failed.")
            pause()

        elif ch == "5":
            status = input("Set status for ALL (Present/Absent/Late, Enter to skip): ") or None
            print(" Bulk updated." if update_all_attendance(status) else " Bulk update failed.")
            pause()

        elif ch == "6":
            aid = int(input("Attendance ID: "))
            print("Deleted." if delete_attendance(aid) else " Delete failed.")
            pause()

        elif ch == "7":
            if input("Type 'YES' to delete ALL: ") == "YES":
                print("All deleted." if delete_all_attendance() else " Delete failed.")
            pause()

        elif ch == "0":
            return
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\n==== Student Management CLI ====")
        print("1) Initialize/Reset Database (DROP & CREATE)")
        print("2) Students")
        print("3) Courses")
        print("4) Enrollments")
        print("5) Grades")
        print("6) Attendance")
        print("0) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            init_db(); pause()
        elif choice == "2":
            students_menu()
        elif choice == "3":
            courses_menu()
        elif choice == "4":
            enrollments_menu()
        elif choice == "5":
            grades_menu()
        elif choice == "6":
            attendance_menu()
        elif choice == "0":
            print("Bye"); break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
