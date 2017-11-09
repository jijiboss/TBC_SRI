from django.shortcuts import render
from django.template import loader
from .models import lnos_statusPipeLine
from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import HttpRequest #https://docs.djangoproject.com/en/dev/ref/request-response/
from django.core import serializers
import json
from django.views.decorators.csrf import ensure_csrf_cookie

#=================================
#for debugging
#https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/
#import pdb

#just for experimenting purposes. DO not use "csrf_exempt" in production
#from django.views.decorators.csrf import csrf_exempt
#=================================
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
#To see if the data was returned to the calling HTML, go to the Network tab and look for the XHR entry.
#The Response tab will have the actual returned data, or "failure".
#Also can test out this query and result by tryin them on the python shell;
#   python manage.py shell
def myLoadData(request):

    #run the query
    myQuerySet = lnos_statusPipeLine.objects.values('mbol','container')
    #cast from QuerySet to array
    try:
        response_data = list(myQuerySet)
    except:
        response_data = 'Failed to query data.'
    #convert the aray to JSON and return
    return HttpResponse(json.dumps(response_data), content_type="application/json")

#just for experimenting purposes. DO not use "csrf_exempt" in production
#@csrf_exempt
#@ensure_csrf_cookie
def myUpdateData(request):
    #request contains all info that were passed over form the client side
    #https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.body
    #first check the method to se if it is PUT
    if request.method == 'PUT':
        inMethod = "method: " + request.method + ". "
        inMIME = "MIME: " + request.content_type + ". "
#        inPayLoad = "payload: " + request.body + " "
#        return HttpResponse(inPayLoad) # this doesn't work due to bytes vs str
        return HttpResponse(request.body)
    else:
        return HttpResponse("response no update")
