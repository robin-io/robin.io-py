import requests

BASE_URL = "https://robbin-api.herokuapp.com/api/v1"

class Robin:

    def __init__(self, api_key, tls):

        self.api_key = api_key
        self.tls = tls
        self.HEADERS = {'content-type': 'application/json', 'x-api-key': self.api_key}

    
    def create_user_token(self, data):
        # defining a params dict for the parameters to be sent to the API
        DATA = data
        
        # sending post request and saving the response as response object
        r = requests.post(url = BASE_URL+"/chat/user_token", json=DATA, headers=self.HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        return data