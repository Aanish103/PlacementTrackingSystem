# Loop Testing

import sys
import os
import unittest
from unittest.mock import patch

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import applications


class TestShowAllApplications_Loop(unittest.TestCase):

    @patch("modules.applications.ds.applications", new=[])
    def test_zero_applications(self):
        applications.show_all_applications()

    @patch("modules.applications.ds.get_by_id", side_effect=[
        # student
        {
            "student_id": "S1",
            "name": "John Doe",
            "dob": "01/01/2000",
            "address": "Addr1",
            "qualification": "BSc",
            "grad_year": "2022",
            "school_id": "SC001"
        },
        # school
        {
            "school_id": "SC001",
            "school_name": "ABC School",
            "location": "City"
        }
    ])
    @patch("modules.applications.ds.applications", new=[
        {
            "application_id": "AP001",
            "student_id": "S1",
            "employer": "ABC",
            "role": "Intern",
            "start_date": "01/01/2025",
            "end_date": "01/06/2025",
            "status": "Approved",
            "documents": []
        }
    ])
    def test_one_application(self, mock_get):
        applications.show_all_applications()

    @patch("modules.applications.ds.get_by_id", side_effect=[
        # student 1
        {
            "student_id": "S1",
            "name": "John Doe",
            "dob": "01/01/2000",
            "address": "Addr1",
            "qualification": "BSc",
            "grad_year": "2022",
            "school_id": "SC001"
        },
        # school 1
        {
            "school_id": "SC001",
            "school_name": "ABC School",
            "location": "City"
        },
        # student 2
        {
            "student_id": "S2",
            "name": "Jane Doe",
            "dob": "02/02/2000",
            "address": "Addr2",
            "qualification": "BCom",
            "grad_year": "2023",
            "school_id": "SC002"
        },
        # school 2
        {
            "school_id": "SC002",
            "school_name": "XYZ School",
            "location": "Town"
        }
    ])
    @patch("modules.applications.ds.applications", new=[
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
        {
            "application_id": "AP002",
            "student_id": "S2",
            "employer": "XYZ",
            "role": "Intern",
            "start_date": "01/02/2025",
            "end_date": "01/07/2025",
            "status": "Pending",
            "documents": ["resume.pdf"]
        }
    ])
    def test_multiple_applications(self, mock_get):
        applications.show_all_applications()


class TestShowFullApplicationDetails_Loop(unittest.TestCase):

    @patch("builtins.input", return_value="AP001")
    @patch("modules.applications.ds.decisions", new=[])
    @patch("modules.applications.ds.visits", new=[])
    @patch("modules.applications.ds.assessments", new=[])
    @patch("modules.applications.ds.get_by_id", side_effect=[
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
        {
            "student_id": "S1",
            "name": "John Doe",
            "dob": "01/01/2000",
            "address": "Addr1",
            "qualification": "BSc",
            "grad_year": "2022",
            "school_id": "SC001"
        },
        {
            "school_id": "SC001",
            "school_name": "ABC School",
            "location": "City"
        }
    ])
    def test_zero_iterations(self, mock_input, mock_get):
        applications.show_full_application_details()


if __name__ == "__main__":
    unittest.main()
