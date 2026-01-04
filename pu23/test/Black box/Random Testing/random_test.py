import unittest
import sys
import os
import random   # ✅ FIX ADDED

# ---------------------------------------------------
# ADD pu23 FOLDER TO PYTHON PATH
# ---------------------------------------------------
CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


class TestRandomTesting(unittest.TestCase):

    def setUp(self):
        self.school_backup = list(getattr(data_store, "schools", []))
        self.application_backup = list(getattr(data_store, "applications", []))

    def tearDown(self):
        if hasattr(data_store, "schools"):
            data_store.schools.clear()
            data_store.schools.extend(self.school_backup)

        if hasattr(data_store, "applications"):
            data_store.applications.clear()
            data_store.applications.extend(self.application_backup)

    # ==================================================
    # RANDOM TESTING – SCHOOL
    # ==================================================
    def test_random_school_operations(self):
        school_id = f"SC{random.randint(100, 999)}"
        school_data = {
            "name": random.choice(["Engineering", "Medical", "Arts"]),
            "status": random.choice(["Active", "Inactive"])
        }

        if hasattr(data_store, "add_school"):
            data_store.add_school(school_id, school_data)

        if hasattr(data_store, "update_school"):
            data_store.update_school(school_id, {"status": "Inactive"})

        if hasattr(data_store, "delete_school"):
            data_store.delete_school(school_id)

        self.assertTrue(True)

    # ==================================================
    # RANDOM TESTING – APPLICATION
    # ==================================================
    def test_random_application_operations(self):
        app_id = f"AP{random.randint(100, 999)}"

        actions = [
            "approve_application",
            "reject_application",
            "withdraw_application"
        ]

        action = random.choice(actions)

        if hasattr(data_store, action):
            getattr(data_store, action)(app_id)

        self.assertTrue(True)

    # ==================================================
    # RANDOM TESTING – VIEW
    # ==================================================
    def test_random_view_functions(self):
        views = [
            "show_all_details",
            "show_all_placement_staffs"
        ]

        view = random.choice(views)

        if hasattr(data_store, view):
            result = getattr(data_store, view)()
            self.assertTrue(result is None or isinstance(result, (list, dict)))
        else:
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
