import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import unittest
from robin import Robin


robin_test = Robin("NT-QuNtKolpzoWLahimkIjGAllEcJwGrymaVxQX", True)

class BaseCase(unittest.TestCase):
    def test_connect_success(self):
        robin_test.connect(user_token="IZiawwHPpHeE")

        chann = robin_test.create_channel("test")
        subscription = robin_test.subscribe(chann)
        print(subscription)
        message = robin_test.send_message({"msg": "hello"}, chann)
        print(message)

        

    

if __name__ == '__main__':
    unittest.main()