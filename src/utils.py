import json

def load_json(path):
    with open(path) as raw_file:
        config = json.load(raw_file)
    return config