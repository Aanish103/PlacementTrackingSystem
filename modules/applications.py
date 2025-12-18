# modules/applications.py
from modules import data_store as ds

def add_application():
    student_id = input("Student ID: ")
    if not ds.get_by_id(ds.students, student_id):
        print("student_id not found. Create student first.")
        return
    employer = input("Employer name: ")
    job_role = input("Job role: ")
    start_date = input("Start date (DD/MM/YYYY): ")
    end_date = input("End date (DD/MM/YYYY): ")
    docs = input("Documents (comma separated filenames): ").strip()
    docs_list = [d.strip() for d in docs.split(",")] if docs else []
    aid = ds.add_application(student_id, employer, job_role, start_date, end_date, docs_list)
    print(f"Application created. application_id: {aid}")


def update_application():
    aid = input("Enter application_id: ").strip()
    a = ds.get_by_id(ds.applications, aid)
    if not a:
        print("application_id not found.")
        return

    data = {}

    employer = input(f"Employer [{a['employer']}]: ").strip()
    if employer:
        data["employer"] = employer

    role = input(f"Job Role [{a['role']}]: ").strip()
    if role:
        data["role"] = role

    start = input(f"Start Date [{a['start_date']}]: ").strip()
    if start:
        data["start_date"] = start

    end = input(f"End Date [{a['end_date']}]: ").strip()
    if end:
        data["end_date"] = end

    docs = input("Documents (comma separated - leave blank to keep existing): ").strip()
    if docs:
        data["documents"] = [d.strip() for d in docs.split(",")]

    status = input(f"Status [{a['status']}]: ").strip()
    if status:
        data["status"] = status

    if ds.update_application(aid, data):
        print("Application updated successfully.")
    else:
        print("Update failed.")


def delete_application():
    aid = input("Enter application_id to delete: ")
    if ds.delete_application(aid):
        print("Application and related records deleted.")
    else:
        print("application_id not found.")