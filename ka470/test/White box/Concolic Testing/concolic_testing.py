import sys
import os
import unittest
from unittest.mock import patch

# PROJECT ROOT
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import placement_staffs, visits


# ==================================================
# UPDATE PLACEMENT STAFF – CONCOLIC TESTING
# ==================================================
class TestUpdatePlacementStaff_Concolic(unittest.TestCase):

    @patch(
        "modules.placement_staffs.ds.placement_staffs",
        new=[{
            "staff_id": "PS001",
            "name": "Old Manager",
            "email": "old@mail.com",
            "phone": "900001",
            "role": "Officer"
        }]
    )
    @patch(
        "builtins.input",
        side_effect=[
            "PS001",           # staff_id
            "New Manager",     # name
            "new@mail.com",    # email
            "7896541235",      # phone
            "Officer"          # role
        ]
    )
    def test_update_existing_staff(self, mock_input):
        placement_staffs.update_placement_staff()

        staff = placement_staffs.ds.placement_staffs[0]
        self.assertEqual(staff["name"], "New Manager")
        self.assertEqual(staff["email"], "new@mail.com")
        self.assertEqual(staff["phone"], "7896541235")
        self.assertEqual(staff["role"], "Officer")

    @patch(
        "modules.placement_staffs.ds.placement_staffs",
        new=[{
            "staff_id": "PS001",
            "name": "Old Manager",
            "email": "old@mail.com",
            "phone": "900001",
            "role": "Officer"
        }]
    )
    @patch(
        "builtins.input",
        side_effect=[
            "PS999", "X", "x@mail.com", "123", "X"
        ]
    )
    def test_update_non_existing_staff(self, mock_input):
        placement_staffs.update_placement_staff()

        staff = placement_staffs.ds.placement_staffs[0]
        self.assertEqual(staff["name"], "Old Manager")


# ==================================================
# UPDATE VISIT – CONCOLIC TESTING
# ==================================================
class TestUpdateVisit_Concolic(unittest.TestCase):

    @patch(
        "modules.visits.ds.visits",
        new=[
            {
                "visit_id": "V001",
                "visitor_name": "Visitor1",
                "visit_date": "01/01/2025",
                "outcome": "Neutral",
                "notes": "Check"
            }
        ]
    )
    @patch(
        "builtins.input",
        side_effect=[
            "V001",
            "Updated Visitor",
            "02/02/2025",
            "Positive",
            "All good"
        ]
    )
    def test_update_existing_visit(self, mock_input):
        visits.update_visit()

        visit = visits.ds.visits[0]
        self.assertEqual(visit["visitor_name"], "Updated Visitor")
        self.assertEqual(visit["visit_date"], "02/02/2025")
        self.assertEqual(visit["outcome"], "Positive")
        self.assertEqual(visit["notes"], "All good")

    @patch(
        "modules.visits.ds.visits",
        new=[
            {
                "visit_id": "V001",
                "visitor_name": "Visitor1",
                "visit_date": "01/01/2025",
                "outcome": "Neutral",
                "notes": "Check"
            }
        ]
    )
    @patch(
        "builtins.input",
        side_effect=[
            "V999", "X", "01/01/2025", "Neutral", "Note"
        ]
    )
    def test_update_non_existing_visit(self, mock_input):
        visits.update_visit()

        self.assertEqual(len(visits.ds.visits), 1)
        self.assertEqual(visits.ds.visits[0]["visitor_name"], "Visitor1")


if __name__ == "__main__":
    unittest.main()
