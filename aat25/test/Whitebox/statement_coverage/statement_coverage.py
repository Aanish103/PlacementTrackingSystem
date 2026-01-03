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

from modules import students, schools


class TestStatementCoverage(unittest.TestCase):

    # add_student
    @patch("modules.students.ds.add_student", return_value="ST001")
    @patch("builtins.input")
    def test_add_student_statement(self, mock_input, mock_add):
        mock_input.side_effect = [
            "Apurva", "15/10/1996", "Nashik",
            "BSc", "2024", "SC001", "ST001"
        ]
        students.add_student()

    # update_student
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
    def test_update_student_statement(self, mock_input, mock_update, mock_get):
        mock_input.side_effect = [
            "STU001", "", "", "", "", "", "", ""
        ]
        students.update_student()

    # delete_student
    @patch("modules.students.ds.delete_student", return_value=True)
    @patch("builtins.input", return_value="STU001")
    def test_delete_student_statement(self, mock_input, mock_delete):
        students.delete_student()

    # filter_students_by_graduation_year
    @patch("builtins.input", return_value="2024")
    def test_filter_students_by_year_statement(self, mock_input):
        with patch.object(students.ds, "students", [
            {
                "student_id": "ST001",
                "name": "A",
                "dob": "1",
                "address": "X",
                "qualification": "B",
                "school_id": "SC1",
                "staff_id": "ST1",
                "grad_year": 2024
            }
        ]):
            students.filter_students_by_graduation_year()

    # filter_students_by_school
    @patch("modules.students.ds.get_by_id", return_value={
        "school_id": "SC001",
        "school_name": "Test School",
        "location": "UK"
    })
    @patch("builtins.input", return_value="SC001")
    def test_filter_students_by_school_statement(self, mock_input, mock_get):
        with patch.object(students.ds, "students", [
            {
                "student_id": "ST001",
                "name": "A",
                "dob": "1",
                "address": "X",
                "qualification": "B",
                "school_id": "SC001",
                "staff_id": "ST1",
                "grad_year": 2024
            }
        ]):
            students.filter_students_by_school()

    # show_all_schools
    def test_show_all_schools_statement(self):
        with patch.object(students.ds, "schools", [
            {"school_id": "SC001", "school_name": "Test", "location": "UK"}
        ]):
            schools.show_all_schools()


if __name__ == "__main__":
    unittest.main()
