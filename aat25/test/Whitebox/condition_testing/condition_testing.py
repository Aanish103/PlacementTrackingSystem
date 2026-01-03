import sys
import os
import unittest
from unittest.mock import patch


CURRENT_DIR = os.path.dirname(__file__)
while CURRENT_DIR != os.path.dirname(CURRENT_DIR):
    if os.path.isdir(os.path.join(CURRENT_DIR, "modules")):
        sys.path.insert(0, CURRENT_DIR)
        break
    CURRENT_DIR = os.path.dirname(CURRENT_DIR)
else:
    raise RuntimeError("Could not locate project root containing 'modules'")

from modules import students

# filter_students_by_graduation_year – Condition: year.isdigit()
class TestFilterStudentsByYearCondition(unittest.TestCase):

    @patch("builtins.input", return_value="2024")
    def test_year_isdigit_true(self, mock_input):
        """Condition TRUE: year.isdigit() == True"""
        students.filter_students_by_graduation_year()

    @patch("builtins.input", return_value="ABCD")
    def test_year_isdigit_false(self, mock_input):
        """Condition FALSE: year.isdigit() == False"""
        students.filter_students_by_graduation_year()


# update_student – Condition: student exists
class TestUpdateStudentCondition(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value=None)
    @patch("builtins.input", return_value="BADID")
    def test_student_not_found_condition(self, mock_input, mock_get):
        """Condition TRUE: not s"""
        students.update_student()

    @patch("modules.students.ds.get_by_id", return_value={
        "name": "A",
        "dob": "1",
        "address": "X",
        "qualification": "B",
        "grad_year": 2024,
        "school_id": "SC1",
        "staff_id": "ST1"
    })
    @patch("modules.students.ds.update_student", return_value=True)
    @patch("builtins.input")
    def test_student_found_condition(self, mock_input, mock_update, mock_get):
        """Condition FALSE: not s"""

        mock_input.side_effect = [
            "STU001", "", "", "", "", "", "", ""
        ]
        students.update_student()


# delete_student – Condition: delete result
class TestDeleteStudentCondition(unittest.TestCase):

    @patch("modules.students.ds.delete_student", return_value=True)
    @patch("builtins.input", return_value="STU001")
    def test_delete_success_condition(self, mock_input, mock_delete):
        """Condition TRUE: deletion succeeded"""
        students.delete_student()

    @patch("modules.students.ds.delete_student", return_value=False)
    @patch("builtins.input", return_value="BADID")
    def test_delete_failure_condition(self, mock_input, mock_delete):
        """Condition FALSE: deletion failed"""
        students.delete_student()


# filter_students_by_school – Condition: school exists
class TestFilterStudentsBySchoolCondition(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value={
        "school_id": "SC001",
        "school_name": "Test School",
        "location": "UK"
    })
    @patch("builtins.input", return_value="SC001")
    def test_school_exists_condition(self, mock_input, mock_get):
        """Condition FALSE: not school"""
        students.filter_students_by_school()

    @patch("modules.students.ds.get_by_id", return_value=None)
    @patch("builtins.input", return_value="BAD")
    def test_school_not_found_condition(self, mock_input, mock_get):
        """Condition TRUE: not school"""
        students.filter_students_by_school()


if __name__ == "__main__":
    unittest.main()
