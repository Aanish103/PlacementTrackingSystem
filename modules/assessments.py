from modules import data_store as ds

def add_assessment():
    application_id = input("Application ID: ")
    if not ds.get_by_id(ds.applications, application_id):
        print("application_id not found.")
        return
    assessor = input("Assessor name: ")
    score = int(input("Score (0-100): "))
    comments = input("Comments: ")
    aid = ds.add_assessment(application_id, assessor, score, comments)
    print(f"Assessment added. assessment_id: {aid}")