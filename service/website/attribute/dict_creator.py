import os
import json
import pprint
def create_dict():
    attr_dict = {}
    for file in os.listdir('/home/shivam/OpenWPM/demo_results'):
        if file.endswith(".html"):
            attr_dict[file]={}
            name = file.split(".")[0]
            geo = name.split("=")[1]
            attr_dict[file]["geo"]=geo
    attr_dict["all_values"] = {}
    all_geo = ["germany","india"]
    attr_dict["all_values"]["geo"]=all_geo
    with open('/home/shivam/OpenWPM/demo_results/localhost_dict.json','w') as outfile:
        json.dump(attr_dict,outfile,indent=4)
create_dict()
