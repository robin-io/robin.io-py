import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import unittest
from sdk import Robin


robin_test = Robin("NT-LSTTNiKdEQyAagVBdhKtoqqTEhbXGGZxaQbp", True)

class BaseCase(unittest.TestCase):
    def test_create_channel_success(self):
        actual = robin_test.create_channel(name=" ")
        print(actual)
        self.assertIsNotNone(actual)

if __name__ == '__main__':
    unittest.main()