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
from modules import applications  # <- this is where find_application_by_id() is actually defined


class TestFindApplication_BVA(unittest.TestCase):

    @patch("modules.applications.ds.get_by_id")
    @patch("builtins.input")
    def test_empty_application_id(self, mock_input, mock_get):
        """Boundary: Empty input"""
        mock_input.return_value = ""
        mock_get.return_value = None

        applications.find_application_by_id()
        mock_get.assert_called_once()

    @patch("modules.applications.ds.get_by_id")
    @patch("builtins.input")
    def test_min_valid_application_id(self, mock_input, mock_get):
        """Boundary: Minimum valid ID"""
        mock_input.return_value = "AP001"

        mock_get.side_effect = [
            {
                "application_id": "AP001",
                "student_id": "S1",
                "employer": "ABC",
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

    @patch("modules.applications.ds.get_by_id")
    @patch("builtins.input")
    def test_invalid_application_id(self, mock_input, mock_get):
        """Boundary: Invalid ID"""
        mock_input.return_value = "AP999"
        mock_get.return_value = None

        applications.find_application_by_id()


class TestDeletePlacementStaff_BVA(unittest.TestCase):

    @patch("modules.placement_staffs.ds.delete_staff", return_value=False)
    @patch("builtins.input")
    def test_empty_staff_id(self, mock_input, mock_delete):
        """Boundary: Empty staff_id"""
        mock_input.return_value = ""

        placement_staffs.delete_placement_staff()
        mock_delete.assert_called_once()

    @patch("modules.placement_staffs.ds.delete_staff", return_value=True)
    @patch("builtins.input")
    def test_valid_staff_id(self, mock_input, mock_delete):
        """Boundary: Minimum valid staff_id"""
        mock_input.return_value = "ST001"

        placement_staffs.delete_placement_staff()
        mock_delete.assert_called_once()

    @patch("modules.placement_staffs.ds.delete_staff", return_value=False)
    @patch("builtins.input")
    def test_invalid_staff_id(self, mock_input, mock_delete):
        """Boundary: Invalid staff_id"""
        mock_input.return_value = "ST999"

        placement_staffs.delete_placement_staff()


class TestDeleteVisit_BVA(unittest.TestCase):

    @patch("modules.visits.ds.delete_visit", return_value=False)
    @patch("builtins.input")
    def test_empty_visit_id(self, mock_input, mock_delete):
        """Boundary: Empty visit_id"""
        mock_input.return_value = ""

        visits.delete_visit()
        mock_delete.assert_called_once()

    @patch("modules.visits.ds.delete_visit", return_value=True)
    @patch("builtins.input")
    def test_valid_visit_id(self, mock_input, mock_delete):
        """Boundary: Minimum valid visit_id"""
        mock_input.return_value = "V001"

        visits.delete_visit()
        mock_delete.assert_called_once()

    @patch("modules.visits.ds.delete_visit", return_value=False)
    @patch("builtins.input")
    def test_invalid_visit_id(self, mock_input, mock_delete):
        """Boundary: Invalid visit_id"""
        mock_input.return_value = "V999"

        visits.delete_visit()


if __name__ == "__main__":
    unittest.main()
