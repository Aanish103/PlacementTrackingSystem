import sys
import os
import unittest
from unittest.mock import patch
import random
import string

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import placement_staffs
from modules import visits


def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email():
    return random_string(5) + "@test.com"

def random_phone():
    return ''.join(random.choices(string.digits, k=10))

def random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(2024, 2030)
    return f"{day:02d}/{month:02d}/{year}"

def random_outcome():
    return random.choice(["Positive", "Negative", "Neutral"])


class TestAddPlacementStaff_Random(unittest.TestCase):

    @patch("modules.placement_staffs.ds.add_staff", return_value="ST" + str(random.randint(100, 999)))
    @patch("builtins.input")
    def test_random_inputs(self, mock_input, mock_add):
        # Generate random inputs
        mock_input.side_effect = [
            random_string(6),   # name
            random_email(),     # email
            random_phone(),     # phone
            random_string(4)    # role
        ]

        placement_staffs.add_placement_staff()
        mock_add.assert_called_once()


class TestAddVisit_Random(unittest.TestCase):

    @patch("modules.visits.ds.get_by_id")
    @patch("modules.visits.ds.add_visit", return_value="V" + str(random.randint(100, 999)))
    @patch("builtins.input")
    def test_random_visit(self, mock_input, mock_add, mock_get):
        # Mock application exists
        mock_get.return_value = {"application_id": "AP001"}

        mock_input.side_effect = [
            "AP001",             # application_id
            random_string(6),    # visitor_name
            random_date(),       # visit_date
            random_outcome(),    # outcome
            random_string(10)    # notes
        ]

        visits.add_visit()
        mock_add.assert_called_once()


class TestUpdateVisit_Random(unittest.TestCase):

    @patch("modules.visits.ds.get_by_id")
    @patch("modules.visits.ds.update_visit", return_value=True)
    @patch("builtins.input")
    def test_random_update(self, mock_input, mock_update, mock_get):
        # Mock visit exists
        mock_get.return_value = {
            "visitor_name": "OldVisitor",
            "visit_date": "01/01/2025",
            "outcome": "Neutral",
            "notes": "Old Notes"
        }

        mock_input.side_effect = [
            "V001",             # visit_id
            random_string(6),   # visitor_name
            random_date(),      # visit_date
            random_outcome(),   # outcome
            random_string(10)   # notes
        ]

        visits.update_visit()
        mock_update.assert_called_once()


if __name__ == "__main__":
    unittest.main()
