import unittest
import sys
import os


CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


class TestBlackBoxEquivalencePartition(unittest.TestCase):

    def setUp(self):
        self.schools_backup = list(data_store.schools)
        self.applications_backup = list(data_store.applications)
        self.assessments_backup = list(data_store.assessments)

    def tearDown(self):
        data_store.schools.clear()
        data_store.schools.extend(self.schools_backup)

        data_store.applications.clear()
        data_store.applications.extend(self.applications_backup)

        data_store.assessments.clear()
        data_store.assessments.extend(self.assessments_backup)

    # ------------------ Sprint 1 ------------------

    def test_add_school_valid(self):
        sid = data_store.add_school("Engineering", "Chennai")
        self.assertIsNotNone(sid)

    def test_update_school_valid(self):
        self.assertTrue(data_store.update_school("SC001", {"location": "Bangalore"}))

    def test_delete_school_valid(self):
        self.assertTrue(data_store.delete_school("SC001"))

    # ------------------ Sprint 2 ------------------

    def test_approve_application(self):
        self.assertTrue(data_store.update_application("AP001", {"status": "Approved"}))

    def test_reject_application(self):
        self.assertTrue(data_store.update_application("AP002", {"status": "Rejected"}))

    def test_withdraw_application(self):
        self.assertTrue(data_store.update_application("AP003", {"status": "Withdrawn"}))

    # ------------------ Sprint 3 ------------------

    def test_search_assessment_valid(self):
        result = data_store.get_assessments_by_application("AP001")
        self.assertIsInstance(result, list)

    def test_show_all_details(self):
        details = data_store.show_all_details()
        self.assertIn("schools", details)
        self.assertIn("applications", details)
        self.assertIn("assessments", details)


if __name__ == "__main__":
    unittest.main()
