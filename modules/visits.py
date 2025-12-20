from modules import data_store as ds


def add_visit():
    application_id = input("Application ID: ").strip()

    if not ds.get_by_id(ds.applications, application_id):
        print("application_id not found. Create application first.")
        return

    visitor_name = input("Visitor Name: ").strip()
    visit_date = input("Visit Date (DD/MM/YYYY): ").strip()
    outcome = input("Outcome: ").strip()
    notes = input("Notes: ").strip()

    vid = ds.add_visit(application_id, visitor_name, visit_date, outcome, notes)
    print(f"Visit recorded successfully. visit_id: {vid} ")


def update_visit():
    vid = input("Enter Visit ID: ").strip()
    v = ds.get_by_id(ds.visits, vid)

    if not v:
        print("Visit ID not found.")
        return

    data = {}

    visitor = input(f"Visitor Name [{v['visitor_name']}]: ").strip()
    if visitor:
        data["visitor_name"] = visitor

    visit_date = input(f"Visit Date [{v['visit_date']}]: ").strip()
    if visit_date:
        data["visit_date"] = visit_date

    outcome = input(f"Outcome [{v['outcome']}]: ").strip()
    if outcome:
        data["outcome"] = outcome

    notes = input(f"Notes [{v['notes']}]: ").strip()
    if notes:
        data["notes"] = notes

    if ds.update_visit(vid, data):
        print("Visit updated successfully.")
    else:
        print("Update failed.")

def delete_visit():
    vid = input("Enter Visit ID to delete: ").strip()

    if ds.delete_visit(vid):
        print("Visit deleted successfully.")
    else:
        print("Visit ID not found.")