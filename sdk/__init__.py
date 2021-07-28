import requests

BASE_URL = "https://robbin-api.herokuapp.com/api/v1"

class Robin:

    def __init__(self, api_key, tls):

        self.api_key = api_key
        self.tls = tls
        self.HEADERS = {'content-type': 'application/json', 'x-api-key': self.api_key}


    """
        Endpoints handling anything tokens
    """

    
    def create_user_token(self, data):
        # defining a params dict for the parameters to be sent to the API
        DATA = data
        
        # sending post request and saving the response as response object
        r = requests.post(url = BASE_URL+"/chat/user_token", json=DATA, headers=self.HEADERS)
        
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
        r = requests.put(url = BASE_URL+"/chat/user_token/"+data['user_token'], json=DATA, headers=self.HEADERS)
        
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
        r = requests.post(url = BASE_URL+"/conversation", json=DATA, headers=self.HEADERS)
        
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
        r = requests.get(url = BASE_URL+"/conversation/messages/"+id, headers=self.HEADERS)
        
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

        
