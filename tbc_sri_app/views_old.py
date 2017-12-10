from django.shortcuts import render
from django.template import loader
from .models import lnos_statusPipeLine
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest #https://docs.djangoproject.com/en/dev/ref/request-response/
from django.core import serializers
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import lnosStatusPipeLineSerializer
#=================================
#for REST framework
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#=================================
#for debugging
#https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/
#import pdb

#just for experimenting purposes. DO not use "csrf_exempt" in production
#from django.views.decorators.csrf import csrf_exempt
#=================================
"""
    ================
    old code, delete
    ================

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def helloWorld(request, namae):
    return HttpResponse("Hello world %s!" % namae)

def sritable(request):
    return render(request, 'tbc_sri_app/sritable.html')

def jquery01(request):
    return render(request, 'tbc_sri_app/jquery01.html')

#I can test this method by calling this URL on the browser directly.
#if successful, i shoudl see the query results.
#To see if the data was returned to the calling HTML, go to the Network tab and look for the XHR entry.
#The Response tab will have the actual returned data, or "failure".
#Also can test out this query and result by tryin them on the python shell;
#   python manage.py shell
def myLoadData(request):

    #run the query
    myQuerySet = lnos_statusPipeLine.objects.values('pk','mbol','container')
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
    #first check the method to see if it is PUT
    if request.method == 'PUT':
        #Let's see what data came through
        print('*' *50) #should print in the dos prompt console
        print('DEBUG STUFF   ' * 5)

        print("incoming data => ", request.body) #b'{"pk":24,"mbol":"ZIMUBKK8004895","container":"daf"}'
        strInData = request.body.decode("utf-8")
        print("strInData => ", strInData) #{"pk":24,"mbol":"ZIMUBKK8004895","container":"daf"}
        listInData = json.loads(strInData)
        print("listInData => ", listInData) #{'pk': 24, 'mbol': 'ZIMUBKK8004895', 'container': 'das'}
        jsonInData = json.dumps(listInData)
        print("jsonInData => ", jsonInData) #{"pk": 24, "mbol": "ZIMUBKK8004895", "container": "das"}

        #check few other request detail or fun
        inMethod = "method: " + request.method + ". "
        print("inMethod => ", inMethod)
        inMIME = "MIME: " + request.content_type + ". "
        print("inMIME => ", inMIME)
        print('*' *50)

        #try to load the data into the model
#        for deserialized_object in serializers.deserialize("json", request.body):
#            deserialized_object.save()
        foo = lnos_statusPipeLine(**listInData)
        foo.save()

        return HttpResponse(strInData)
    else:
        return HttpResponse("response no update")
"""

def index(request):
    #add code here
    #https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-render
    return render(request, 'tbc_sri_app/index.html')

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
#Take 2 in attept to understand REST better
#http://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
def myLoadData02(request):
    #List all existing or create new
    if request.method == 'GET':
        cargo = lnos_statusPipeLine.objects.all()
        serializer = lnosStatusPipeLineSerializer(cargo, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = lnosStatusPipeLineSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

def myUpdateData02(request, pk):

    """
        Because I need to pass pk, need to update the JS with the following...

            var thisPK = item["pk"] //need to get the pk to pass with the PUT request
            ...
            url: 'myUpdateData02/' + thisPK,
            ...

        Then update urls.py accordingly

            url(r'^myUpdateData02/(?P<pk>[0-9]+)$', views.myUpdateData02, name='myUpdateData02'),
    """

    #Retrieve, update or delete

    print('***********')
    #try getting the 'pk' instance
    try:
        cargo = lnos_statusPipeLine.objects.get(pk = pk)
    #return Not FOund 404 if not found
    except lnos_statusPipeLine.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        #Serializer will return the instance object in Python native format
        serializer = lnosStatusPipeLineSerializer(cargo)
        #Return JSON-fied representation of the instance data
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        #JSONParser() => parse request content that is in JSON format
        #.parse(request) => parse stream-like object representing the body of the request
        #http://www.django-rest-framework.org/api-guide/parsers/#custom-parsers
        #parse the stream into Python native data type
        data = JSONParser().parse(request)
        #then turn that into a dictionary of validated data
        serializer = lnosStatusPipeLineSerializer(cargo, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        cargo.delete()
        return HttpResponse(status = 204)
