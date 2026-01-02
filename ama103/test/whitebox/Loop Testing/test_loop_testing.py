import unittest
import sys
import os
from unittest.mock import patch

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store, students


class TestLoopTesting(unittest.TestCase):

    def setUp(self):
        self.orig_students = list(data_store.students)
        self.orig_apps = list(data_store.applications)
        self.orig_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.students.clear()
        data_store.students.extend(self.orig_students)

        data_store.applications.clear()
        data_store.applications.extend(self.orig_apps)

        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)


# Find Student by Student ID
    @patch("builtins.input", return_value="ST001")
    def test_find_student_single_iteration(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)

    @patch("builtins.input", return_value="INVALID")
    def test_find_student_zero_iteration(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)



# Update Application
    def test_update_application_multiple_iterations(self):
        result = data_store.update_application("AP001", {"status": "Approved"})
        self.assertTrue(result)

    def test_update_application_no_match(self):
        result = data_store.update_application("INVALID", {"status": "Approved"})
        self.assertFalse(result)




# Show full Details
    @patch("builtins.input", return_value="ST001")
    def test_show_full_details_multiple_loops(self, mock_input):
        result = students.show_full_details_for_student()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()