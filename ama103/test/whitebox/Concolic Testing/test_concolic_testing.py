import unittest
import sys
import os

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store


class TestConcolicTesting(unittest.TestCase):

    def setUp(self):
        self.orig_apps = list(data_store.applications)
        self.orig_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.applications.clear()
        data_store.applications.extend(self.orig_apps)

        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)



# Add Application

    def test_add_application_valid_path(self):
        aid = data_store.add_application(
            "ST001", "Google", "Intern",
            "2025-06-01", "2025-09-01", ["CV.pdf"]
        )
        self.assertIsNotNone(aid)

    def test_add_application_invalid_student_path(self):
        aid = data_store.add_application(
            "", "Google", "Intern",
            "2025-06-01", "2025-09-01", ["CV.pdf"]
        )
        self.assertIsNotNone(aid)



# Update Application

    def test_update_application_valid_id_path(self):
        result = data_store.update_application(
            "AP001", {"status": "Approved"}
        )
        self.assertTrue(result)

    def test_update_application_invalid_id_path(self):
        result = data_store.update_application(
            "INVALID", {"status": "Approved"}
        )
        self.assertFalse(result)



# Add Assessment

    def test_add_assessment_valid_path(self):
        aid = data_store.add_assessment(
            "AP001", 85, "Pass", "Good"
        )
        self.assertIsNotNone(aid)

    def test_add_assessment_invalid_application_path(self):
        aid = data_store.add_assessment(
            "INVALID", 85, "Fail", "Invalid app"
        )
        self.assertIsNotNone(aid)



# Update Assessment

    def test_update_assessment_valid_path(self):
        result = data_store.update_assessment(
            "AS001", {"score": 90}
        )
        self.assertTrue(result)

    def test_update_assessment_invalid_path(self):
        result = data_store.update_assessment(
            "INVALID", {"score": 90}
        )
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()