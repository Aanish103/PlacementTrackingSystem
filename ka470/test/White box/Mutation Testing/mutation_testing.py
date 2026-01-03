import sys
import os
import unittest
from unittest.mock import patch

# PROJECT ROOT
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, PROJECT_ROOT)

from modules import visits, placement_staffs


class TestDeleteVisit_Mutation(unittest.TestCase):

    @patch("builtins.input", return_value="V001")
    @patch(
        "modules.visits.ds.visits",
        new=[
            {
                "visit_id": "V001",
                "visitor_name": "Visitor1",
                "visit_date": "01/01/2025",
                "outcome": "Neutral",
                "notes": "Check"
            },
            {
                "visit_id": "V002",
                "visitor_name": "Visitor2",
                "visit_date": "02/01/2025",
                "outcome": "Positive",
                "notes": "None"
            }
        ]
    )
    def test_delete_existing_visit(self, mock_input):
        visits.delete_visit()

        visit_ids = [v["visit_id"] for v in visits.ds.visits]
        self.assertNotIn("V001", visit_ids)
        self.assertIn("V002", visit_ids)

    @patch("builtins.input", return_value="V999")
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
    def test_delete_non_existing_visit(self, mock_input):
        visits.delete_visit()

        self.assertEqual(len(visits.ds.visits), 1)
        self.assertEqual(visits.ds.visits[0]["visit_id"], "V001")


class TestDeletePlacementStaff_Mutation(unittest.TestCase):

    @patch("builtins.input", return_value="PS001")
    @patch(
        "modules.placement_staffs.ds.placement_staffs",
        new=[
            {
                "staff_id": "PS001",
                "name": "Manager",
                "email": "m@mail.com",
                "phone": "9999999999",
                "role": "Officer"
            }
        ]
    )
    def test_delete_existing_staff(self, mock_input):
        placement_staffs.delete_placement_staff()

        self.assertEqual(len(placement_staffs.ds.placement_staffs), 0)

    @patch("builtins.input", return_value="PS999")
    @patch(
        "modules.placement_staffs.ds.placement_staffs",
        new=[
            {
                "staff_id": "PS001",
                "name": "Manager"
            }
        ]
    )
    def test_delete_non_existing_staff(self, mock_input):
        placement_staffs.delete_placement_staff()

        self.assertEqual(len(placement_staffs.ds.placement_staffs), 1)
        self.assertEqual(
            placement_staffs.ds.placement_staffs[0]["staff_id"], "PS001"
        )


if __name__ == "__main__":
    unittest.main()
