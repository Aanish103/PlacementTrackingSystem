import unittest
import sys
import os

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store


class TestBoundaryValue(unittest.TestCase):

    def setUp(self):
        self.orig_assessments = list(data_store.assessments)
        self.orig_applications = list(data_store.applications)

    def tearDown(self):
        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)

        data_store.applications.clear()
        data_store.applications.extend(self.orig_applications)

# Add Assessment

    def test_add_assessment_score_lower_boundary(self):
        aid = data_store.add_assessment("AP001", 0, "Pass", "Min score")
        self.assertIsNotNone(aid)

    def test_add_assessment_score_upper_boundary(self):
        aid = data_store.add_assessment("AP001", 100, "Pass", "Max score")
        self.assertIsNotNone(aid)

    def test_add_assessment_score_below_min(self):
        aid = data_store.add_assessment("AP001", -1, "Fail", "Invalid low")
        self.assertIsNotNone(aid)

    def test_add_assessment_score_above_max(self):
        aid = data_store.add_assessment("AP001", 101, "Fail", "Invalid high")
        self.assertIsNotNone(aid)

# Update Assessment

    def test_update_assessment_score_lower_boundary(self):
        result = data_store.update_assessment("AS001", {"score": 0})
        self.assertTrue(result)

    def test_update_assessment_score_upper_boundary(self):
        result = data_store.update_assessment("AS001", {"score": 100})
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()