import User
from xml.dom.minidom import Document
import random
delimiter = "&"

def tokenize(input):
    input = input.split(delimiter)
    input_attribute = {}
    for pairs in input:
        pairs = pairs.split("=")
        input_attribute[pairs[0]] = pairs[1]
    choice = random.randint(0,1)
    if choice ==0:
        make_dom(input_attribute)
    else:
        base_dom(input_attribute)
    return input_attribute

def make_dom(input_attribute):
    doc = Document()
    base = doc.createElement("Attributes")
    x = doc.appendChild(base)
    for k,v in input_attribute.iteritems():
        element = doc.createElement(k)
        content = doc.createTextNode(v)
        element.appendChild(content)
        base.appendChild(element)
    print doc.toprettyxml()

def base_dom(input_attribute):
    doc = Document()
    base  = doc.createElement("Attributes")
    x = doc.appendChild(base)
    for k,v in input_attribute.iteritems():
        element = doc.createElement(k)
        content = doc.createTextNode("Fixed")
        element.appendChild(content)
        base.appendChild(element)
    print doc.toprettyxml()
tokenize("gender=m&nation=Germany&age=23")




