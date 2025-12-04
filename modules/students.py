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