import unittest
from unittest.mock import patch

from students import add_student


class TestAddStudentEquivalence(unittest.TestCase):

    @patch("builtins.input", side_effect=[
        "Apurva", "15/10/1996", "Nashik", "BSc", "2024", "SC001", "ST001"
    ])
    @patch("aat25.modules.data_store.add_student", return_value="STU001")
    def test_add_student_valid(self, mock_add, mock_input):
        add_student()
        mock_add.assert_called_once()


if __name__ == "__main__":
    unittest.main()
