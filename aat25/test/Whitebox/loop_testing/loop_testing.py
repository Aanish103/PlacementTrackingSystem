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


class CountingList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.iteration_count = 0

    def __iter__(self):
        for item in super().__iter__():
            self.iteration_count += 1
            yield item


class TestFilterStudentsByYearLoop(unittest.TestCase):

    @patch("builtins.input", return_value="2024")
    def test_zero_iterations(self, mock_input):
        students_list = CountingList([])
        with patch.object(students.ds, "students", students_list):
            students.filter_students_by_graduation_year()
        print(f"[Loop Count] filter_students_by_graduation_year → {students_list.iteration_count}")

    @patch("builtins.input", return_value="2024")
    def test_one_iteration(self, mock_input):
        students_list = CountingList([
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
        ])
        with patch.object(students.ds, "students", students_list):
            students.filter_students_by_graduation_year()
        print(f"[Loop Count] filter_students_by_graduation_year → {students_list.iteration_count}")

    @patch("builtins.input", return_value="2024")
    def test_multiple_iterations(self, mock_input):
        students_list = CountingList([
            {
                "student_id": "S1",
                "name": "A",
                "dob": "1",
                "address": "X",
                "qualification": "B",
                "school_id": "SC1",
                "staff_id": "ST1",
                "grad_year": 2024
            },
            {
                "student_id": "S2",
                "name": "B",
                "dob": "2",
                "address": "Y",
                "qualification": "MSc",
                "school_id": "SC2",
                "staff_id": "ST2",
                "grad_year": 2024
            }
        ])
        with patch.object(students.ds, "students", students_list):
            students.filter_students_by_graduation_year()
        print(f"[Loop Count] filter_students_by_graduation_year → {students_list.iteration_count}")


class TestFilterStudentsBySchoolLoop(unittest.TestCase):

    @patch("modules.students.ds.get_by_id", return_value={
        "school_id": "SC001",
        "school_name": "Test School",
        "location": "UK"
    })
    @patch("builtins.input", return_value="SC001")
    def test_zero_students(self, mock_input, mock_get):
        students_list = CountingList([])
        with patch.object(students.ds, "students", students_list):
            students.filter_students_by_school()
        print(f"[Loop Count] filter_students_by_school → {students_list.iteration_count}")

    @patch("modules.students.ds.get_by_id", return_value={
        "school_id": "SC001",
        "school_name": "Test School",
        "location": "UK"
    })
    @patch("builtins.input", return_value="SC001")
    def test_one_student(self, mock_input, mock_get):
        students_list = CountingList([
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
        ])
        with patch.object(students.ds, "students", students_list):
            students.filter_students_by_school()
        print(f"[Loop Count] filter_students_by_school → {students_list.iteration_count}")

    @patch("modules.students.ds.get_by_id", return_value={
        "school_id": "SC001",
        "school_name": "Test School",
        "location": "UK"
    })
    @patch("builtins.input", return_value="SC001")
    def test_multiple_students(self, mock_input, mock_get):
        students_list = CountingList([
            {
                "student_id": "S1",
                "name": "A",
                "dob": "1",
                "address": "X",
                "qualification": "B",
                "school_id": "SC001",
                "staff_id": "ST1",
                "grad_year": 2024
            },
            {
                "student_id": "S2",
                "name": "B",
                "dob": "2",
                "address": "Y",
                "qualification": "MSc",
                "school_id": "SC001",
                "staff_id": "ST2",
                "grad_year": 2024
            }
        ])
        with patch.object(students.ds, "students", students_list):
            students.filter_students_by_school()
        print(f"[Loop Count] filter_students_by_school → {students_list.iteration_count}")


class TestShowAllSchoolsLoop(unittest.TestCase):

    def test_zero_schools(self):
        schools_list = CountingList([])
        with patch.object(students.ds, "schools", schools_list):
            schools.show_all_schools()
        print(f"[Loop Count] show_all_schools → {schools_list.iteration_count}")

    def test_one_school(self):
        schools_list = CountingList([
            {"school_id": "SC001", "school_name": "Test", "location": "UK"}
        ])
        with patch.object(students.ds, "schools", schools_list):
            schools.show_all_schools()
        print(f"[Loop Count] show_all_schools → {schools_list.iteration_count}")

    def test_multiple_schools(self):
        schools_list = CountingList([
            {"school_id": "SC001", "school_name": "A", "location": "UK"},
            {"school_id": "SC002", "school_name": "B", "location": "US"}
        ])
        with patch.object(students.ds, "schools", schools_list):
            schools.show_all_schools()
        print(f"[Loop Count] show_all_schools → {schools_list.iteration_count}")


if __name__ == "__main__":
    unittest.main()
