import os
import json

CONFIG_PATH = os.path.expanduser("~/fasterfastapi_config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}

def save_config(config  ):
    with open(CONFIG_PATH, "w") as f:
        return json.dump(config, f, indent=4)


