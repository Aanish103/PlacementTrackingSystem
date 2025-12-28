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


def show_applications_by_student():
    student_id = input("Enter student_id: ").strip()

    if not ds.get_by_id(ds.students, student_id):
        print("student_id not found.")
        return

    found = False
    print(f"\nApplications for Student ID: {student_id}")
    print("" * 60)

    for app in ds.applications:
        if app["student_id"] == student_id:
            found = True
            print(f"Application ID : {app['application_id']}")
            print(f"Employer       : {app['employer']}")
            print(f"Role           : {app['role']}")
            print(f"Start Date     : {app['start_date']}")
            print(f"End Date       : {app['end_date']}")
            print(f"Status         : {app['status']}")
            print(f"Documents      : {', '.join(app['documents']) if app['documents'] else 'None'}")
            print("" * 60)

    if not found:
        print("No applications found for this student.")

def show_all_applications():
    if not ds.applications:
        print("No applications available.")
        return

    print("\nAll Applications")
    print("=" * 80)

    for app in ds.applications:
        student = ds.get_by_id(ds.students, app["student_id"])
        school = ds.get_by_id(ds.schools, student["school_id"]) if student else None

        print(f"Application ID : {app['application_id']}")
        print(f"Student ID     : {app['student_id']}")
        print(f"Student Name   : {student['name'] if student else 'N/A'}")
        print(f"School         : {school['school_name'] if school else 'N/A'}")
        print(f"Employer       : {app['employer']}")
        print(f"Role           : {app['role']}")
        print(f"Start Date     : {app['start_date']}")
        print(f"End Date       : {app['end_date']}")
        print(f"Status         : {app['status']}")
        print(f"Documents      : {', '.join(app['documents']) if app['documents'] else 'None'}")
        print("-" * 80)

def find_application_by_id():
    app_id = input("Enter application_id (e.g. AP001): ").strip()

    app = ds.get_by_id(ds.applications, app_id)
    if not app:
        print("application_id not found. - applications.py")
        return

    student = ds.get_by_id(ds.students, app["student_id"])
    school = ds.get_by_id(ds.schools, student["school_id"]) if student else None

    print("\nApplication Details")
    print("=" * 80)
    print(f"Application ID : {app['application_id']}")
    print(f"Student ID     : {app['student_id']}")
    print(f"Student Name   : {student['name'] if student else 'N/A'}")
    print(f"School         : {school['school_name'] if school else 'N/A'}")
    print(f"Employer       : {app['employer']}")
    print(f"Role           : {app['role']}")
    print(f"Start Date     : {app['start_date']}")
    print(f"End Date       : {app['end_date']}")
    print(f"Status         : {app['status']}")
    print(f"Documents      : {', '.join(app['documents']) if app['documents'] else 'None'}")
    print("=" * 80)

def show_full_application_details():
    aid = input("Enter application_id: ").strip()

    app = ds.get_by_id(ds.applications, aid)
    if not app:
        print("application_id not found. - applications.py")
        return

    student = ds.get_by_id(ds.students, app["student_id"])
    school = ds.get_by_id(ds.schools, student["school_id"]) if student else None

    print("\nAPPLICATION DETAILS")
    print("=" * 80)
    print(f"Application ID : {app['application_id']}")
    print(f"Employer       : {app['employer']}")
    print(f"Role           : {app['role']}")
    print(f"Start Date     : {app['start_date']}")
    print(f"End Date       : {app['end_date']}")
    print(f"Status         : {app['status']}")
    print(f"Documents      : {', '.join(app['documents']) if app['documents'] else 'None'}")

    if student:
        print("\nSTUDENT DETAILS")
        print("-" * 80)
        print(f"Student ID     : {student['student_id']}")
        print(f"Name           : {student['name']}")
        print(f"DOB            : {student['dob']}")
        print(f"Address        : {student['address']}")
        print(f"Qualification  : {student['qualification']}")
        print(f"Graduation Year: {student['grad_year']}")

    if school:
        print("\nSCHOOL DETAILS")
        print("-" * 80)
        print(f"School Name    : {school['school_name']}")
        print(f"Location       : {school['location']}")

    print("\nASSESSMENTS")
    print("-" * 80)
    found = False
    for ass in ds.assessments:
        if ass["application_id"] == aid:
            found = True
            print(f"Assessment ID  : {ass['assessment_id']}")
            print(f"Assessor Name : {ass['assessor_name']}")
            print(f"Score          : {ass['score']}")
            print(f"Comments       : {ass['comments']}")
            print("-" * 80)

    if not found:
        print("No assessments found for this application.")

    print("\nVISITS")
    print("-" * 80)
    found = False
    for v in ds.visits:
        if v["application_id"] == aid:
            found = True
            print(f"Visit ID       : {v['visit_id']}")
            print(f"Visitor Name  : {v['visitor_name']}")
            print(f"Visit Date    : {v['visit_date']}")
            print(f"Outcome       : {v['outcome']}")
            print(f"Notes         : {v['notes']}")
            print("-" * 80)

    if not found:
        print("No visits found for this application.")

    print("\nDECISIONS")
    print("-" * 80)
    decision_found = False
    for d in ds.decisions:
        if d["application_id"] == aid:
            decision_found = True
            print(f"Decision Type : {d['decision_type']}")
            print(f"Decision By   : {d['decision_by']}")
            print(f"Comment       : {d['decision_comment']}")
            print(f"Decision Date : {d['decision_date']}")
            print("-" * 80)

    if not decision_found:
        print("No decisions recorded for this application.")

    print("=" * 80)