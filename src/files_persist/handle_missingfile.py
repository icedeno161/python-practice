import json
from pathlib import Path

file_path = Path("data.json")

if file_path.exists():
    with open(file_path, "r") as file:
        data = json.load(file)
else:
    data = {}

print(data)