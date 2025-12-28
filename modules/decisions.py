from datetime import date
import modules.data_store as ds


def approve_application():
    aid = input("Application ID: ")
    comment = input("Comment: ")
    d = input("Decision date (DD/MM/YYYY) [blank for today]: ")

    decision_date = d if d else date.today().strftime("%d/%m/%Y")

    ds.add_decision(
        app_id=aid,
        d_type="Approved",
        by="System",
        comment=comment,
        date=decision_date
    )

    print("Application approved successfully")


def reject_application():
    aid = input("Application ID: ")
    comment = input("Comment: ")
    d = input("Decision date (DD/MM/YYYY) [blank for today]: ")

    decision_date = d if d else date.today().strftime("%d/%m/%Y")

    ds.add_decision(
        app_id=aid,
        d_type="Rejected",
        by="System",
        comment=comment,
        date=decision_date
    )

    print("Application rejected successfully")


def withdraw_application():
    aid = input("Application ID: ")
    comment = input("Comment: ")
    d = input("Decision date (DD/MM/YYYY) [blank for today]: ")

    decision_date = d if d else date.today().strftime("%d/%m/%Y")

    ds.add_decision(
        app_id=aid,
        d_type="Withdrawn",
        by="System",
        comment=comment,
        date=decision_date
    )

    print("Application withdrawn successfully")

def show_all_decisions():
    if not ds.decisions:
        print("No decisions available.")
        return

    print("\nALL DECISIONS")
    print("=" * 80)

    for d in ds.decisions:
        app = ds.get_by_id(ds.applications, d["application_id"])
        student = ds.get_by_id(ds.students, app["student_id"]) if app else None

        print(f"Application ID : {d['application_id']}")
        print(f"Student Name  : {student['name'] if student else 'N/A'}")
        print(f"Decision Type : {d['decision_type']}")
        print(f"Decision By   : {d['decision_by']}")
        print(f"Comment       : {d['decision_comment']}")
        print(f"Decision Date : {d['decision_date']}")
        print("-" * 80)