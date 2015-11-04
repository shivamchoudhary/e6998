import json
config = {
        "age":{
            "18":0.5
            },
        "gender":{
            "male":{
                0.7:"Testing",
                "default":"Default"
                },
            "female":
                    {
                "0.5":"Female",
                "default":"Default"
                }
            },
        "race":{
            "caucasian":0.6
            },
        "country":{
            "german":{
                "0.6":"German",
                "default":"Default"
                },
            "indian":{
                "0.5":"Indian",
                "default":"Default"
                }
            }
        }

def read_config():
    base_attributes =[]
    for attr,vals in config.iteritems():
        base_attributes.append(attr)
    return base_attributes
# read_config()
