import sys
import os
import unittest
from unittest.mock import patch

# Project root (same style as your friend)
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import students, applications


# add_student
class TestAddStudentEP(unittest.TestCase):

    @patch("modules.students.ds.add_student", return_value="STU001")
    @patch("builtins.input")
    def test_add_student_valid_partition(self, mock_input, mock_add):
        mock_input.side_effect = [
            "Apurva", "15/10/1997", "UK",
            "BSc", "2024", "SC001", "ST001"
        ]
        students.add_student()
        mock_add.assert_called_once()


# update_student
class TestUpdateStudentEP(unittest.TestCase):

    @patch("modules.students.ds.get_by_id")
    @patch("modules.students.ds.update_student", return_value=True)
    @patch("builtins.input")
    def test_update_student_valid_id(self, mock_input, mock_update, mock_get):

        # 8 inputs (student_id + 7 fields)
        mock_input.side_effect = [
            "STU001",  # student_id
            "",        # name
            "",        # dob
            "",        # address
            "",        # qualification
            "",        # grad_year
            "",        # school_id
            ""         # staff_id
        ]

        mock_get.return_value = {
            "name": "A",
            "dob": "1",
            "address": "X",
            "qualification": "B",
            "grad_year": 2024,
            "school_id": "SC1",
            "staff_id": "ST1"
        }

        students.update_student()
        mock_update.assert_called_once()


# delete_student
class TestDeleteStudentEP(unittest.TestCase):

    @patch("modules.students.ds.delete_student", return_value=True)
    @patch("builtins.input", return_value="STU001")
    def test_delete_student_valid_id(self, mock_input, mock_delete):
        students.delete_student()
        mock_delete.assert_called_once()


# filter_students_by_school
class TestFilterStudentsBySchoolEP(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value={
        "school_id": "SC001",
        "school_name": "Test School",
        "location": "UK"
    })
    @patch("builtins.input", return_value="SC001")
    def test_filter_students_valid_school(self, mock_input, mock_get):
        students.filter_students_by_school()


# show_applications_by_student
class TestShowApplicationsByStudentEP(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value={"student_id": "STU001"})
    @patch("builtins.input", return_value="STU001")
    def test_show_applications_valid_student(self, mock_input, mock_get):
        applications.show_applications_by_student()


# filter_students_by_graduation_year
class TestFilterStudentsByYearEP(unittest.TestCase):

    @patch("builtins.input", return_value="2024")
    def test_filter_students_valid_year(self, mock_input):
        students.filter_students_by_graduation_year()


if __name__ == "__main__":
    unittest.main()
