from modules import data_store as ds

def add_school():
    name = input("School name: ")
    location = input("Location: ")
    sid = ds.add_school(name, location)
    print(f"School added. school_id: {sid}")