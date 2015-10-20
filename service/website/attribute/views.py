from django.shortcuts import render
from django.http import HttpResponse
from xml.dom.minidom import Document
import Common
import random
def index(request):
    query_params = request.META['QUERY_STRING']
    dict = tokenize(query_params)
    base = make_dom(dict)
    x = "<html><body>Hi there %s</body> </html>" %base
    return HttpResponse(x)

def tokenize(query_params):
    delimiter = "&"
    input = query_params.split(delimiter)
    input_attribute = {}
    for pairs in input:
        pairs = pairs.split("=")
        input_attribute[pairs[0]] = pairs[1]
    return input_attribute

def make_dom(dict):
    doc = Document()
    base = doc.createElement("Attributes")
    x = doc.appendChild(base)
    base_attributes = Common.read_config()
    for k,v in dict.iteritems():
        if k in base_attributes:
            p = random.random()
            if p <=Common.config[k][v]:
                element = doc.createElement(k)
                content = doc.createTextNode(v)
                element.appendChild(content)
                base.appendChild(element)
            elif p>Common.config[k][v]:
                element = doc.createElement(k)
                content = doc.createTextNode('Fixed')
                element.appendChild(content)
                base.appendChild(element)
                element = doc.createElement("img")
                element.attributes['src'] = "http://www.w3schools.com/images/lamp.gif"
                element.attributes['alt'] = "text"
                element.attributes['width'] = "100"
                element.attributes['height']="100"
                base.appendChild(element)
    return base.toprettyxml()
