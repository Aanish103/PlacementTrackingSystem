import unittest
import random
import string
import sys
import os

# Project's Root Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from modules import data_store


class TestRandomTesting(unittest.TestCase):

    def setUp(self):
        self.orig_apps = list(data_store.applications)
        self.orig_assessments = list(data_store.assessments)

    def tearDown(self):
        data_store.applications.clear()
        data_store.applications.extend(self.orig_apps)

        data_store.assessments.clear()
        data_store.assessments.extend(self.orig_assessments)

# Add Application
    def test_add_application_random_inputs(self):
        for _ in range(5):
            student_id = random.choice(["ST001", "", "ST999"])
            employer = ''.join(random.choices(string.ascii_letters, k=5))
            role = ''.join(random.choices(string.ascii_letters, k=4))
            start = "2025-06-01"
            end = "2025-09-01"
            docs = random.choice([["CV.pdf"], [], "INVALID"])

            try:
                result = data_store.add_application(
                    student_id, employer, role, start, end, docs
                )
                self.assertIsNotNone(result)
            except (TypeError, ValueError):
                pass

# Update Application

    def test_update_application_random(self):
        for _ in range(5):
            app_id = random.choice(["AP001", "INVALID"])
            status = random.choice(["Approved", "Rejected", "", None])

            try:
                result = data_store.update_application(app_id, status)
                self.assertIn(result, [True, False])
            except (TypeError, ValueError):
                pass




# Add Assessment

    def test_add_assessment_random(self):
        for _ in range(5):
            app_id = random.choice(["AP001", "INVALID"])
            score = random.randint(-10, 120)
            result = random.choice(["Pass", "Fail", ""])

            try:
                aid = data_store.add_assessment(app_id, score, result, "Random test")
                self.assertIsNotNone(aid)
            except (TypeError, ValueError):
                pass



# Update Assessment

    def test_update_assessment_random(self):
        for _ in range(5):
            as_id = random.choice(["AS001", "INVALID"])
            score = random.randint(-10, 120)

            try:
                result = data_store.update_assessment(as_id, score)
                self.assertIn(result, [True, False])
            except (TypeError, ValueError):
                pass


if __name__ == "__main__":
    unittest.main()
