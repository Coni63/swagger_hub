import yaml

def get_info(path):
    with open(path, 'r') as stream:
        try:
            content = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return {
        "title" : content["info"]["title"],
        "description" : content["info"]["description"],
        "version" : content["info"]["version"],
        "path" : path
    }