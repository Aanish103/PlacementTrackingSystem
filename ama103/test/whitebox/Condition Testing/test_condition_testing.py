import unittest
import sys
import os
from unittest.mock import patch

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store, students


class TestConditionTesting(unittest.TestCase):

    def setUp(self):
        self.orig_apps = list(data_store.applications)
        self.orig_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.applications.clear()
        data_store.applications.extend(self.orig_apps)

        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)



# Update Application

    def test_update_application_condition_true(self):
        result = data_store.update_application("AP001", {"status": "Approved"})
        self.assertTrue(result)

    def test_update_application_condition_false(self):
        result = data_store.update_application("INVALID", {"status": "Approved"})
        self.assertFalse(result)




# Add Assessment

    def test_add_assessment_condition_true(self):
        aid = data_store.add_assessment("AP001", 85, "Pass", "Good")
        self.assertIsNotNone(aid)

    def test_add_assessment_condition_false(self):
        aid = data_store.add_assessment("INVALID", 85, "Fail", "Invalid app")
        self.assertIsNotNone(aid)



# Update Assessment

    def test_update_assessment_condition_true(self):
        result = data_store.update_assessment("AS001", {"score": 90})
        self.assertTrue(result)

    def test_update_assessment_condition_false(self):
        result = data_store.update_assessment("INVALID", {"score": 90})
        self.assertFalse(result)



# Find Student by ID

    @patch("builtins.input", return_value="ST001")
    def test_find_student_condition_true(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)

    @patch("builtins.input", return_value="INVALID")
    def test_find_student_condition_false(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)




# Show full Details for student

    @patch("builtins.input", return_value="ST001")
    def test_show_full_details_condition(self, mock_input):
        result = students.show_full_details_for_student()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()