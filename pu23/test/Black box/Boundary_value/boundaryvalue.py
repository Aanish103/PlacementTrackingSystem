import unittest
import sys
import os

CURRENT_DIR = os.path.dirname(__file__)
PU23_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_PATH)

from modules import data_store



class TestBoundaryValueAnalysis(unittest.TestCase):



    def setUp(self):
        self.schools_backup = list(data_store.schools)
        self.applications_backup = list(data_store.applications)
        self.assessments_backup = list(data_store.assessments)
        self.staff_backup = list(data_store.placement_staffs)

    def tearDown(self):
        data_store.schools.clear()
        data_store.schools.extend(self.schools_backup)

        data_store.applications.clear()
        data_store.applications.extend(self.applications_backup)

        data_store.assessments.clear()
        data_store.assessments.extend(self.assessments_backup)

        data_store.placement_staffs.clear()
        data_store.placement_staffs.extend(self.staff_backup)


    # SPRINT 1 – SCHOOL (Boundary Value Analysis)


    def test_add_school_min_boundary(self):
        sid = data_store.add_school("A", "X")
        self.assertIsNotNone(sid)

    def test_add_school_max_boundary(self):
        sid = data_store.add_school("A" * 100, "L" * 100)
        self.assertIsNotNone(sid)

    def test_update_school_valid_id(self):
        self.assertTrue(data_store.update_school("SC001", {"location": "Delhi"}))

    def test_update_school_invalid_id(self):
        self.assertFalse(data_store.update_school("SC999", {"location": "Delhi"}))

    def test_delete_school_valid(self):
        self.assertTrue(data_store.delete_school("SC001"))

    def test_delete_school_invalid(self):
        self.assertFalse(data_store.delete_school("SC999"))


    # SPRINT 2 – APPLICATION STATUS (Boundary Values)


    def test_approve_application(self):
        self.assertTrue(
            data_store.update_application("AP001", {"status": "Approved"})
        )

    def test_reject_application(self):
        self.assertTrue(
            data_store.update_application("AP002", {"status": "Rejected"})
        )

    def test_withdraw_application(self):
        self.assertTrue(
            data_store.update_application("AP003", {"status": "Withdrawn"})
        )

    def test_update_application_invalid(self):
        self.assertFalse(
            data_store.update_application("AP999", {"status": "Approved"})
        )

    # ==================================================
    # SPRINT 3 – VIEW & SEARCH (Boundary Values)
    # ==================================================

    def test_show_all_placement_staffs(self):
        staffs = data_store.list_staffs()
        self.assertGreaterEqual(len(staffs), 1)

    def test_search_assessments_valid(self):
        result = data_store.get_assessments_by_application("AP001")
        self.assertIsInstance(result, list)

    def test_search_assessments_invalid(self):
        result = data_store.get_assessments_by_application("AP999")
        self.assertEqual(result, [])

    def test_show_all_details(self):
        details = data_store.show_all_details()
        self.assertIn("schools", details)
        self.assertIn("applications", details)
        self.assertIn("assessments", details)


if __name__ == "__main__":
    unittest.main()
