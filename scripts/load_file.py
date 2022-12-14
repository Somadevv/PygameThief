import json


def load_file(path):
    items = open(path)
    data = json.load(items)

    return data
