import unittest
import sys
import os

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store

class TestEquivalencePartition(unittest.TestCase):

    def setUp(self):
        self.original_applications = list(data_store.applications)
        self.original_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.applications.clear()
        data_store.applications.extend(self.original_applications)

        data_store.assessments.clear()
        data_store.assessments.extend(self.original_assessments)

# Update Application
    def test_add_application_valid(self):
        aid = data_store.add_application(
            "ST001", "Google", "Intern",
            "2025-06-01", "2025-09-01", ["CV.pdf"]
        )
        self.assertIsNotNone(aid)

    def test_add_application_invalid_student(self):
        aid = data_store.add_application(
            "", "Google", "Intern",
            "2025-06-01", "2025-09-01", ["CV.pdf"]
        )
        self.assertIsNotNone(aid)

# Update Application
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

# Add Assessment
    def test_add_assessment_valid(self):
        aid = data_store.add_assessment(
            "AP001", 85, "Pass", "Good performance"
        )
        self.assertIsNotNone(aid)

    def test_add_assessment_invalid(self):
        aid = data_store.add_assessment(
            "INVALID", 85, "Pass", "Invalid app"
        )
        self.assertIsNotNone(aid)

# Update Assessment
    def test_update_assessment_valid(self):
        result = data_store.update_assessment(
            "AS001", {"score": 90}
        )
        self.assertTrue(result)

    def test_update_assessment_invalid(self):
        result = data_store.update_assessment(
            "INVALID", {"score": 90}
        )
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()