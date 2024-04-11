import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw5_2b
except Exception:
    raise Exception(f'Could not process your file. Remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw5_2b as solution

class TestHW(unittest.TestCase):
    def simulate_input(self, func, inputs):
        """Simulates input for given function by patching 'input' and 'print'."""
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            func()
        return mock_stdout.getvalue()
    @weight(10)
    def test_hw(self):
        # List of inputs to simulate user input sequence for each test case
        test_cases = [
            ["18", "21", ""],
            ["30", "12", ""],
            ["-10", "15", "95", ""],
            ["3", "6", "42", ""],
            ["3", "6", "7", ""],
            ["20", "50", "120", ""],
            ["81", "27", "-9", ""], 
            ["11", "13", "17", "19", ""],
            ["64", "-32", "96", ""], 
            ["0", "0", "5", ""], 
            ["0", "0", "0", ""]
        ]

        for inputs in test_cases:
            # Expected output using solution module
            expected_output = self.simulate_input(solution.main, inputs)
            # Actual output using submission module
            actual_output = self.simulate_input(hw5_2b.main, inputs)
            self.assertEqual(expected_output, actual_output, f"Failed at inputs = {inputs}")


