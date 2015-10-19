from django.shortcuts import render
from django.http import HttpResponse
from xml.dom.minidom import Document
# Create your views here.

def index(request):
    attr = ['age','sex','gender']
    data = {}
    for val in attr:
        data[val] = request.GET.get(val)
    base = make_dom(data)
    x = "<html><body>Hi there %s</body></html>" %base
    print base
    return HttpResponse(x)
def make_dom(dict):
    doc = Document()
    base = doc.createElement("Attributes")
    x = doc.appendChild(base)
    for k,v in dict.iteritems():
        element = doc.createElement(k)
        content = doc.createTextNode(v)
        element.appendChild(content)
        base.appendChild(element)
    print base.toprettyxml()
    return base.toprettyxml()
