# 1.In your workspace we’ve put dictionary called data_payload. We want to save this to a file called data.json.
# Let’s start by importing the json library.

# 2.Open a new file object in the variable data_json. The filename should be 'data.json' and the file should be opened in write-mode.

# 3.Call json.dump() with data_payload and data_json to convert our data to JSON and then save it to the file data.json.

import json
data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
     'follow up': 'But enough talk!'}
]


with open("data.json", "w") as data_json:
    json.dump(data_payload, data_json)
