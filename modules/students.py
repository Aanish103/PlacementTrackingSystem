from modules import data_store as ds

def add_student():
    name = input("Name: ")
    dob = input("DOB (DD/MM/YYYY): ")
    address = input("Address: ")
    qualification = input("Highest qualification: ")
    graduation_year = int(input("Graduation year: "))
    school_id = input("School ID: ")
    staff_id = input("Staff ID: ")
    sid = ds.add_student(name, dob, address, qualification, graduation_year, school_id, staff_id)
    print(f"Student added. student_id: {sid}")


def update_student():
    sid = input("Enter student_id: ")
    s = ds.get_by_id(ds.students, sid)
    if not s:
        print("student_id not found.")
        return
    data = {}
    name = input(f"Name [{s['name']}]: ").strip()
    if name: data["name"] = name
    dob = input(f"DOB [{s['dob']}]: ").strip()
    if dob: data["dob"] = dob
    address = input(f"Address [{s['address']}]: ").strip()
    if address: data["address"] = address
    qualification = input(f"Qualification [{s['qualification']}]: ").strip()
    if qualification: data["qualification"] = qualification
    graduation_year = input(f"Graduation Year [{s['grad_year']}]: ").strip()
    if graduation_year: data["grad_year"] = int(graduation_year)
    school_id = input(f"School ID [{s['school_id']}]: ").strip()
    if school_id: data["school_id"] = school_id
    staff_id = input(f"Staff ID [{s['staff_id']}]: ").strip()
    if staff_id: data["staff_id"] = staff_id
    if ds.update_student(sid, data):
        print("Student updated.")
    else:
        print("Update failed.")


def delete_student():
    sid = input("Enter student_id to delete: ")
    if ds.delete_student(sid):
        print("Student and related records deleted.")
    else:
        print("student_id not found.")


def filter_students_by_graduation_year():
    year = input("Enter Graduation Year (e.g. 2024): ").strip()

    if not year.isdigit():
        print("Invalid year. Please enter a numeric year.")
        return

    year = int(year)
    found = False

    print(f"\nStudents graduating in {year}")
    print("-" * 70)

    for student in ds.students:
        if student["grad_year"] == year:
            found = True
            print(f"Student ID     : {student['student_id']}")
            print(f"Name           : {student['name']}")
            print(f"DOB            : {student['dob']}")
            print(f"Address        : {student['address']}")
            print(f"Qualification  : {student['qualification']}")
            print(f"School ID      : {student['school_id']}")
            print(f"Staff ID       : {student['staff_id']}")
            print("-" * 70)

    if not found:
        print("No students found for this graduation year.")