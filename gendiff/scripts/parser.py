import json
import yaml
import os


def parse(path):
    with open(os.path.abspath(path)) as f:
        if path.endswith('.json'):
            data = json.load(f)
        elif path.endswith('.yml'):
            data = yaml.safe_load(f)
        else:
            raise ValueError('.yml and .json formats are only supported')
    return data
