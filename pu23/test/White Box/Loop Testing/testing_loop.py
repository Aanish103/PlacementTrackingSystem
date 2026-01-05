import unittest
import sys
import os


CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


class TestLoopTesting(unittest.TestCase):

    def setUp(self):
        self.school_backup = list(data_store.schools)
        self.application_backup = list(data_store.applications)

    def tearDown(self):
        data_store.schools.clear()
        data_store.schools.extend(self.school_backup)

        data_store.applications.clear()
        data_store.applications.extend(self.application_backup)

    # LOOP TESTING – update_school

    # Zero iterations (empty list)
    def test_update_school_zero_iteration(self):
        data_store.schools.clear()
        result = data_store.update_school("SC001", {"location": "Delhi"})
        self.assertFalse(result)

    # One iteration
    def test_update_school_one_iteration(self):
        data_store.schools.clear()
        data_store.schools.append(
            {"school_id": "SC001", "name": "Engineering", "status": "Active"}
        )
        result = data_store.update_school("SC001", {"status": "Inactive"})
        self.assertTrue(result)

    # Multiple iterations
    def test_update_school_multiple_iterations(self):
        result = data_store.update_school("SC002", {"location": "Mumbai"})
        self.assertTrue(result)

    # LOOP TESTING – update_application

    # Zero iterations
    def test_update_application_zero_iteration(self):
        data_store.applications.clear()
        result = data_store.update_application("AP001", {"status": "Approved"})
        self.assertFalse(result)

    # One iteration
    def test_update_application_one_iteration(self):
        data_store.applications.clear()
        data_store.applications.append(
            {"application_id": "AP001", "student": "John", "status": "Pending"}
        )
        result = data_store.update_application("AP001", {"status": "Approved"})
        self.assertTrue(result)

    # Multiple iterations
    def test_update_application_multiple_iterations(self):
        result = data_store.update_application("AP002", {"status": "Rejected"})
        self.assertTrue(result)

    # LOOP TESTING – delete_school

    # Zero iterations
    def test_delete_school_zero_iteration(self):
        data_store.schools.clear()
        result = data_store.delete_school("SC001")
        self.assertFalse(result)

    # One iteration
    def test_delete_school_one_iteration(self):
        data_store.schools.clear()
        data_store.schools.append(
            {"school_id": "SC005", "name": "Law", "status": "Active"}
        )
        result = data_store.delete_school("SC005")
        self.assertTrue(result)

    # Multiple iterations
    def test_delete_school_multiple_iterations(self):
        result = data_store.delete_school("SC003")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
