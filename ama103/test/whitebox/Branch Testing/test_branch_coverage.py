import unittest
import sys
import os
from unittest.mock import patch

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store, students


class TestBranchCoverage(unittest.TestCase):

    def setUp(self):
        self.orig_apps = list(data_store.applications)
        self.orig_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.applications.clear()
        data_store.applications.extend(self.orig_apps)

        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)


# Add Assessment
    def test_add_assessment_valid_branch(self):
        aid = data_store.add_assessment("AP001", 80, "Pass", "Good")
        self.assertIsNotNone(aid)

    def test_add_assessment_invalid_branch(self):
        # Invalid application_id branch
        aid = data_store.add_assessment("INVALID", 80, "Fail", "Invalid app")
        self.assertIsNotNone(aid)




# Update Application

    def test_update_application_valid_branch(self):
        result = data_store.update_application("AP001", {"status": "Approved"})
        self.assertTrue(result)

    def test_update_application_invalid_branch(self):
        result = data_store.update_application("INVALID", {"status": "Approved"})
        self.assertFalse(result)


#Find Student

    @patch("builtins.input", return_value="ST001")
    def test_find_student_exists_branch(self, mock_input):
        students.find_student_by_id()

    @patch("builtins.input", return_value="INVALID")
    def test_find_student_not_exists_branch(self, mock_input):
        students.find_student_by_id()



# Show full Details

    @patch("builtins.input", return_value="ST001")
    def test_show_full_details_branch(self, mock_input):
        students.show_full_details_for_student()


if __name__ == "__main__":
    unittest.main()