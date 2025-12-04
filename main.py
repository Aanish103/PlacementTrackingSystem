from modules import placement_staffs
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


        return
    else:
        print("Invalid")


if __name__ == "__main__":
    main_menu()