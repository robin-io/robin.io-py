<h1 align="start">
  Robin.io-py
</h1>

[![PyPI version](https://badge.fury.io/py/stream-chat.svg)](http://badge.fury.io/py/stream-chat) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stream-chat.svg)


## Table of contents

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#prerequisites">Prerequisites</a>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#sending-your-first-message">Sending your first message</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<br />

[View Documentation Here](https://robin-io-js-doc-csgdc.ondigitalocean.app/classes/Robin.html)

## Introduction

Robin.io-py is a Python SDK built to communicate with the [Robinapp API](https://robinapp.co/). Now you can integrate [Robin.io](https://robinapp.co/) with minimal effort and quickly setup a real-time messaging platform in your Web application.

## Prerequisites

The following packages are required to use the sdk:
* Requests
* Websocket-Client

## Getting started

#### Step 1: Create a Robinapp account

A Robinapp account comprises everything required in a chat service including users, message, and api-keys. To create an application:

1. Go to the [Robinapp Dashboard](https://dashboard.robinapp.co/signup) and enter your email and password, and create a new account.
2. Navigate to [Api Config](https://dashboard.robinapp.co/apiconfig) and copy your `API key`

> Note: All the data is limited to the scope of a single user account, thus the users in different Robinapp accounts are unable to chat with each other.

#### Step 2: Install the Chat SDK

```
  ## PIP

  pip3 install robin.io-py
```

## Sending your first message

Follow the step-by-step instructions below to authenticate and send your first message.

### Authentication

To use the features of the Chat SDK in your client app, a `robin` instance must be initiated in each client app before user authentication with Robin server. These instances communicate and interact with the server based on an authenticated user account, allowing for the client app to use the Chat SDK features.

### Step 1: Initialize the Chat SDK

You need to initialize a `robin` instance before authentication. Initialization binds the Chat SDK to Javascript’s context which allows the Chat SDK to respond to connection, state changes and also enables client apps to use the Chat SDK features.

To initialize a `Robin` instance, pass the `API key` as the first argument to in the `new Robin()` method, You can find your API key in the API Configuration tab in your [Robin Account](https://robin-user.herokuapp.com/apiconfig).

Then `true` or `false` for as the second parameter as it tells the sdk whether to load with ssl or not. As the `new Robin()` can only be a single instance, call it only a single time across your Javascript client app. Typically, initialization is implemented in the user login screen.

> **Note**: It is recommended to initialize the Chat SDK at the top of your Javascript file.

```python
robin = Robin("<api_key>", True)
```

### Step 2: Connect to Robin server

You'll need a **USER_TOKEN** to connect to the Robin server.

#### A. Create User Token

Create user token

```python
response = robin.create_user_token(data={
    "meta_data":{
        "name": "Samuel 0.",
    }
})
```

Connect to the Robin server using the **USER_TOKEN** you just created.

```python
robin.connect(user_token="<api_key>")
```

### Step 3: Channels

All messages sent via Robin are sent through channels, you can consider channels as tunnels that relay messages to all connected clients.

### Step 4: Create a conversation

Before we can send a message to a channel we first need to create a converstion.

```python
response = robin.create_conversation(sender_token="<sender_token>", sender_name="<sender_name>", receiver_token="<reciever_token>", receiver_name="<reciever_name>")    
```

### Step 5: Send a message to a conversation

Finally, send a message to a conversation.

```python
robin.send_conversation_message(msg={}, channel="<channel_id>", conversation_id="<conversation_id>", sender_token="<sender_token>")
```

#### Options

The following are general attributes used in Robin:

|   Attribute    |   Type    | Default | Description                                              |
| :------------: | :-------: | :-----: | :------------------------------------------------------- |
|      Conn      | WebSocket |  null   | Websocket opbject returned after calling robin.connect() |
|  sender_name   |  String   |   ''    | Name of the person sending the message                   |
|  sender_token  |  String   |   ''    | USER_TOKEN of the person sending the message             |
| receiver_name  |  String   |   ''    | Name of the person receiving the message                 |
| receiver_token |  String   |   ''    | USER_TOKEN of the person receiving the message           |
|      msg       |  Object   |   {}    | Json serializable object containing the message          |

If you have any comments or questions regarding bugs and feature requests, visit [Robinapp community](https://community.robinapp.co).

[View Documentation Here]().

## License

Distributed under the MIT License. See `LICENSE` for more information.