import json


config = {
        "age":0.5,
        "sex":0.5,
        "race":0.6,
        "nationality":"0.7"
        }

def read_config():
    base_attributes =[]
    for attr,prob in config.iteritems():
        base_attributes.append(attr)

    return base_attributes

