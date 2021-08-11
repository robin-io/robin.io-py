import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import unittest
from sdk import Robin


robin_test = Robin("NT-LSTTNiKdEQyAagVBdhKtoqqTEhbXGGZxaQbp", True)

class BaseCase(unittest.TestCase):
    def test_create_single_conversation_success(self):
        actual = robin_test.create_conversation(sender_token="IZiawwHPpHeE", sender_name="Elvis Mike", receiver_token="IZiawwHPpHeE", receiver_name="Ayo Onas")
        print(actual)
        self.assertIsNotNone(actual)

    def test_get_conversation_success(self):
        actual = robin_test.get_conversation(id="610041ac411c882b47d633db")
        print(actual)
        self.assertIsNotNone(actual)
    
    def test_search_message_success(self):
        actual = robin_test.search_message(id="610041ac411c882b47d633db", text="")
        print(actual)
        self.assertIsNotNone(actual)

    def test_delete_message_success(self):
        actual = robin_test.delete_message(id="610041ac411c882b47d633db")
        print(actual)
        self.assertIsNotNone(actual)


    def test_create_group_conversation_success(self):
        moderator_data = {
            "user_token":"IZiawwHPpHeE",
            "meta_data": {
                "name": "Elvis Chuks"
            }
        }

        
        participants_data = [
            {
                "user_token":"IZiawwHPpHeE",
                "meta_data": {
                    "name": "Josheph Ewu"
                }
            }
        ] 
        actual = robin_test.create_group_conversation(group_name="Sams Test Group", moderator=moderator_data, participants=participants_data)
        print(actual)
        self.assertIsNotNone(actual)

    def test_add_group_participants_success(self):
       
        participants_data = [
            {
                "user_token":"IZiawwHPpHeE",
                "meta_data": {
                    "name": "Josheph Ewu"
                }
            }
        ] 
        actual = robin_test.add_group_participants(group_id="6103ee6628e71d0daf8dcd03", participants=participants_data)
        print(actual)
        self.assertIsNotNone(actual)

    def test_remove_group_participants_success(self):
        
        actual = robin_test.remove_group_participants(user_token="YFXOKVyKBGvHxuBaqKgDWOhE", group_id="6103ee6628e71d0daf8dcd03")
        print(actual)
        self.assertIsNotNone(actual)

    def test_assign_group_moderator(self):

        actual = robin_test.assign_group_moderator(user_token="YFXOKVyKBGvHxuBaqKgDWOhE", group_id="6103ee6628e71d0daf8dcd03")
        print(actual)
        self.assertIsNotNone(actual)




if __name__ == '__main__':
    unittest.main()