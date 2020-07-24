from typing import Any, List
import json
import os

AMS_CAMERA_ROOT_PATH = os.path.join(os.path.dirname(__file__), '../')
CONFIG_PATH = '/'.join([
    AMS_CAMERA_ROOT_PATH,
    'camera_config.json',
])

class KeyNotExist(Exception):
    pass

def read_json(json_path: str) -> dict:
     with open(json_path) as f:
         return json.load(f)

def get_config() -> dict:
    return read_json(CONFIG_PATH)

def get_config_items(keys: List[str]) -> dict:
    config = get_config()
    result = {}
    for key in keys:
        if key not in config:
            raise KeyNotExist('key: {key} does not exist.'.format(key = key))
        result[key] = config[key]
    return result

def get_config_item(key: str) -> Any:
    return get_config_items([key])[key]
