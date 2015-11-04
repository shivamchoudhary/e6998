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
            sumK = 0
            attr_values = Common.config[k][v] 
            for k1 , val1 in attr_values.iteritems():
                sumK += k1
                if (p<sumK):
                    element = doc.createElement(k)
                    content = doc.createTextNode(val1)
                    element.appendChild(content)
                    base.appendChild(element)
                    break
    return base.toprettyxml()

def dry_run(dict):
    base_attributes = Common.read_config()
    for k,v in dict.iteritems():
        if k in base_attributes:
            p = random.random()
            sumK = 0
            attr_values = Common.config[k][v] 
            for k1 , val1 in attr_values.iteritems():
                sumK += k1
                if (p<sumK):
                    return val1
                    # break

