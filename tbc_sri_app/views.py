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
