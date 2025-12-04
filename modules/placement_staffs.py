from modules import data_store as ds

def add_placement_staff():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    role = input("Role: ")
    sid = ds.add_staff(name, email, phone, role)
    print(f"Placement Staff added. staff_id: {sid}")