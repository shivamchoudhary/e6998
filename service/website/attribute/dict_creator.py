import os
import json
import pprint
import sys
def create_dict(fname):
    attr_dict = {}
    for file in os.listdir(os.environ['OPENWPM_DIR']+"/"+fname+"_results"):
        if file.endswith(".html"):
            attr_dict[file]={}
            name = file.split(".")[0]
            geo = name.split("=")[1]
            attr_dict[file]["geo"]=geo
    attr_dict["all_values"] = {}
    all_geo = ["germany","india"]
    attr_dict["all_values"]["geo"]=all_geo
    with open(os.environ['OPENWPM_DIR']+"/"+fname+"_results/localhost.json",'w') as outfile:
        json.dump(attr_dict,outfile,indent=4)


def main():
    fname = sys.argv[1]
    create_dict(fname)

if __name__=="__main__":
    main()
