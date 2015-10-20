import json


config = {
        "age":{
            "18":0.5
            },
        "gender":{
            "male":0.5,
            "female":0.5
            },
        "race":{
            "caucasian":0.6
            },
        "nationality":{
            "german":0.6,
            "indian":0.5
            }
        }

def read_config():
    base_attributes =[]
    for attr,vals in config.iteritems():
        base_attributes.append(attr)
    return base_attributes
read_config()
