import unittest
import sys
import os


CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


class TestBranchCoverageSchool(unittest.TestCase):

    def setUp(self):
        self.school_backup = list(data_store.schools)

    def tearDown(self):
        data_store.schools.clear()
        data_store.schools.extend(self.school_backup)

    # ADD SCHOOL - VALID BRANCH

    def test_add_school_valid(self):
        school_id = data_store.add_school("Engineering College", "Chennai")
        self.assertIsNotNone(school_id)

    # ADD SCHOOL - INVALID (EMPTY VALUES)

    def test_add_school_invalid(self):
        school_id = data_store.add_school("", "")
        self.assertIsNotNone(school_id)


    # UPDATE SCHOOL - VALID BRANCH

    def test_update_school_valid(self):
        result = data_store.update_school(
            "SC001",
            {"location": "Bangalore"}
        )
        self.assertTrue(result)


    def test_update_school_invalid(self):
        result = data_store.update_school(
            "INVALID",
            {"location": "Unknown"}
        )
        self.assertFalse(result)


    def test_delete_school_valid(self):
        school_id = data_store.add_school("Law College", "Delhi")
        result = data_store.delete_school(school_id)
        self.assertTrue(result)


    # DELETE SCHOOL - INVALID BRANCH

    def test_delete_school_invalid(self):
        result = data_store.delete_school("INVALID")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
