from modules import placement_staffs, schools, students, applications, assessments, visits
from modules import data_store as ds

def main_menu():
    while True:
        print("\n=== Placement Tracking Tool - Console ===")
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
        elif choice == "10":
            visits_menu()
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
    elif c == "0":
        return
    else:
        print("Invalid.")


def applications_menu():
    print("\nApplication: 1 Add | 2 Update | 3 Delete | 4 Show All | 5 Find by ID | 6 Show Full Details | 0 Back")
    c = input("Sub choice: ").strip()
    if c == "1":
        applications.add_application()
    elif c == "2":
        applications.update_application()
    elif c == "3":
        applications.delete_application()
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
    elif c == "0":
        return
    else:
        print("Invalid.")

def visits_menu():
    print("\nVisits: 1 Add | 2 Update | 3 Delete | 0 Back ")
    c = input("Sub choice: ").strip()

    if c == "1":
        visits.add_visit()
    elif c == "2":
        visits.update_visit()
    elif c == "0":
        return
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_menu()