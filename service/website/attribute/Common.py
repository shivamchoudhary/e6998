import json
import os
def open_config():

    with open('/home/shivam/e6998/service/website/attribute/config.json') as conf:
        config = json.load(conf)
    return config
def read_config():
    base_attributes =[]
    config = open_config()
    for attr,vals in config.iteritems():
        base_attributes.append(attr)
    return base_attributes
