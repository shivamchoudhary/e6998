from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from django.template import loader, Context
from xml.dom.minidom import Document
import Common
import random

def index(request):
    return render_to_response('base.html')

def test(request):
    query_params = request.META['QUERY_STRING']
    dict = tokenize(query_params)
    base = make_dom(dict)
    t = loader.get_template('test.html')
    c = Context(base)
    return render_to_response('test.html', context = c)

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
    output = {}
    base_attributes = Common.read_config()
    for k,v in dict.iteritems():
        if k in base_attributes:
            p = random.random()
            sumK = 0
            attr_values = Common.config[k][v] 
            for k1 , val1 in attr_values.iteritems():
                sumK += k1
                if (p<sumK):
                    output[k] = val1
                    break
    return output

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

