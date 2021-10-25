import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import unittest
from robin import Robin


robin_test = Robin("NT-LSTTNiKdEQyAagVBdhKtoqqTEhbXGGZxaQbp", True)

class BaseCase(unittest.TestCase):
    def test_create_user_token_success(self):
        actual = robin_test.create_user_token(data={
           "meta_data":{
                "name": "Samuel 0.",
            }
        })
        print(actual)
        self.assertIsNotNone(actual)

    def test_sync_user_token_success(self):
        actual = robin_test.sync_user_token(data={
            "user_token": "YFXOKVyKBGvHxuBaqKgDWOhE",
            "meta_data":{
                "email": "elvis@acumen.com.ng",
            }
        })
        print(actual)
        self.assertIsNotNone(actual)

    def test_get_user_token_success(self):
        actual = robin_test.get_user_token(data={
            "user_token": "YFXOKVyKBGvHxuBaqKgDWOhE",
            "meta_data":{
                "email": "elvis@acumen.com.ng",
            }
        })
        print(actual)
        self.assertIsNotNone(actual)

if __name__ == '__main__':
    unittest.main()