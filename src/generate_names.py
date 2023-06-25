import json

json_file = "assets/names.json"

with open(json_file) as json_data:
    data = json.load(json_data)

