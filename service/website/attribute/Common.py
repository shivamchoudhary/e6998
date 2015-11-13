import json
config = {
        "gender":{
            "male":{
                0.7:"Male",
                0.3:"Default"
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
            "germany":{
                0.6:"German",
                0.4:"Default"
                },
            "india":{
                0.2:"Indian",
                0.8:"Default"
                }
            }
        }

def read_config():
    base_attributes =[]
    for attr,vals in config.iteritems():
        base_attributes.append(attr)
    return base_attributes
