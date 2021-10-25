import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import unittest
from robin import Robin


robin_test = Robin("NT-LSTTNiKdEQyAagVBdhKtoqqTEhbXGGZxaQbp", True)

class BaseCase(unittest.TestCase):
    def test_create_support_staff_success(self):
        actual = robin_test.create_support_staff(user_token="YFXOKVyKBGvHxuBaqKgDWOhE")
        print(actual)
        self.assertIsNotNone(actual)

    def test_get_support_staff_success(self):
        actual = robin_test.create_support_staff(support_name="Bayo Support")
        print(actual)
        self.assertIsNotNone(actual)

    

if __name__ == '__main__':
    unittest.main()