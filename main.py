from modules import placement_staffs, schools, students, applications, assessments, visits, decisions
from modules import data_store as ds

def main_menu():
    while True:
        print("\n=== Placement Tracking Tool  Console ===")
        print("1  Placement Staffs")
        print("2  Schools")
        print("3  Students")
        print("4  Application")
        print("5  Assessments")
        print("6  Show All Applications for a Student")
        print("7  Filter Students by Graduation Year")
        print("8  Filter Students by School")
        print("9  Show All Details")
        print("10 Visits")
        print("11 Record Decisions")
        print("0  Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            placement_staffs_menu()
        elif choice == "2":
            schools_menu()
        elif choice == "3":
            students_menu()
        elif choice == "4":
            applications_menu()
        elif choice == "5":
            assessments_menu()
        elif choice == "6":
            applications.show_applications_by_student()
        elif choice == "7":
            students.filter_students_by_graduation_year()
        elif choice == "8":
            students.filter_students_by_school()
        elif choice == "10":
            visits_menu()
        elif choice == "11":
            decisions_menu()
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


def placement_staffs_menu():
    print("\nPlacement Staffs: 1 Add | 2 Update | 3 Delete | 4 Show All | 0 Back")
    c = input("Sub choice: ").strip()
    if c == "1":
        placement_staffs.add_placement_staff()
    elif c == "2":
        placement_staffs.update_placement_staff()
    elif c == "3":
        placement_staffs.delete_placement_staff()
    elif c == "4":
        placement_staffs.show_all_placement_staffs()
    elif c == "0":
        return
    else:
        print("Invalid")


def schools_menu():
    print("\nSchools: 1 Add | 2 Update | 3 Delete | 4 Show All | 0 Back")
    c = input("Sub choice: ").strip()
    if c == "1":
        schools.add_school()
    elif c == "2":
        schools.update_school()
    elif c == "3":
        schools.delete_school()
    elif c == "4":
        schools.show_all_schools()
    elif c == "0":
        return
    else:
        print("Invalid.")


def students_menu():
    print("\nStudents: 1 Add | 2 Update | 3 Delete | 4 Show All | 5 Find by ID | 6 Show Full Details | 0 Back")
    c = input("Sub choice: ").strip()
    if c == "1":
        students.add_student()
    elif c == "2":
        students.update_student()
    elif c == "3":
        students.delete_student()
    elif c == "5":
        students.find_student_by_id()
    elif c == "0":
        return
    else:
        print("Invalid.")


def applications_menu():
    print("\nApplication: 1 Add | 2 Update | 3 Delete | 4 Show All Applications | 5 Find by ID | 6 Show Full Details | 0 Back")
    c = input("Sub choice: ").strip()
    if c == "1":
        applications.add_application()
    elif c == "2":
        applications.update_application()
    elif c == "3":
        applications.delete_application()
    elif c == "4":
        applications.show_all_applications()
    elif c == "5":
        applications.find_application_by_id()
    elif c == "6":
        applications.show_full_application_details()
    elif c == "0":
        return
    else:
        print("Invalid.")


def assessments_menu():
    print("\nAssessments: 1 Add | 2 Update | 3 Delete | 4 Show All | 5 Search by Application ID | 0 Back")
    c = input("Sub choice: ").strip()
    if c == "1":
        assessments.add_assessment()
    elif c == "2":
        assessments.update_assessment()
    elif c == "3":
        assessments.delete_assessment()
    elif c == "4":
        assessments.show_all_assessments()
    elif c == "5":
        assessments.search_assessments_by_application()
    elif c == "0":
        return
    else:
        print("Invalid. - main.py:115")

def visits_menu():
    print("\nVisits: 1 Add | 2 Update | 3 Delete | 4 Show All | 0 Back")
    c = input("Sub choice: ").strip()

    if c == "1":
        visits.add_visit()
    elif c == "2":
        visits.update_visit()
    elif c == "3":
        visits.delete_visit()
    elif c == "0":
        return
    else:
        print("Invalid choice.")


def decisions_menu():
    print("\nDecisions: 1 Approve | 2 Reject | 3 Withdraw | 4 Show All | 0 Back")
    c = input("Sub choice: ").strip()
    if c == "1":
        decisions.approve_application()
    elif c == "2":
        decisions.reject_application()
    elif c == "3":
        decisions.withdraw_application()
    elif c == "0":
        return
    else:
        print("Invalid.")

if __name__ == "__main__":
    main_menu()