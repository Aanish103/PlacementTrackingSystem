from modules import data_store as ds

def add_placement_staff():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    role = input("Role: ")
    sid = ds.add_staff(name, email, phone, role)
    print(f"Placement Staff added. staff_id: {sid}")


def update_placement_staff():
    sid = input("Enter staff_id to update: ")
    s = ds.get_by_id(ds.placement_staffs, sid)
    if not s:
        print("staff_id not found.")
        return
    data = {}
    name = input(f"Name [{s['name']}]: ").strip()
    if name: data["name"] = name
    email = input(f"Email [{s['email']}]: ").strip()
    if email: data["email"] = email
    phone = input(f"Phone [{s['phone']}]: ").strip()
    if phone: data["phone"] = phone
    role = input(f"Role [{s['role']}]: ").strip()
    if role: data["role"] = role
    if ds.update_staff(sid, data):
        print("Staff updated.")
    else:
        print("Update failed.")



def delete_placement_staff():
    sid = input("Enter staff_id to delete: ")
    if ds.delete_staff(sid):
        print("Staff deleted.")
    else:
        print("staff_id not found.")


def show_all_placement_staffs():
    for s in ds.list_staffs():
        print(s)