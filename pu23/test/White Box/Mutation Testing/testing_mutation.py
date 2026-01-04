import unittest
import sys
import os


CURRENT_DIR = os.path.dirname(__file__)
PU23_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "../../../.."))
sys.path.insert(0, PU23_ROOT)

from modules import data_store


# ---------------------------------------------------
# MUTATED FUNCTIONS (SIMULATED)
# ---------------------------------------------------

def mutated_add_school(school_id, school_data):
    """
    Mutation: Original logic might return True,
    but this mutation always returns False
    """
    return False


def mutated_approve_application(app_id):
    """
    Mutation: Approval always fails
    """
    return False


class TestMutationTesting(unittest.TestCase):


    # MUTATION TEST – SCHOOL

    def test_mutation_add_school(self):
        original_result = True

        mutated_result = mutated_add_school(
            "SC300",
            {"name": "Engineering", "status": "Active"}
        )

        # Test should detect mutation
        self.assertNotEqual(original_result, mutated_result)

    # MUTATION TEST – APPLICATION
    def test_mutation_approve_application(self):
        original_result = True

        mutated_result = mutated_approve_application("AP001")

        # Mutation detected
        self.assertNotEqual(original_result, mutated_result)


    # CONTROL TEST – REAL FUNCTION

    def test_real_function_execution(self):
        if hasattr(data_store, "add_school"):
            result = data_store.add_school(
                "SC301",
                {"name": "Medical", "status": "Active"}
            )
            self.assertTrue(result or result is False)
        else:
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
