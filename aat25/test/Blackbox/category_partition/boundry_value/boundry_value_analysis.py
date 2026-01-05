import sys
import os
import unittest
from unittest.mock import patch

# Add PlacementTrackingSystem to Python path (IMPORTANT)
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import students, applications


# 1️⃣ add_student – Boundary: minimum graduation year
class TestAddStudentBVA(unittest.TestCase):

    @patch("modules.students.ds.add_student", return_value="STU001")
    @patch("builtins.input")
    def test_add_student_min_year(self, mock_input, mock_add):
        mock_input.side_effect = [
            "Apurva", "15/10/1996", "Nashik",
            "BSc", "1900", "SC001", "ST001"
        ]
        students.add_student()
        mock_add.assert_called_once()


# 2️⃣ update_student – Boundary: empty student_id
class TestUpdateStudentBVA(unittest.TestCase):

    @patch("builtins.input", return_value="")
    def test_update_student_empty_id(self, mock_input):
        students.update_student()


# 3️⃣ delete_student – Boundary: empty student_id
class TestDeleteStudentBVA(unittest.TestCase):

    @patch("modules.students.ds.delete_student", return_value=False)
    @patch("builtins.input", return_value="")
    def test_delete_student_empty_id(self, mock_input, mock_delete):
        students.delete_student()
        mock_delete.assert_called_once()


# 4️⃣ show_applications_by_student – Boundary: empty student_id
class TestShowApplicationsByStudentBVA(unittest.TestCase):

    @patch("modules.applications.ds.get_by_id", return_value=None)
    @patch("builtins.input", return_value="")
    def test_show_applications_empty_student_id(self, mock_input, mock_get):
        applications.show_applications_by_student()


# 5️⃣ filter_students_by_graduation_year – Boundary: non-numeric year
class TestFilterStudentsByYearBVA(unittest.TestCase):

    @patch("builtins.input", return_value="ABCD")
    def test_filter_students_invalid_year(self, mock_input):
        students.filter_students_by_graduation_year()


if __name__ == "__main__":
    unittest.main()
