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


class TestSymbolicExecutionFilterStudentsByYear(unittest.TestCase):
    """
    Symbolic Execution (simulated):
    Input year is treated as symbolic variable Y
    """

    def test_path_P1_invalid_year(self):
        """
        Path constraint:
            ¬isdigit(Y)
        Example concrete value:
            Y = "ABCD"
        """

        with patch("builtins.input", return_value="ABCD"):
            students.filter_students_by_graduation_year()

        print("[Symbolic Path P1] year = non-numeric")

    def test_path_P2_valid_year_no_students(self):
        """
        Path constraint:
            isdigit(Y) ∧ students = empty
        Example concrete value:
            Y = "2024"
        """

        with patch("builtins.input", return_value="2024"), \
             patch.object(students.ds, "students", []):
            students.filter_students_by_graduation_year()

        print("[Symbolic Path P2] year numeric, students empty")

    def test_path_P3_valid_year_with_students(self):
        """
        Path constraint:
            isdigit(Y) ∧ students ≠ empty
        Example concrete value:
            Y = "2024"
        """

        with patch("builtins.input", return_value="2024"), \
             patch.object(students.ds, "students", [
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

        print("[Symbolic Path P3] year numeric, students present")


if __name__ == "__main__":
    unittest.main()
