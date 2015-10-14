import User
from xml.dom import minidom
delimiter = "&"

def tokenize(input):
    input = input.split(delimiter)
    input_attribute = {}
    for pairs in input:
        pairs = pairs.split("=")
        input_attribute[pairs[0]] = pairs[1]
    return input_attribute

def make_dom():
    doc = minidom.Document()
    elem = doc.createElement("one")
    elem.setAttribute("id","1")
    doc.appendChild(elem)
make_dom()
User.User('shivam',tokenize("gender=m&nation=d"))



