from modules import data_store as ds

def add_assessment():
    application_id = input("Application ID: ")
    if not ds.get_by_id(ds.applications, application_id):
        print("application_id not found. - assessments.py:6")
        return
    assessor = input("Assessor name: ")
    score = int(input("Score (0-100): "))
    comments = input("Comments: ")
    aid = ds.add_assessment(application_id, assessor, score, comments)
    print(f"Assessment added. assessment_id: {aid} - assessments.py:12")


def update_assessment():
    aid = input("Assessment ID: ").strip()

    a = ds.get_by_id(ds.assessments, aid)
    if not a:
        print("Assessment not found. - assessments.py:20")
        return

    data = {}

    assessor = input(f"Assessor Name [{a['assessor_name']}]: ").strip()
    if assessor:
        data["assessor_name"] = assessor

    score = input(f"Score [{a['score']}]: ").strip()
    if score:
        try:
            data["score"] = int(score)
        except ValueError:
            print("Score must be a number. - assessments.py:34")
            return

    comments = input(f"Comments [{a['comments']}]: ").strip()
    if comments:
        data["comments"] = comments

    if a.update(data) is None:
        print("Assessment updated successfully. - assessments.py:42")


def delete_assessment():
    aid = input("Assessment ID to delete: ")
    if ds.delete_assessment(aid):
        print("Assessment deleted. - assessments.py:48")
    else:
        print("assessment_id not found. - assessments.py:50")


def show_all_assessments():
    for a in ds.list_assessments():
        print(a)


def search_assessments_by_application():
    aid = input("Application ID: ")
    res = ds.get_assessments_by_application(aid)
    if not res:
        print("No assessments for this application.")
    else:
        for r in res:
            print(r)