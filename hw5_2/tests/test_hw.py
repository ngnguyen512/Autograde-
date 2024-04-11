import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    import hw5_2a as student_module
except ImportError:
    raise Exception('Could not import hw5_2a. Ensure the file is named correctly and contains a main() function.')

try:
    import solution.hw5_2a as solution_module
except ImportError:
    raise Exception('Could not import solution for hw5_2a. Ensure the solution file is named correctly and contains a main() function.')

class TestGCD(unittest.TestCase):
    def simulate_input(self, func, inputs):
        """Simulates input for given function by patching 'input' and 'print'."""
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            func()
        return mock_stdout.getvalue()
    @weight(10)
    def test_hw(self):
        """Tests the GCD calculation by comparing student submission against the solution."""
        test_cases = [
            ["18", "21"],
            ["30", "12"],
            ["-10", "15"],
            ["3", "8"],
            ["42", "56"],
            ["11", "13"],
            ["0", "0"],  # Handling edge cases
            ["-24", "-36"],
        ]

        for inputs in test_cases:
            expected_output = self.simulate_input(solution_module.main, inputs)
            # Actual output using submission module
            actual_output = self.simulate_input(student_module.main, inputs)
            self.assertEqual(expected_output, actual_output, f"Failed at inputs = {inputs}")
