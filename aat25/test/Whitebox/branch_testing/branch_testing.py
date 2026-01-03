import sys
import os
import unittest
from unittest.mock import patch

# Robust project root detection
CURRENT_DIR = os.path.dirname(__file__)
while CURRENT_DIR != os.path.dirname(CURRENT_DIR):
    if os.path.isdir(os.path.join(CURRENT_DIR, "modules")):
        sys.path.insert(0, CURRENT_DIR)
        break
    CURRENT_DIR = os.path.dirname(CURRENT_DIR)
else:
    raise RuntimeError("Could not locate project root containing 'modules' directory")

from modules import students, applications

# update_student
class TestUpdateStudentBranch(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value=None)
    @patch("builtins.input", return_value="BADID")
    def test_update_student_not_found_branch(self, mock_input, mock_get):
        """Branch: student NOT found"""
        students.update_student()

    @patch("modules.students.ds.get_by_id")
    @patch("modules.students.ds.update_student", return_value=True)
    @patch("builtins.input")
    def test_update_student_found_branch(self, mock_input, mock_update, mock_get):
        """Branch: student found"""

        mock_get.return_value = {
            "name": "A",
            "dob": "1",
            "address": "X",
            "qualification": "B",
            "grad_year": 2024,
            "school_id": "SC1",
            "staff_id": "ST1"
        }

        mock_input.side_effect = [
            "ST001", "", "", "", "", "", "", ""
        ]

        students.update_student()
        mock_update.assert_called_once()


# delete_student
class TestDeleteStudentBranch(unittest.TestCase):

    @patch("modules.students.ds.delete_student", return_value=True)
    @patch("builtins.input", return_value="ST001")
    def test_delete_student_success_branch(self, mock_input, mock_delete):
        """Branch: deletion successful"""
        students.delete_student()
        mock_delete.assert_called_once()

    @patch("modules.students.ds.delete_student", return_value=False)
    @patch("builtins.input", return_value="BADID")
    def test_delete_student_failure_branch(self, mock_input, mock_delete):
        """Branch: deletion failed"""
        students.delete_student()
        mock_delete.assert_called_once()


# filter_students_by_school
class TestFilterStudentsBySchoolBranch(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value={
        "school_id": "SC001",
        "school_name": "Test School",
        "location": "UK"
    })
    @patch("builtins.input", return_value="SC001")
    def test_filter_students_school_found(self, mock_input, mock_get):
        """Branch: school found"""
        students.filter_students_by_school()

    @patch("modules.students.ds.get_by_id", return_value=None)
    @patch("builtins.input", return_value="BAD")
    def test_filter_students_school_not_found(self, mock_input, mock_get):
        """Branch: school NOT found"""
        students.filter_students_by_school()


# show_applications_by_student
class TestShowApplicationsByStudentBranch(unittest.TestCase):

    @patch("modules.applications.ds.get_by_id", return_value={"student_id": "ST001"})
    @patch("builtins.input", return_value="ST001")
    def test_show_applications_none_branch(self, mock_input, mock_get):
        """Branch: no applications"""

        # Patch the DATA, not as decorator
        with patch.object(applications.ds, "applications", []):
            applications.show_applications_by_student()

    @patch("modules.applications.ds.get_by_id", return_value={"student_id": "ST001"})
    @patch("builtins.input", return_value="ST001")
    def test_show_applications_exist_branch(self, mock_input, mock_get):
        """Branch: applications exist"""

        test_apps = [
            {
                "application_id": "AP001",
                "student_id": "ST001",
                "employer": "ABC",
                "role": "Intern",
                "start_date": "01/01/2025",
                "end_date": "01/06/2025",
                "status": "Approved",
                "documents": []
            }
        ]

        # Patch the DATA, not as decorator
        with patch.object(applications.ds, "applications", test_apps):
            applications.show_applications_by_student()


# filter_students_by_graduation_year
class TestFilterStudentsByYearBranch(unittest.TestCase):

    @patch("builtins.input", return_value="2024")
    def test_filter_students_valid_year_branch(self, mock_input):
        """Branch: valid numeric year"""
        students.filter_students_by_graduation_year()

    @patch("builtins.input", return_value="ABCD")
    def test_filter_students_invalid_year_branch(self, mock_input):
        """Branch: invalid year"""
        students.filter_students_by_graduation_year()


if __name__ == "__main__":
    unittest.main()
