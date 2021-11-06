import os

from robin import Robin
from flask import Flask, request

robin_key = os.environ.get("ROBIN_SECRET_KEY")

app = Flask(__name__)



def example():
    """
    some example usage of robin resources.
    """

    #initialize new robin module
    robin_test = Robin(robin_key, True)


    #create a new channel
    channel = robin_test.create_channel(name="Channel O")

    print(channel)



if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))