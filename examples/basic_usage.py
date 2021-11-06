import os

from robin import Robin
from flask import Flask, redirect, url_for, request

robin_key = os.environ.get("ROBIN_SECRET_KEY")

app = Flask(__name__)

"""
    some example usage of robin resources.
"""
@app.route('/channel',methods = ['POST'])
def create_channel():
    
    #initialize new robin module
    robin_test = Robin(robin_key, True)

    #create a new channel
    channel = robin_test.create_channel(name="Channel O")

    print(channel)

"""
    method to create direct conversation with robin
"""
@app.route('/conversation/direct/',methods = ['POST'])
def create_direct_conversation():

    #initialize new robin module
    robin_test = Robin(robin_key, True)

    #create a new conversation
    conversation = robin_test.create_conversation(sender_token="IZiawwHPpHeE", sender_name="Elvis Mike", receiver_token="IZiawwHPpHeE", receiver_name="Ayo Onas")

    print(conversation)

"""
    method to create group conversation with robin
"""
@app.route('/conversation/group/',methods = ['POST'])
def create_group_conversation():

    #initialize new robin module
    robin_test = Robin(robin_key, True)

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

    #create a new conversation
    conversation = robin_test.create_group_conversation(group_name="Robin Test Group", moderator=moderator_data, participants=participants_data)

    print(conversation)

"""
    method to search message in a conversation with robin
"""
@app.route('/conversation/search/<conversation_id>/<search_text>',methods = ['GET'])
def search_message():
    
    #initialize new robin module
    robin_test = Robin(robin_key, True)

    #search message in a conversation
    response = robin_test.search_message(id=conversation_id, text=search_text)

    print(response)

"""
    method to delete message in a conversation with robin
"""
@app.route('/conversation/delete/',methods = ['DELETE'])
def delete_message():
    
    #initialize new robin module
    robin_test = Robin(robin_key, True)

    #delete message in a conversation
    response = robin_test.delete_message(id="610041ac411c882b47d633db")

    print(response)

"""
    method to get a conversation with robin
"""
@app.route('/conversation/<conversation_id>',methods = ['GET'])
def get_conversation(conversation_id):
    
    #initialize new robin module
    robin_test = Robin(robin_key, True)

    #retrieve all data related to a conversation
    response = robin_test.get_conversation(id=conversation_id)

    print(response)

"""
    method to send message with attachements like images, files in a conversation with robin
"""
@app.route('/conversation/send/attachment/',methods = ['POST'])
def send_message_attachment():
    
    #initialize new robin module
    robin_test = Robin(robin_key, True)

    uploaded_file = request.files['file']

    #search message in a conversation
    response = robin_test.send_message_attachment(user_token="IZiawwHPpHeE", conversation_id="610041ac411c882b47d633db", file=uploaded_file)

    print(response)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))