from django.shortcuts import render
from django.http import HttpResponse
from xml.dom.minidom import Document
import Common
def index(request):
    query_params = request.META['QUERY_STRING']
    dict = tokenize(query_params)
    base = make_dom(dict)
    x = "<html><body>Hi there %s</body></html>" %base
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
    for k,v in dict.iteritems():
        element = doc.createElement(k)
        content = doc.createTextNode(v)
        element.appendChild(content)
        base.appendChild(element)
    return base.toprettyxml()
