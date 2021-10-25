import requests
import websocket
import json
import _thread
import time

class Robin:

    def __init__(self, api_key, tls):

        self.api_key = api_key
        self.tls = tls

        if tls:
            self.WSURL = 'wss://robbin-api.herokuapp.com/ws'
            self.BASEURL = 'https://robbin-api.herokuapp.com/api/v1'
        else:
            self.WSURL = 'ws://robbin-api.herokuapp.com/ws'
            self.BASEURL = 'http://robbin-api.herokuapp.com/api/v1'

        self.HEADERS = {'content-type': 'application/json', 'x-api-key': self.api_key}


        

    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def on_open(self, ws):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            
        _thread.start_new_thread(run, ())
        


    """
        Endpoints handling anything tokens
        1. create users token.
        2. sync users token.
        3. get users token.
    """

    
    def create_user_token(self, data):
        # defining a params dict for the parameters to be sent to the API
        DATA = data
        
        # sending post request and saving the response as response object
        r = requests.post(url = self.BASE_URL+"/chat/user_token", json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def sync_user_token(self, data):
        # defining a params dict for the parameters to be sent to the API
        DATA = data
        
        # sending put request and saving the response as response object
        r = requests.put(url = self.BASE_URL+"/chat/user_token/"+data['user_token'], json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def get_user_token(self, data):
        # defining a params dict for the parameters to be sent to the API
        DATA = data
        
        # sending put request and saving the response as response object
        r = requests.get(url = self.BASE_URL+"/chat/user_token/"+data['user_token'])
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    """
        Endpoints handling anything conversations
        1. create conversations
        2. get conversations by ID
        3. delete conversation message
        4. create group conversations
        5. add group participants
        6. remove group participants
        7. assign group moderator
        8. search messages
        9. send message with attachment
        10. archive conversation
        11. unarchive conversation
        12. forward messages
    """

    def create_conversation(self, sender_token, sender_name, receiver_token, receiver_name):
        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "sender_name": sender_name,
            "sender_token": sender_token,
            "receiver_token": receiver_token,
            "receiver_name": receiver_name
        }
        
        # sending post request and saving the response as response object
        r = requests.post(url = self.BASE_URL+"/conversation", json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def get_conversation(self, id):

        # sending get request and saving the response as response object
        r = requests.get(url = self.BASE_URL+"/conversation/messages/"+id, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            if data["data"] is not None:
                return data["data"]
            else:
                return []

    def delete_message(self, id):
        # sending get request and saving the response as response object
        r = requests.delete(url = self.BASE_URL+"/chat/message/"+id, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            if data["data"] is not None:
                return data["data"]
            else:
                return []

    
    def create_group_conversation(self, group_name, moderator, participants):

        #checks
        if group_name == "":
            print("group name should not be empty")
            return None
        
        if not isinstance(participants, list):
            print("participants should be an array")
            return None

        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "name": group_name,
            "moderator": moderator,
            "participants": participants
        }

        # sending post request and saving the response as response object
        r = requests.post(url = self.BASE_URL+"/chat/conversation/group", json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def add_group_participants(self, group_id, participants):

        #checks
        if group_id == "":
            print("group id should not be empty")
            return None

        if not isinstance(participants, list):
            print("participants should be an array")
            return None
        
        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "participants": participants
        }

        # sending post request and saving the response as response object
        r = requests.put(url = self.BASE_URL+"/chat/conversation/group/add_participants/"+group_id, json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def remove_group_participants(self, user_token, group_id):

        #checks
        if user_token == "":
            print("user token cannot be empty")
            return None

        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "user_token": user_token
        }

        # sending post request and saving the response as response object
        r = requests.put(url = self.BASE_URL+"/chat/conversation/group/remove_participant/"+group_id, json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def assign_group_moderator(self, user_token, group_id):

        #checks
        if user_token == "":
            print("user token cannot be empty")
            return None

        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "user_token": user_token
        }

        # sending post request and saving the response as response object
        r = requests.put(url = self.BASE_URL+"/chat/conversation/group/assign_moderator/"+group_id, json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]
    
    def search_message(self, id, text):

        
        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "text": text,
        }

        # sending post request and saving the response as response object
        r = requests.post(url = self.BASE_URL+"/chat/search/message/"+id, json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def send_message_attachment(self, user_token, conversation_id, file):

        fd = {"sender_token":user_token, "conversation_id": conversation_id, "file": file}

         # sending post request and saving the response as response object
        r = requests.post(url = self.BASE_URL+"/conversation", json=DATA, files=fd, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    """
        Endpoints handling anything channels
        1. create channel
    """

    def create_channel(self, name):

        #check if the name is empty or contains just whitespace
        if len(name) == 0 or name.isspace():
            print("Channel name cannot be empty")
            return None

        data = {
            "name": name,
            "private_name": '-'.join(name.split()) +"-"+ self.api_key
        }

        print("creating channel...")

        return data

    """
        Endpoints handling anything support
        1. create support staff
        2. get support staff
    """

    def create_support_staff(self, user_token, support_name, support_id):
        #checks
        if user_token == "":
            print("user token cannot be empty")
            return None

        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "user_token": user_token,
            "support_name": support_name,
            "support_id": support_id
        }

        # sending post request and saving the response as response object
        r = requests.put(url = self.BASE_URL+"/chat/user_token/support", json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]

    def get_support_staff(self, support_name):

        #checks
        if support_name == "":
            print("support name cannot be empty")
            return None

        # defining a params dict for the parameters to be sent to the API
        DATA = {
            "support_name": support_name
        }
        
        # sending put request and saving the response as response object
        r = requests.get(url = self.BASE_URL+"/chat/user_token/support/"+DATA['support_name'])
        
        # extracting data in json format
        data = r.json()

        #return data
        if data["error"]:
            print(data["error"])
            return None
        else:
            return data["data"]
    

    """
        Endpoints handling anything websocket
        1. connect to websocket
        2. subscribe to websocket
        3. send message to websocket
        4. send conversation message to websocket
        5. create support ticket.
    """

    def connect(self, user_token):

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.WSURL,
                                on_open=self.on_open,
                                on_message=self.on_message,
                                on_error=self.on_error,
                                on_close=self.on_close)

        self.ws.run_forever()

    def subscribe(self, channel):
        msg = {
            "type": 0,
            "channel":  channel["name"],
            "content": {}
        }

        print("subscribing...")

        self.ws.send(json.dumps(msg, separators=(',', ':')))
        return

    def send_message(self, msg, channel):

        msg = {
            "type": 1,
            "channel":  channel["name"],
            "content": msg,
        }

        print("sending...")

        self.ws.send(json.dumps(msg, separators=(',', ':')))

    def send_conversation_message(self, msg, channel, conversation_id, sender_token):

        msg = {
            "type": 1,
            "channel":  channel,
            "content": msg,
            "conversation_id": conversation_id,
            "sender_token": sender_token
        }

        print("sending...")

        self.ws.send(json.dumps(msg, separators=(',', ':')))
        
    def create_support_ticket(self, msg, channel, support_name, sender_token, sender_name):
        
        msg = {
            "type": 1,
            "channel":  channel,
            "content": msg,
            "suppor_name": support_name,
            "sender_token": sender_token,
            "sender_name": sender_name
        }

        print("sending...")

        self.ws.send(json.dumps(msg, separators=(',', ':')))