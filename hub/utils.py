import yaml
import json

def get_info(path):
    if path.endswith("yaml") or path.endswith("yml"):
        with open(path, 'r') as f:
            try:
                content = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)
    elif path.endswith("json"):
        with open(path, 'r') as f:
            try:
                content = json.load(f)
            except json.JSONDecodeError as exc:
                print(exc)
    else:
        raise ValueError("Invalid File")

    return {
        "title" : content["info"]["title"],
        "description" : content["info"]["description"],
        "version" : content["info"]["version"],
        "path" : path
    }