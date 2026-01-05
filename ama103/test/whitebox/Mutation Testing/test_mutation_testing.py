import unittest
import sys
import os
from unittest.mock import patch

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store, students


class TestMutationTesting(unittest.TestCase):


    def setUp(self):
        self.orig_apps = list(data_store.applications)
        self.orig_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.applications.clear()
        data_store.applications.extend(self.orig_apps)

        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)




# Add Application

    def test_add_application_mutation(self):
        aid = data_store.add_application(
            "ST001", "Google", "Intern",
            "2025-06-01", "2025-09-01", ["CV.pdf"]
        )
        self.assertIsNotNone(aid)



# Get by ID

    def test_get_by_id_valid(self):
        app = data_store.get_by_id(data_store.applications, "AP001")
        self.assertIsNotNone(app)

    def test_get_by_id_invalid(self):
        app = data_store.get_by_id(data_store.applications, "INVALID")
        self.assertIsNone(app)



# Update Application

    def test_update_application_valid(self):
        result = data_store.update_application("AP001", {"status": "Approved"})
        self.assertTrue(result)

    def test_update_application_invalid(self):
        result = data_store.update_application("INVALID", {"status": "Approved"})
        self.assertFalse(result)



# Delete Application

    def test_delete_application_valid(self):
        result = data_store.delete_application("AP001")
        self.assertTrue(result)

    def test_delete_application_invalid(self):
        result = data_store.delete_application("INVALID")
        self.assertFalse(result)




# Add Assessment

    def test_add_assessment_valid(self):
        aid = data_store.add_assessment("AP001", 85, "Pass", "Good")
        self.assertIsNotNone(aid)



# Update Assessment

    def test_update_assessment_valid(self):
        result = data_store.update_assessment("AS001", {"score": 90})
        self.assertTrue(result)

    def test_update_assessment_invalid(self):
        result = data_store.update_assessment("INVALID", {"score": 90})
        self.assertFalse(result)



# Delete Assessment

    def test_delete_assessment_valid(self):
        result = data_store.delete_assessment("AS001")
        self.assertTrue(result)

    def test_delete_assessment_invalid(self):
        result = data_store.delete_assessment("INVALID")
        self.assertFalse(result)




# Find student

    @patch("builtins.input", return_value="ST001")
    def test_find_student_exists(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)

    @patch("builtins.input", return_value="INVALID")
    def test_find_student_not_exists(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)





# Show full Details
    @patch("builtins.input", return_value="ST001")
    def test_show_full_details_executes(self, mock_input):
        result = students.show_full_details_for_student()
        self.assertIsNone(result)



if __name__ == "__main__":
    unittest.main()