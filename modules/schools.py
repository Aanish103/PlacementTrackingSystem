from modules import data_store as ds

def add_school():
    name = input("School name: ")
    location = input("Location: ")
    sid = ds.add_school(name, location)
    print(f"School added. school_id: {sid}")

def update_school():
    sid = input("Enter school_id: ")
    s = ds.get_by_id(ds.schools, sid)
    if not s:
        print("school_id not found.")
        return
    data = {}
    name = input(f"Name [{s['school_name']}]: ").strip()
    if name: data["school_name"] = name
    location = input(f"Location [{s['location']}]: ").strip()
    if location: data["location"] = location
    if ds.update_school(sid, data):
        print("School updated.")
    else:
        print("Update failed.")