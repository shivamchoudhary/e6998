from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from django.template import loader, Context
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from xml.dom.minidom import Document
import Common
from collections import OrderedDict
import random
import json
import experiment_detect
import openwpm_wrapper

def index(request):
    return render_to_response('base.html')

def test(request):
    query_params = request.META['QUERY_STRING']
    dict = tokenize(query_params)
    base = make_dom(dict)
    t = loader.get_template('test.html')
    c = Context(base)
    return render_to_response('test.html', context = c)

@csrf_exempt
def configure(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        return render_to_response('configure.html')
    else:
        json_data = json.loads(request.body)
        with open('./attribute/config.json', 'w') as f:
            f.write(json_data["config"])
        print json_data['openwpm_dir']
        print json_data['iterations']
        print json_data['num_browers']
        print json_data['sites']
        print json_data['db_dir']
        #openwpm_wrapper.startExperiment(json_data['openwpm_dir'], json_data['num_browers'], json_data['iterations'], json_data['sites'])
        return HttpResponse("Successfully received!") 

def chart(request):
    response_data = {}
    response_data['message'] = 'ajax message'
    pvals = experiment_detect.pvals()
    #num_experiment = pvals.num_experiment()
    experiment_prob = pvals.run_exp()
    ordered_prob =  OrderedDict(sorted(experiment_prob.items()))
    number_data = []
    for k, v in ordered_prob.iteritems():
        current_data = {}
        current_data['y'] = k
        current_data['s'] = v
        number_data.append(current_data)
    """ morris chart data format
    number_data = [{'y': '0.9', 's': 1}]
            #,{'y':'0.6', 'a':90, 'b':90}]
    """
    #print number_data
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

