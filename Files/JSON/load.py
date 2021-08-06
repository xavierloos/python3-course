# 1.Let’s read a JSON file! Start by importing the json module.

# 2.Open up the file message.json, saving the file object to the variable message_json.
# Open the file in read-mode, without passing any additional arguments to open().

import json

with open("message.json") as message_json:
    message = json.load(message_json)

print(message['text'])
