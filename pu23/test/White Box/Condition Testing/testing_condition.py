import unittest
import sys
import os


CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


class TestConditionTesting(unittest.TestCase):

    def setUp(self):
        self.school_backup = list(data_store.schools)
        self.application_backup = list(data_store.applications)

    def tearDown(self):
        data_store.schools.clear()
        data_store.schools.extend(self.school_backup)

        data_store.applications.clear()
        data_store.applications.extend(self.application_backup)

    # CONDITION TESTING – update_school


    # Condition TRUE (school exists)
    def test_update_school_condition_true(self):
        result = data_store.update_school(
            "SC001",
            {"location": "Chennai"}
        )
        self.assertTrue(result)

    # Condition FALSE (school does not exist)
    def test_update_school_condition_false(self):
        result = data_store.update_school(
            "INVALID",
            {"location": "Unknown"}
        )
        self.assertFalse(result)

    # CONDITION TESTING – update_application


    # Condition TRUE (application exists)
    def test_update_application_condition_true(self):
        result = data_store.update_application(
            "AP001",
            {"status": "Approved"}
        )
        self.assertTrue(result)

    # Condition FALSE (application does not exist)
    def test_update_application_condition_false(self):
        result = data_store.update_application(
            "INVALID",
            {"status": "Rejected"}
        )
        self.assertFalse(result)


    # Condition TRUE (school exists)
    def test_delete_school_condition_true(self):
        result = data_store.delete_school("SC001")
        self.assertTrue(result)

    # Condition FALSE (school does not exist)
    def test_delete_school_condition_false(self):
        result = data_store.delete_school("INVALID")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
