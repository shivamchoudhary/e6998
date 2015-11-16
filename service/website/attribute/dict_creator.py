import os

def create_dict():
    attr_dict = {}
    for file in os.listdir('/home/shivam/OpenWPM/demo_results'):
        if file.endswith(".html"):
            attr_dict[file]={}
            name = file.split(".")[0]
            geo = name.split("=")[1]
            attr_dict[file]['geo']=geo
    attr_dict['all_values'] = {}
    all_geo = ['germany','india']
    attr_dict['all_values']['geo']=all_geo
create_dict()
