import sys
import os
import unittest
from unittest.mock import patch

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import placement_staffs
from modules import visits

class TestUpdatePlacementStaff_Condition(unittest.TestCase):

    # Condition: staff exists → True branch
    @patch("modules.placement_staffs.ds.get_by_id")
    @patch("modules.placement_staffs.ds.update_staff", return_value=True)
    @patch("builtins.input")
    def test_staff_exists_update_some_fields(self, mock_input, mock_update, mock_get):
        mock_get.return_value = {
            "name": "OldName",
            "email": "old@mail.com",
            "phone": "123456",
            "role": "Admin"
        }

        # User updates name and leaves others blank
        mock_input.side_effect = [
            "ST001",      # staff_id
            "NewName",    # name
            "",           # email
            "",           # phone
            ""            # role
        ]

        placement_staffs.update_placement_staff()
        mock_update.assert_called_once()

    # Condition: staff does not exist → False branch
    @patch("modules.placement_staffs.ds.get_by_id", return_value=None)
    @patch("builtins.input", return_value="ST999")
    def test_staff_does_not_exist(self, mock_input, mock_get):
        placement_staffs.update_placement_staff()
        mock_get.assert_called_once()


class TestUpdateVisit_Condition(unittest.TestCase):

    # Condition: visit exists → True branch
    @patch("modules.visits.ds.get_by_id")
    @patch("modules.visits.ds.update_visit", return_value=True)
    @patch("builtins.input")
    def test_visit_exists_update_fields(self, mock_input, mock_update, mock_get):
        mock_get.return_value = {
            "visitor_name": "OldVisitor",
            "visit_date": "01/01/2025",
            "outcome": "Neutral",
            "notes": "Old Notes"
        }

        # Update visitor_name only
        mock_input.side_effect = [
            "V001",        # visit_id
            "NewVisitor",  # visitor_name
            "",            # visit_date
            "",            # outcome
            ""             # notes
        ]

        visits.update_visit()
        mock_update.assert_called_once()

    # Condition: visit does not exist → False branch
    @patch("modules.visits.ds.get_by_id", return_value=None)
    @patch("builtins.input", return_value="V999")
    def test_visit_does_not_exist(self, mock_input, mock_get):
        visits.update_visit()
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
