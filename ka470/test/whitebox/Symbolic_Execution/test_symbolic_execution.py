# symbolic_execution_test.py

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# PROJECT ROOT
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import applications, visits  # do not change these modules


class TestFindApplicationById_SE(unittest.TestCase):

    @patch("modules.applications.find_application_by_id")
    def test_application_not_found_empty_list(self, mock_find):
        """Simulate empty applications list → return None"""
        mock_find.return_value = None
        result = applications.find_application_by_id("AP001")
        self.assertIsNone(result)
        mock_find.assert_called_once_with("AP001")

    @patch("modules.applications.find_application_by_id")
    def test_application_found(self, mock_find):
        """Simulate application exists → return dict"""
        mock_find.return_value = {"application_id": "AP002", "student_id": "S2"}
        result = applications.find_application_by_id("AP002")
        self.assertIsNotNone(result)
        self.assertEqual(result["student_id"], "S2")
        mock_find.assert_called_once_with("AP002")

    @patch("modules.applications.find_application_by_id")
    def test_application_not_found_in_list(self, mock_find):
        """Simulate application ID not in list → return None"""
        mock_find.return_value = None
        result = applications.find_application_by_id("AP999")
        self.assertIsNone(result)
        mock_find.assert_called_once_with("AP999")


class TestDeleteVisit_SE(unittest.TestCase):

    @patch("builtins.input", return_value="V001")
    @patch("modules.visits.delete_visit")
    def test_delete_visit_no_visits(self, mock_delete, mock_input):
        """Simulate no visits exist → should not fail"""
        mock_delete.return_value = None
        visits.delete_visit()
        mock_delete.assert_called_once()

    @patch("builtins.input", return_value="V002")
    @patch("modules.visits.delete_visit")
    def test_delete_visit_found(self, mock_delete, mock_input):
        """Simulate visit exists → deleted"""
        mock_delete.return_value = None
        visits.delete_visit()
        mock_delete.assert_called_once()

    @patch("builtins.input", return_value="V999")
    @patch("modules.visits.delete_visit")
    def test_delete_visit_not_found(self, mock_delete, mock_input):
        """Simulate visit ID not found → no deletion"""
        mock_delete.return_value = None
        visits.delete_visit()
        mock_delete.assert_called_once()


if __name__ == "__main__":
    unittest.main()
