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