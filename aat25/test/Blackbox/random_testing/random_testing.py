import sys
import os
import unittest
import random
import string
from unittest.mock import patch

CURRENT_DIR = os.path.dirname(__file__)
while CURRENT_DIR != os.path.dirname(CURRENT_DIR):
    if os.path.isdir(os.path.join(CURRENT_DIR, "modules")):
        sys.path.insert(0, CURRENT_DIR)
        break
    CURRENT_DIR = os.path.dirname(CURRENT_DIR)
else:
    raise RuntimeError("Could not locate project root containing 'modules' directory")


from modules import students


def random_string(length=6):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


# add_student
class TestAddStudentRandom(unittest.TestCase):

    @patch("modules.students.ds.add_student", return_value="STU999")
    @patch("builtins.input")
    def test_add_student_random(self, mock_input, mock_add):
        mock_input.side_effect = [
            random_string(),
            "01/01/2000",
            random_string(),
            "BSc",
            str(random.randint(1990, 2030)),
            "SC" + str(random.randint(1, 99)).zfill(3),
            "ST" + str(random.randint(1, 99)).zfill(3)
        ]
        students.add_student()
        mock_add.assert_called_once()


# update_student
class TestUpdateStudentRandom(unittest.TestCase):

    @patch("modules.students.ds.get_by_id")
    @patch("modules.students.ds.update_student", return_value=True)
    @patch("builtins.input")
    def test_update_student_random(self, mock_input, mock_update, mock_get):

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
            "STU" + str(random.randint(1, 999)).zfill(3),
            random_string(),
            "",
            "",
            "",
            "",
            "",
            ""
        ]

        students.update_student()
        mock_update.assert_called_once()


# delete_student
class TestDeleteStudentRandom(unittest.TestCase):

    @patch("modules.students.ds.delete_student", return_value=False)
    @patch("builtins.input")
    def test_delete_student_random(self, mock_input, mock_delete):
        mock_input.return_value = "STU" + str(random.randint(100, 999))
        students.delete_student()
        mock_delete.assert_called_once()


# filter_students_by_graduation_year
class TestFilterStudentsByYearRandom(unittest.TestCase):

    @patch("builtins.input")
    def test_filter_students_random_year(self, mock_input):
        mock_input.return_value = str(random.randint(1990, 2030))
        students.filter_students_by_graduation_year()


# filter_students_by_school
class TestFilterStudentsBySchoolRandom(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value=None)
    @patch("builtins.input")
    def test_filter_students_random_school(self, mock_input, mock_get):
        mock_input.return_value = "SC" + str(random.randint(1, 99)).zfill(3)
        students.filter_students_by_school()


if __name__ == "__main__":
    unittest.main()
