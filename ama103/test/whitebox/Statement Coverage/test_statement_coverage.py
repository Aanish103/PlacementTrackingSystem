import unittest
import sys
import os
from unittest.mock import patch

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import students


class TestStatementCoverage(unittest.TestCase):

# Find Student

    @patch("builtins.input", return_value="ST001")
    def test_find_student_exists_executes(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)

    @patch("builtins.input", return_value="INVALID")
    def test_find_student_not_exists_executes(self, mock_input):
        result = students.find_student_by_id()
        self.assertIsNone(result)

# Show full details for student

    @patch("builtins.input", return_value="ST001")
    def test_show_full_details_executes(self, mock_input):
        result = students.show_full_details_for_student()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()