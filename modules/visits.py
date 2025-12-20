from modules import data_store as ds


def add_visit():
    application_id = input("Application ID: ").strip()

    if not ds.get_by_id(ds.applications, application_id):
        print("application_id not found. Create application first. - visits.py:8")
        return

    visitor_name = input("Visitor Name: ").strip()
    visit_date = input("Visit Date (DD/MM/YYYY): ").strip()
    outcome = input("Outcome: ").strip()
    notes = input("Notes: ").strip()

    vid = ds.add_visit(application_id, visitor_name, visit_date, outcome, notes)
    print(f"Visit recorded successfully. visit_id: {vid} ")