import sys
import os
import unittest
from unittest.mock import patch

# --------------------------------------------------
# PROJECT ROOT
# --------------------------------------------------
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
from modules import placement_staffs
from modules import visits

# If show_all_applications() is in another module like applications.py:
from modules import applications  # or placement_staffs if it's defined there


# ==================================================
# UPDATE PLACEMENT STAFF – STATEMENT COVERAGE
# ==================================================
class TestUpdatePlacementStaff_StatementCoverage(unittest.TestCase):

    @patch("modules.placement_staffs.ds.get_by_id")
    @patch("modules.placement_staffs.ds.update_staff", return_value=True)
    @patch("builtins.input")
    def test_update_all_fields(self, mock_input, mock_update, mock_get):
        # Mock existing staff
        mock_get.return_value = {
            "name": "OldName",
            "email": "old@mail.com",
            "phone": "123456",
            "role": "Admin"
        }

        # Simulate user input for all fields
        mock_input.side_effect = [
            "ST001",        # staff_id
            "NewName",      # name
            "new@mail.com", # email
            "9876543210",   # phone
            "Manager"       # role
        ]

        placement_staffs.update_placement_staff()
        mock_update.assert_called_once()

    @patch("modules.placement_staffs.ds.get_by_id")
    @patch("modules.placement_staffs.ds.update_staff", return_value=False)
    @patch("builtins.input")
    def test_update_failure(self, mock_input, mock_update, mock_get):
        # Staff exists but update fails
        mock_get.return_value = {
            "name": "OldName",
            "email": "old@mail.com",
            "phone": "123456",
            "role": "Admin"
        }

        mock_input.side_effect = [
            "ST001", "", "", "", ""  # leave all fields empty
        ]

        placement_staffs.update_placement_staff()
        mock_update.assert_called_once()


# ==================================================
# UPDATE VISIT – STATEMENT COVERAGE
# ==================================================
class TestUpdateVisit_StatementCoverage(unittest.TestCase):

    @patch("modules.visits.ds.get_by_id")
    @patch("modules.visits.ds.update_visit", return_value=True)
    @patch("builtins.input")
    def test_update_some_fields(self, mock_input, mock_update, mock_get):
        # Mock existing visit
        mock_get.return_value = {
            "visitor_name": "OldVisitor",
            "visit_date": "01/01/2025",
            "outcome": "Neutral",
            "notes": "Old Notes"
        }

        # Simulate user input: update only visitor_name and leave others blank
        mock_input.side_effect = [
            "V001",           # visit_id
            "NewVisitor",     # visitor_name
            "",               # visit_date
            "",               # outcome
            ""                # notes
        ]

        visits.update_visit()
        mock_update.assert_called_once()


# ==================================================
# SHOW ALL APPLICATIONS – STATEMENT COVERAGE
# ==================================================
class TestShowAllApplications_StatementCoverage(unittest.TestCase):

    @patch("modules.applications.ds.applications", new_callable=list)
    @patch("modules.applications.ds.get_by_id")
    def test_no_applications(self, mock_get, mock_applications):
        # Empty applications list
        mock_applications.clear()  # ensure it's empty
        applications.show_all_applications()

    @patch("modules.applications.ds.applications", new_callable=list)
    @patch("modules.applications.ds.get_by_id")
    def test_with_applications(self, mock_get, mock_applications):
        # Simulate applications present
        mock_applications.append({
            "application_id": "AP001",
            "student_id": "S1",
            "employer": "ABC Corp",
            "role": "Intern",
            "start_date": "01/01/2025",
            "end_date": "01/06/2025",
            "status": "Approved",
            "documents": []
        })

        # Mock get_by_id for student and school
        mock_get.side_effect = [
            {"student_id": "S1", "name": "John Doe", "school_id": "SC001"},
            {"school_id": "SC001", "school_name": "XYZ School"}
        ]

        applications.show_all_applications()


# --------------------------------------------------
# RUN TESTS
# --------------------------------------------------
if __name__ == "__main__":
    unittest.main()
