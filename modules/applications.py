# modules/applications.py
from modules import data_store as ds

def add_application():
    student_id = input("Student ID: ")
    if not ds.get_student(student_id):
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