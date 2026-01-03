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
from modules import applications  # Assuming find_application_by_id() is here


class TestDeletePlacementStaff_BranchCoverage(unittest.TestCase):

    @patch("modules.placement_staffs.ds.delete_staff", return_value=True)
    @patch("builtins.input", return_value="ST001")
    def test_valid_staff_id(self, mock_input, mock_delete):
        # Branch: staff exists → deletion success
        placement_staffs.delete_placement_staff()
        mock_delete.assert_called_once()

    @patch("modules.placement_staffs.ds.delete_staff", return_value=False)
    @patch("builtins.input", return_value="ST999")
    def test_invalid_staff_id(self, mock_input, mock_delete):
        # Branch: staff does not exist → print "staff_id not found."
        placement_staffs.delete_placement_staff()
        mock_delete.assert_called_once()


class TestDeleteVisit_BranchCoverage(unittest.TestCase):

    @patch("modules.visits.ds.delete_visit", return_value=True)
    @patch("builtins.input", return_value="V001")
    def test_valid_visit_id(self, mock_input, mock_delete):
        # Branch: visit exists → deletion success
        visits.delete_visit()
        mock_delete.assert_called_once()

    @patch("modules.visits.ds.delete_visit", return_value=False)
    @patch("builtins.input", return_value="V999")
    def test_invalid_visit_id(self, mock_input, mock_delete):
        # Branch: visit does not exist → print "Visit ID not found."
        visits.delete_visit()
        mock_delete.assert_called_once()


class TestFindApplication_BranchCoverage(unittest.TestCase):

    @patch("modules.applications.ds.get_by_id")
    @patch("builtins.input", return_value="AP001")
    def test_valid_application_id(self, mock_input, mock_get):
        # Branch: application found
        mock_get.side_effect = [
            {
                "application_id": "AP001",
                "student_id": "S1",
                "employer": "ABC Corp",
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
        mock_get.assert_called()

    @patch("modules.applications.ds.get_by_id")
    @patch("builtins.input", return_value="AP999")
    def test_invalid_application_id(self, mock_input, mock_get):
        # Branch: application not found → print "application_id not found"
        mock_get.return_value = None
        applications.find_application_by_id()
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
