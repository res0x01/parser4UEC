import json
json_filename = "output.json"

with open(json_filename) as f:
    data = json.load(f)

print(data)
