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
import os
import experiment_detect
import experiment_detect_multielements
import experiment_detect_dryrun
import openwpm_wrapper

def index(request):
    return render_to_response('base.html')

def dryrun(request):
    return render_to_response('dryrun.html')

def test(request):
    query_params = request.META['QUERY_STRING']
    print query_params
    if query_params == '':
        return render_to_response('testConfig.html')
    dict = tokenize(query_params)
    base = make_dom(dict)
    t = loader.get_template('test.html')
    c = Context(base)
    return render_to_response('test.html', context = c)

def multielements(request):
    return render_to_response('multielements.html')

def visualization(request,path):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    visualization_filename = os.path.join(BASE_DIR,"attribute/result/localhost/" + path)
    if path =="":
        return render_to_response("Visualization.html")
    else:
        return render_to_response(visualization_filename)

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
        print json_data['dataObservatory_dir']
        openwpm_wrapper.startExperiment(json_data['openwpm_dir'], json_data['num_browers'], json_data['iterations'], json_data['sites'])
        return HttpResponse("Successfully received!") 

def probability(request):
    response_data = {}
    number_data = []
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.join(BASE_DIR,"attribute/pvalues/")
    number_data += [each.split("prob")[1] for each in os.listdir(BASE_DIR)]
    response_data['probability'] = number_data
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def multiprobability(request):
    response_data = {}
    number_data = []
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.join(BASE_DIR,"attribute/multipvalues/")
    number_data += [each.split("condition")[1] for each in os.listdir(BASE_DIR)]
    response_data['probability'] = number_data
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def dryrunnumber(request):
    response_data = {}
    number_data = []
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.join(BASE_DIR,"attribute/dry_run/")
    number_data += [each.split("condition")[1] for each in os.listdir(BASE_DIR)]
    response_data['probability'] = number_data
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def chart(request):
    json_data = json.loads(request.body)
    response_data = {}
    response_data['message'] = 'ajax message'
    prob_flag = json_data['request_prob'] 
    prob_array = []
    if prob_flag == -1:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        BASE_DIR = os.path.join(BASE_DIR,"attribute/pvalues/")
        prob_array += [each.split("prob")[1] for each in os.listdir(BASE_DIR)]
    else:
        prob_array += [prob_flag]
    print prob_array

    number_data = []
    prob_ykeys = []
    for current_prob in prob_array:
        prob_ykeys += ['prob' + current_prob]
        pvals = experiment_detect.pvals(current_prob)
        #num_experiment = pvals.num_experiment()
        experiment_prob = pvals.run_exp()
        ordered_prob = OrderedDict(sorted(experiment_prob.items(), key=lambda x:int(x[0])))
        #print ordered_prob
        #number_data = []
        for k, v in ordered_prob.iteritems():
            found = 0
            for ele in number_data:
                if ele['y'] == k:
                    existing_data = ele
                    found = 1
            if found == 0:
                current_data = {}
                current_data['y'] = k
                current_data['prob' + str(current_prob)] = v
                number_data.append(current_data)
            else:
                existing_data['prob' + str(current_prob)] = v
    #number_data = number_data.sort(key=lambda x:int(x['y']))
    number_data = sorted(number_data, key=lambda x:int(x['y']))
    print prob_ykeys
    """ morris chart data format
    number_data = [{'y': '0.9', 's': 1}]
            #,{'y':'0.6', 'a':90, 'b':90}]
    """
    response_data['chartInfo'] = number_data
    response_data['currentProb'] = current_prob
    response_data['ykey_data'] = prob_ykeys
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def multichart(request):
    json_data = json.loads(request.body)
    response_data = {}
    response_data['message'] = 'ajax message'
    prob_flag = json_data['request_prob'] 
    prob_array = []
    if prob_flag == -1:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        BASE_DIR = os.path.join(BASE_DIR,"attribute/multipvalues/")
        prob_array += [each.split("prob")[1] for each in os.listdir(BASE_DIR)]
    else:
        prob_array += [prob_flag]
    #print prob_array

    number_data = []
    prob_ykeys = []
    for current_prob in prob_array:
        #prob_ykeys += ['prob' + current_prob]
        pvals = experiment_detect_multielements.pvals(current_prob)
        #num_experiment = pvals.num_experiment()
        experiment_prob = pvals.run_exp()
        #print experiment_prob
        ordered_prob = OrderedDict(sorted(experiment_prob.items(), key=lambda x:int(x[0])))
        #print ordered_prob
        #number_data = []
        for k, v in ordered_prob.iteritems():
            found = 0 
            for ele, elev in v.iteritems():
                #print ele, elev
                if not ( 'prob' + str(current_prob) + ele in prob_ykeys):
                    prob_ykeys.append('prob' + str(current_prob) + ele)
                if found == 0:
                    current_data = {}
                    current_data['y'] = k
                    current_data['prob' + str(current_prob) + ele] = elev
                    #print current_data
                    number_data.append(current_data)
                    found = 1
                    existing_data = current_data
                else:
                    existing_data['prob' + str(current_prob) + ele] = elev 
   #number_data = number_data.sort(key=lambda x:int(x['y']))
    print number_data
    number_data = sorted(number_data, key=lambda x:int(x['y']))
    #print prob_ykeys
    """ morris chart data format
    number_data = [{'y': '0.9', 's': 1}]
            #,{'y':'0.6', 'a':90, 'b':90}]
    """
    response_data['chartInfo'] = number_data
    response_data['currentProb'] = current_prob
    response_data['ykey_data'] = prob_ykeys
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def dryrunchart(request):
    json_data = json.loads(request.body)
    response_data = {}
    response_data['message'] = 'ajax message'
    prob_flag = json_data['request_prob'] 
    prob_array = []
    if prob_flag == -1:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        BASE_DIR = os.path.join(BASE_DIR,"attribute/dry_run/")
        prob_array += [each.split("prob")[1] for each in os.listdir(BASE_DIR)]
    else:
        prob_array += [prob_flag]
    #print prob_array

    number_data = []
    prob_ykeys = []
    for current_prob in prob_array:
        #prob_ykeys += ['prob' + current_prob]
        pvals = experiment_detect_dryrun.pvals(current_prob)
        #num_experiment = pvals.num_experiment()
        experiment_prob = pvals.run_exp()
        #print experiment_prob
        ordered_prob = OrderedDict(sorted(experiment_prob.items(), key=lambda x:int(x[0])))
        #print ordered_prob
        #number_data = []
        for k, v in ordered_prob.iteritems():
            found = 0 
            for ele, elev in v.iteritems():
                #print ele, elev
                if not ( 'prob' + str(current_prob) + ele in prob_ykeys):
                    prob_ykeys.append('prob' + str(current_prob) + ele)
                if found == 0:
                    current_data = {}
                    current_data['y'] = k
                    current_data['prob' + str(current_prob) + ele] = elev
                    #print current_data
                    number_data.append(current_data)
                    found = 1
                    existing_data = current_data
                else:
                    existing_data['prob' + str(current_prob) + ele] = elev 
    #number_data = number_data.sort(key=lambda x:int(x['y']))
    print number_data 
    number_data = sorted(number_data, key=lambda x:int(x['y']))
    #print prob_ykeys
    """ morris chart data format
    number_data = [{'y': '0.9', 's': 1}]
            #,{'y':'0.6', 'a':90, 'b':90}]
    """
    response_data['chartInfo'] = number_data
    response_data['currentProb'] = current_prob
    response_data['ykey_data'] = prob_ykeys
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

