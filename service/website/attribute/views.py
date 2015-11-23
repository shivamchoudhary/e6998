from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from django.template import loader, Context
from xml.dom.minidom import Document
import Common
import random
import json
import experiment_detect

def index(request):
    return render_to_response('base.html')

def test(request):
    query_params = request.META['QUERY_STRING']
    dict = tokenize(query_params)
    base = make_dom(dict)
    t = loader.get_template('test.html')
    c = Context(base)
    return render_to_response('test.html', context = c)

def chart(request):
    response_data = {}
    response_data['message'] = 'ajax message'
    number_data = [{'y': '0.5', 'a': 100, 'b': 100},{'y':'0.6', 'a':90, 'b':90}]
    response_data['chartInfo'] = number_data
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def tokenize(query_params):
    delimiter = "&"
    input = query_params.split(delimiter)
    input_attribute = {}
    for pairs in input:
        pairs = pairs.split("=")
        input_attribute[pairs[0]] = pairs[1]
    return input_attribute

def make_dom(dict):
    attr_dict = {}
    base_attributes = Common.read_config()
    config = Common.open_config()
    for k,v in dict.iteritems():
        if k in base_attributes:
            p = random.random()
            sumK = 0
            attr_values = config[k][v]
            for k1 , val1 in attr_values.iteritems():
                sumK += float(k1)
                if (p<sumK):
                    attr_dict[k] = val1
                    break
    return attr_dict

