import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR,"attribute")
def open_config():
    with open(BASE_DIR+"/config.json") as conf:
        config = json.load(conf)
    return config
def read_config():
    base_attributes =[]
    config = open_config()
    for attr,vals in config.iteritems():
        base_attributes.append(attr)
    return base_attributes
