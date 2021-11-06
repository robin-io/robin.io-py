import os

from robin import Robin
from flask import Flask, request

robin_key = os.environ.get("ROBIN_SECRET_KEY")

app = Flask(__name__)

"""
    method to create direct conversation with robin
"""

def create_direct_conversation():

    #initialize new robin module
    robin_test = Robin(robin_key, True)

    #create a new conversation
    conversation = robin_test.create_conversation(sender_token="IZiawwHPpHeE", sender_name="Elvis Mike", receiver_token="IZiawwHPpHeE", receiver_name="Ayo Onas")

    print(channel)



if __name__ == "__main__":
    #app.run(port=int(os.environ.get("PORT", 5000)))
    create_direct_conversation()