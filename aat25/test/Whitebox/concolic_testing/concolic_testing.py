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
    raise RuntimeError("Could not locate project root containing 'modules'")

from modules import students


class TestUpdateStudentConcolic(unittest.TestCase):
    """
    Concolic-style testing:
    Concrete execution is guided to explore both symbolic paths
    of the condition: if not s
    """

    def test_path_student_not_found(self):
        """
        Path constraint:
            s == None
        Concrete input chosen:
            student_id = "INVALID"
        """

        with patch("modules.students.ds.get_by_id", return_value=None), \
             patch("builtins.input", return_value="INVALID"):
            students.update_student()

    def test_path_student_found(self):
        """
        Path constraint:
            s != None
        Concrete input chosen:
            student_id = "STU001"
        """

        with patch("modules.students.ds.get_by_id", return_value={
            "name": "A",
            "dob": "1",
            "address": "X",
            "qualification": "B",
            "grad_year": 2024,
            "school_id": "SC001",
            "staff_id": "ST001"
        }), patch("modules.students.ds.update_student", return_value=True), \
             patch("builtins.input") as mock_input:

            mock_input.side_effect = [
                "ST001", "", "", "", "", "", "", ""
            ]

            students.update_student()


if __name__ == "__main__":
    unittest.main()
