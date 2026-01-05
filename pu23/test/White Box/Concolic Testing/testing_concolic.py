import unittest
import sys
import os


CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


class TestConcolicUpdateSchool(unittest.TestCase):

    def setUp(self):
        # backup schools
        self.school_backup = list(data_store.schools)

    def tearDown(self):
        # restore schools
        data_store.schools.clear()
        data_store.schools.extend(self.school_backup)

    # CONCOLIC PATH 1: VALID SCHOOL ID

    def test_update_school_valid(self):
        result = data_store.update_school(
            "SC001",
            {"location": "Chennai"}
        )
        self.assertTrue(result)


    # CONCOLIC PATH 2: INVALID SCHOOL ID

    def test_update_school_invalid(self):
        result = data_store.update_school(
            "INVALID_ID",
            {"location": "Unknown"}
        )
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
