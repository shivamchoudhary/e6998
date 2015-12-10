import os
import json
import pprint
import sys
def create_dict():
    attr_dict = {}
    for file in os.listdir("/home/shivam/OpenWPM/demo_results"):
        if file.endswith(".html"):
            attr_dict[file]={}
            names = file.split("&")
            for name in names:
                geo = name.split("=")[1]
                if not geo.endswith(".html"):
                    attr_dict[file]["geo"]=geo
    attr_dict["all_values"] = {}
    all_geo = ["germany","india"]
    attr_dict["all_values"]["geo"]=all_geo
    with open("/home/shivam/OpenWPM/demo_results/localhost.json",'w') as outfile:
        json.dump(attr_dict,outfile,indent=4)

def main():
    create_dict()
if __name__=="__main__":
    main()
