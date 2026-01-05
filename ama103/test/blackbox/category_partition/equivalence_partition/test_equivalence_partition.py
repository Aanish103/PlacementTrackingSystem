import unittest
import sys
import os

# --------------------------------------------------
# ADD PlacementTrackingSystem TO PYTHON PATH
# --------------------------------------------------
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../")
)
sys.path.insert(0, BASE_DIR)

# --------------------------------------------------
# IMPORT DATA STORE
# --------------------------------------------------
from modules import data_store


class TestBlackBoxEquivalencePartition(unittest.TestCase):

    def setUp(self):
        self.orig_schools = list(data_store.schools)
        self.orig_apps = list(data_store.applications)
        self.orig_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.schools.clear()
        data_store.schools.extend(self.orig_schools)

        data_store.applications.clear()
        data_store.applications.extend(self.orig_apps)

        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)

    # ---------------- SCHOOL ----------------
    def test_add_school_valid(self):
        sid = data_store.add_school("New School", "London")
        self.assertIsNotNone(sid)

    def test_add_school_invalid(self):
        sid = data_store.add_school("", "")
        self.assertIsNotNone(sid)   # black-box: still generates ID

    def test_update_school_valid(self):
        sid = data_store.add_school("Temp School", "York")
        result = data_store.update_school(sid, {"location": "Leeds"})
        self.assertTrue(result)

    def test_update_school_invalid(self):
        result = data_store.update_school("INVALID", {"location": "Leeds"})
        self.assertFalse(result)

    def test_delete_school_valid(self):
        sid = data_store.add_school("Delete School", "Oxford")
        result = data_store.delete_school(sid)
        self.assertTrue(result)

    # ---------------- APPLICATION ----------------
    def test_add_application_valid(self):
        aid = data_store.add_application(
            "ST001", "Google", "Intern",
            "2025-06-01", "2025-09-01", ["CV.pdf"]
        )
        self.assertIsNotNone(aid)

    def test_update_application_valid(self):
        result = data_store.update_application(
            "AP001", {"status": "Approved"}
        )
        self.assertTrue(result)

    def test_update_application_invalid(self):
        result = data_store.update_application(
            "INVALID", {"status": "Approved"}
        )
        self.assertFalse(result)

    # ---------------- ASSESSMENT ----------------
    def test_add_assessment_valid(self):
        aid = data_store.add_assessment(
            "AP001", "Dr Test", 80, "Good"
        )
        self.assertIsNotNone(aid)

    def test_get_assessment_invalid_application(self):
        result = data_store.get_assessments_by_application("INVALID")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
