import json
config = {
        "gender":{
            "male":{
                0.7:"0.7 more beautiful",
                0.2:"Default",
                0.1:"Hi"
                },
            "female":
                    {
                0.4:"Female",
                0.6:"Default"
                }
            },
        "race":{
            "caucasian":{
                0.8:"Caucasian",
                0.2:"Default"
                }
            },
        "country":{
            "german":{
                0.6:"German",
                0.4:"Default"
                },
            "indian":{
                0.2:"indian",
                0.8:"Default"
                }
            }
        }

def read_config():
    base_attributes =[]
    for attr,vals in config.iteritems():
        base_attributes.append(attr)
    return base_attributes
# read_config()
