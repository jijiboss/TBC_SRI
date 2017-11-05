from django.shortcuts import render
from django.template import loader
from .models import lnos_statusPipeLine
from django.forms import model_to_dict
from django.http import HttpResponse
from django.core import serializers
import json
import pdb

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def helloWorld(request, namae):
    return HttpResponse("Hello world %s!" % namae)

def index(request):
    #add code here
    #https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-render
    return render(request, 'tbc_sri_app/index.html')

def sritable(request):
    return render(request, 'tbc_sri_app/sritable.html')

def jquery01(request):
    return render(request, 'tbc_sri_app/jquery01.html')

def sritable3(request):
    #load in the template and create a variable as a reference to the template
    template = loader.get_template('tbc_sri_app/sritable3.html')
    return render(request, 'tbc_sri_app/sritable3.html')

#I can test this method by calling this URL on the browser directly.
#if successful, i shoudl see the query results.
#To see if the data was returned to the calling HTML, go to the Network taband lok for the XHR entry.
#The Response tab will have the actual returned data, or "failure".
def myLoadData(request):

    #run the query
    myQuerySet = lnos_statusPipeLine.objects.values('mbol','container')
    #create an empty dict to put the data in
    try:
        response_data = list(myQuerySet)
    except:
        response_data = 'Failed to query data.'

    return HttpResponse(json.dumps(response_data), content_type="application/json")
