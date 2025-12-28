import json

data = {
    "name": "Alex",
    "score": 5,
    "attempts": [3, 5, 2]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
