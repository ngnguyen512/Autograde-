import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw3_2 as hw3_2
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw3_2 as solution
import random
import math

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            hw3_2.main()
        return mock_stdout.getvalue()
    
    #def setUpTestFile(self, number):
        #file = open('test.txt', 'w')
        #fileContent = []
        #for i in range(number):
            #fileContent.append(str(random.uniform(0.0001,10000)) + "\n")
        #file.writelines(fileContent)
        #file.close()
 #   @visibility("hidden")
    @weight(10)    
    def test_hw(self):
        name = ["Katherine Perry", "Ha Nguyen", "Van Thanh Nguyen", "Hiroshi Nanoka"]
        for i in range(len(name)):
            ans = self.setUpAns(name[i])
            submission = self.setUpSub(name[i])
            self.assertEqual(ans, submission)


    
