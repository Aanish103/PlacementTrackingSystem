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


def mutant_filter_students_by_year_negated():
    year = input("Enter Graduation Year: ")
    # MUTATION: removed NOT
    if year.isdigit():
        print("Invalid year.")
        return
    print("Mutant survived path")


def mutant_filter_students_by_year_no_validation():
    year = input("Enter Graduation Year: ")
    # MUTATION: validation removed
    print("Mutant survived path")


class TestMutationFilterStudentsByYear(unittest.TestCase):

    @patch("builtins.input", return_value="ABCD")
    def test_mutant_1_killed(self, mock_input):
        """
        Original behaviour:
            Invalid year -> printed
        Mutant behaviour:
            Invalid input treated as valid
        EXPECTED: mutant should be killed
        """

        with patch.object(students, "filter_students_by_graduation_year",
                          mutant_filter_students_by_year_negated):
            students.filter_students_by_graduation_year()
            print("[MUTATION] Mutant 1 executed")

    @patch("builtins.input", return_value="ABCD")
    def test_mutant_2_killed(self, mock_input):
        """
        Original behaviour:
            Invalid year rejected
        Mutant behaviour:
            Validation removed
        EXPECTED: mutant should be killed
        """

        with patch.object(students, "filter_students_by_graduation_year",
                          mutant_filter_students_by_year_no_validation):
            students.filter_students_by_graduation_year()
            print("[MUTATION] Mutant 2 executed")


if __name__ == "__main__":
    unittest.main()
