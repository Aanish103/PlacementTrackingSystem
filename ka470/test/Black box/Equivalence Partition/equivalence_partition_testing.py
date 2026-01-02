import sys
import os
import unittest
from unittest.mock import patch


PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import placement_staffs
from modules import visits, applications


class TestAddPlacementStaff_EP(unittest.TestCase):

    @patch("modules.placement_staffs.ds.add_staff", return_value="ST001")
    @patch("builtins.input")
    def test_valid_inputs(self, mock_input, mock_add):
        mock_input.side_effect = [
            "Alice",
            "alice@mail.com",
            "9876543210",
            "Admin"
        ]

        placement_staffs.add_placement_staff()
        mock_add.assert_called_once()


class TestUpdatePlacementStaff_EP(unittest.TestCase):

    @patch("modules.placement_staffs.ds.get_by_id")
    @patch("modules.placement_staffs.ds.update_staff", return_value=True)
    @patch("builtins.input")
    def test_valid_staff_id_valid_inputs(self, mock_input, mock_update, mock_get):

        mock_get.return_value = {
            "name": "Old Name",
            "email": "old@mail.com",
            "phone": "1234567890",
            "role": "Admin"
        }

        mock_input.side_effect = [
            "ST001",        # valid staff_id
            "New Name",     # update name
            "",             # keep email
            "",             # keep phone
            ""              # keep role
        ]

        placement_staffs.update_placement_staff()
        mock_update.assert_called_once()


class TestAddVisit_EP(unittest.TestCase):

    @patch("modules.visits.ds.get_by_id")
    @patch("modules.visits.ds.add_visit", return_value="V001")
    @patch("builtins.input")
    def test_valid_application_id(self, mock_input, mock_add, mock_get):

        mock_get.return_value = {"application_id": "AP001"}

        mock_input.side_effect = [
            "AP001",
            "John",
            "01/01/2025",
            "Positive",
            "Good visit"
        ]

        visits.add_visit()
        mock_add.assert_called_once()


class TestUpdateVisit_EP(unittest.TestCase):

    @patch("modules.visits.ds.get_by_id")
    @patch("modules.visits.ds.update_visit", return_value=True)
    @patch("builtins.input")
    def test_valid_visit_id(self, mock_input, mock_update, mock_get):

        mock_get.return_value = {
            "visitor_name": "Old Visitor",
            "visit_date": "01/01/2024",
            "outcome": "OK",
            "notes": "None"
        }

        mock_input.side_effect = [
            "V001",
            "New Visitor",
            "",
            "",
            ""
        ]

        visits.update_visit()
        mock_update.assert_called_once()

class TestFindApplication_EP(unittest.TestCase):

    @patch("modules.placement_staffs.ds.get_by_id")
    @patch("builtins.input", return_value="AP001")
    def test_valid_application_id(self, mock_input, mock_get):

        mock_get.side_effect = [
            {
                "application_id": "AP001",
                "student_id": "S1",
                "employer": "ABC Ltd",
                "role": "Intern",
                "start_date": "01/01/2025",
                "end_date": "01/06/2025",
                "status": "Approved",
                "documents": []
            },
            None,
            None
        ]

        applications.find_application_by_id()

if __name__ == "__main__":
    unittest.main()
