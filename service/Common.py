import json

def read_attributes(fname):
    attributes = {}
    with open (fname,'r') as conf:
        configuration = json.loads(conf.read()) 
        attribs = configuration['attributes']
        for attrib in attribs:
            attributes[attrib] = ""
    return attributes
