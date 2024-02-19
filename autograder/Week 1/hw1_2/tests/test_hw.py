import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight
try:
    import hw1_2 as hw1_2
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw1_2 as solution

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            hw1_2.main()
        return mock_stdout.getvalue()
    
    @weight(10)
    def test_hw(self):
        m = [2, 5, 10, 30, 50, 60]
        for i in range(len(m)):
            ans = self.setUpAns(m[i])
            submission = self.setUpSub(m[i])
            self.assertEqual(ans, submission, "Failed at m = " + str(m[i]))
            
    
