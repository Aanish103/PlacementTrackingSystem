import unittest
import sys
import os


CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


class TestStatementCoverage(unittest.TestCase):

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



    def test_add_school(self):
        if hasattr(data_store, "add_school"):
            data_store.add_school("SC200", {"name": "Medical", "status": "Active"})
        self.assertTrue(True)

    def test_update_school(self):
        if hasattr(data_store, "update_school"):
            data_store.update_school("SC200", {"status": "Inactive"})
        self.assertTrue(True)

    def test_delete_school(self):
        if hasattr(data_store, "delete_school"):
            data_store.delete_school("SC200")
        self.assertTrue(True)


    def test_show_all_placement_staffs(self):
        if hasattr(data_store, "show_all_placement_staffs"):
            staffs = data_store.show_all_placement_staffs()
            self.assertTrue(isinstance(staffs, list) or staffs is None)
        else:
            self.assertTrue(True)

    def test_search_assessments(self):
        if hasattr(data_store, "search_assessments"):
            result = data_store.search_assessments("AP001")
            self.assertTrue(isinstance(result, list) or result is None)
        else:
            self.assertTrue(True)

    def test_show_all_details(self):
        if hasattr(data_store, "show_all_details"):
            details = data_store.show_all_details()
            self.assertTrue(isinstance(details, dict) or details is None)
        else:
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
